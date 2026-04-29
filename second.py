# ============================================================
# ADIM 2 — TAM VERİ ANALİZİ (LEXICON TABANLI)
#
# Hazır model kullanılmaz. Tamamen turkce_sarki_lexicon.csv
# içindeki kelimelerin ağırlıklı geçiş olasılığına göre
# tür ve duygu tahmini yapılır.
#
# Algoritma:
#   - Şarkı sözündeki her kelime lexiconda aranır
#   - Eşleşen her kelime için: ağırlık puanı biriktirilir
#   - Tür/duygu için: puan / toplam_puan = olasılık
#   - En yüksek olasılıklı tür ve duygu seçilir
#
# CSV formatı (ikisi de desteklenir):
#   singing;lyrics   veya   lyrics
#
# Çalıştırma:
#   python 2_analiz.py
#   python 2_analiz.py --limit 500
#   python 2_analiz.py --limit 500 --batch-rapor 50
# ============================================================

import argparse
import os
import re
import sys
import pandas as pd
from tqdm import tqdm
from collections import defaultdict

tqdm.pandas()

# ─────────────────────────────────────────
# AYARLAR
# ─────────────────────────────────────────
CSV_YOLU         = "./909090.csv"
LEXICON_YOLU     = "./turkce_sarki_lexicon.csv"
CIKTI_YOLU       = "./sarki_analiz_sonuclari.csv"
CHECKPOINT_YOLU  = "./checkpoint_analiz.csv"

# ─────────────────────────────────────────
# LEXICON YÜKLE
# ─────────────────────────────────────────

def lexicon_yukle():
    if not os.path.exists(LEXICON_YOLU):
        print(f"❌ Lexicon bulunamadı: {LEXICON_YOLU}")
        print("   Önce şunu çalıştır: python gen.py")
        sys.exit(1)

    lex = pd.read_csv(LEXICON_YOLU, encoding="utf-8-sig")
    print(f"✅ Lexicon yüklendi: {len(lex)} giriş")

    # Hızlı arama için dict: kelime → [(tur, duygu, tema, agirlik), ...]
    lookup: dict[str, list] = defaultdict(list)
    for _, row in lex.iterrows():
        kelime = str(row["kelime"]).strip().lower()
        lookup[kelime].append({
            "tur":     row["tur"],
            "duygu":   row["duygu"],
            "tema":    row["tema"],
            "agirlik": float(row["agirlik"]),
        })

    return lookup


# ─────────────────────────────────────────
# VERİ YÜKLE
# ─────────────────────────────────────────

def veri_yukle(limit: int = None) -> pd.DataFrame:
    print(f"\n📂 Veri yükleniyor: {CSV_YOLU}")

    with open(CSV_YOLU, encoding="utf-8") as f:
        ilk_satir = f.readline().strip()

    ayirici = ";" if ";" in ilk_satir else ","
    sutunlar_ham = [s.strip().lower() for s in ilk_satir.split(ayirici)]

    # Lyrics ve singing sütun indekslerini bul
    lyrics_idx  = None
    singing_idx = None

    for i, s in enumerate(sutunlar_ham):
        if "lyric" in s or "sozu" in s or "söz" in s:
            lyrics_idx = i
        if "sing" in s or "sanat" in s or "artist" in s:
            singing_idx = i

    if lyrics_idx is None:
        if len(sutunlar_ham) == 1:
            lyrics_idx = 0
        elif len(sutunlar_ham) >= 2:
            lyrics_idx = 1   # singing;lyrics → lyrics sonda
            if singing_idx is None:
                singing_idx = 0

    df_raw = pd.read_csv(
        CSV_YOLU, sep=ayirici, encoding="utf-8",
        on_bad_lines="skip", header=None, skiprows=1
    )

    df = pd.DataFrame()
    df["lyrics"] = df_raw.iloc[:, lyrics_idx].astype(str)

    if singing_idx is not None and singing_idx < len(df_raw.columns):
        df["singing"] = df_raw.iloc[:, singing_idx].astype(str)
    else:
        df["singing"] = "bilinmiyor"

    # Temizle
    df = df[df["lyrics"].notna()]
    df = df[df["lyrics"].str.strip() != ""]
    df = df[df["lyrics"].str.strip().str.lower() != "nan"]
    df["lyrics"] = (
        df["lyrics"]
        .str.replace("\\n", " ", regex=False)
        .str.replace("\n",  " ", regex=False)
        .str.strip()
    )
    df["word_count"] = df["lyrics"].apply(lambda x: len(str(x).split()))
    df = df[df["word_count"] >= 5].reset_index(drop=True)

    if limit:
        df = df.head(limit)

    print(f"✅ {len(df)} şarkı yüklendi (min 5 kelime)")
    return df


# ─────────────────────────────────────────
# TEMEL ANALİZ FONKSİYONU
# ─────────────────────────────────────────

def metin_temizle(metin: str) -> list[str]:
    """Metni küçük harfe çevirir, noktalama kaldırır, token listesi döner."""
    metin = metin.lower()
    metin = re.sub(r"[^\w\s]", " ", metin)
    return metin.split()


def sarki_analiz_et(lyrics: str, lookup: dict) -> dict:
    """
    Şarkı sözünü analiz eder.
    Dönüş:
        tur            : en olası tür
        tur_olasilik   : 0.0–1.0
        duygu          : en olası duygu
        duygu_olasilik : 0.0–1.0
        tema           : en olası tema
        eslesen_kelime : eşleşen kelime sayısı
        tur_dagilim    : {tür: olasılık} tüm türler
        duygu_dagilim  : {duygu: olasılık} tüm duygular
    """
    tokenlar = metin_temizle(lyrics)
    metin_lower = lyrics.lower()

    tur_puan:   dict[str, float] = defaultdict(float)
    duygu_puan: dict[str, float] = defaultdict(float)
    tema_puan:  dict[str, float] = defaultdict(float)
    eslesen = 0

    # 1. Tek kelime eşleşmeleri
    for token in tokenlar:
        if token in lookup:
            eslesen += 1
            for kayit in lookup[token]:
                tur_puan[kayit["tur"]]   += kayit["agirlik"]
                duygu_puan[kayit["duygu"]] += kayit["agirlik"]
                tema_puan[kayit["tema"]]  += kayit["agirlik"]

    # 2. Bigram / çok kelimeli ifade eşleşmeleri
    for kelime, kayitlar in lookup.items():
        if " " in kelime and kelime in metin_lower:
            sayi = metin_lower.count(kelime)
            eslesen += sayi
            for kayit in kayitlar:
                tur_puan[kayit["tur"]]   += kayit["agirlik"] * sayi * 1.5  # çok kelime bonus
                duygu_puan[kayit["duygu"]] += kayit["agirlik"] * sayi * 1.5
                tema_puan[kayit["tema"]]  += kayit["agirlik"] * sayi * 1.5

    toplam_tur   = sum(tur_puan.values())
    toplam_duygu = sum(duygu_puan.values())
    toplam_tema  = sum(tema_puan.values())

    if toplam_tur == 0:
        # Hiç eşleşme yok → varsayılan
        return {
            "tur": "pop", "tur_olasilik": 0.0,
            "duygu": "genel", "duygu_olasilik": 0.0,
            "tema": "genel", "eslesen_kelime": 0,
            "tur_dagilim": {}, "duygu_dagilim": {},
        }

    # Olasılıkları hesapla
    tur_dagilim   = {k: round(v / toplam_tur, 4)   for k, v in tur_puan.items()}
    duygu_dagilim = {k: round(v / toplam_duygu, 4) for k, v in duygu_puan.items()}
    tema_dagilim  = {k: round(v / toplam_tema, 4)  for k, v in tema_puan.items()}

    en_tur   = max(tur_dagilim,   key=tur_dagilim.get)
    en_duygu = max(duygu_dagilim, key=duygu_dagilim.get)
    en_tema  = max(tema_dagilim,  key=tema_dagilim.get)

    return {
        "tur":            en_tur,
        "tur_olasilik":   tur_dagilim[en_tur],
        "duygu":          en_duygu,
        "duygu_olasilik": duygu_dagilim[en_duygu],
        "tema":           en_tema,
        "eslesen_kelime": eslesen,
        "tur_dagilim":    dict(sorted(tur_dagilim.items(), key=lambda x: -x[1])),
        "duygu_dagilim":  dict(sorted(duygu_dagilim.items(), key=lambda x: -x[1])),
    }


# ─────────────────────────────────────────
# TOPLU ANALİZ
# ─────────────────────────────────────────

def toplu_analiz(df: pd.DataFrame, lookup: dict, batch_rapor: int = 100) -> pd.DataFrame:
    print(f"\n🔍 Analiz başlıyor: {len(df)} şarkı...")

    sonuclar = []
    for i, (_, row) in enumerate(tqdm(df.iterrows(), total=len(df), desc="Analiz")):
        s = sarki_analiz_et(str(row["lyrics"]), lookup)
        sonuclar.append({
            "singing":          row.get("singing", "bilinmiyor"),
            "lyrics_onizleme":  " ".join(str(row["lyrics"]).split()[:12]) + "...",
            "tur":              s["tur"],
            "tur_olasilik":     s["tur_olasilik"],
            "duygu":            s["duygu"],
            "duygu_olasilik":   s["duygu_olasilik"],
            "tema":             s["tema"],
            "eslesen_kelime":   s["eslesen_kelime"],
            "kelime_sayisi":    row.get("word_count", 0),
        })

        # Checkpoint
        if (i + 1) % batch_rapor == 0:
            gecici = pd.DataFrame(sonuclar)
            gecici.to_csv(CHECKPOINT_YOLU, index=False, encoding="utf-8-sig")
            tqdm.write(f"  💾 Checkpoint: {i+1}/{len(df)} şarkı kaydedildi")

    df_sonuc = pd.DataFrame(sonuclar)
    print(f"✅ Analiz tamamlandı: {len(df_sonuc)} şarkı")
    return df_sonuc


# ─────────────────────────────────────────
# RAPOR
# ─────────────────────────────────────────

def rapor_yazdir(df: pd.DataFrame):
    print()
    print("=" * 60)
    print("📊 ANALİZ RAPORU")
    print("=" * 60)

    # Tür dağılımı
    print("\n🎵 TÜR DAĞILIMI:")
    tur_say = df["tur"].value_counts()
    toplam  = len(df)
    for tur, sayi in tur_say.items():
        yuzde = sayi / toplam * 100
        bar   = "█" * int(yuzde / 2)
        print(f"  {tur:<12} {bar:<25} {sayi:>5} şarkı  (%{yuzde:.1f})")

    # Duygu dağılımı
    print("\n💬 DUYGU DAĞILIMI:")
    duygu_say = df["duygu"].value_counts()
    for duygu, sayi in duygu_say.items():
        yuzde = sayi / toplam * 100
        bar   = "█" * int(yuzde / 2)
        print(f"  {duygu:<14} {bar:<25} {sayi:>5} şarkı  (%{yuzde:.1f})")

    # Tür × Duygu tablosu
    print("\n📋 TÜR × DUYGU TABLOSU:")
    ct = pd.crosstab(df["tur"], df["duygu"])
    print(ct.to_string())

    # Ortalama eşleşme
    ort_eslesme = df["eslesen_kelime"].mean()
    sifir_eslesme = (df["eslesen_kelime"] == 0).sum()
    print(f"\n🔗 Ortalama eşleşen kelime sayısı : {ort_eslesme:.1f}")
    print(f"   Eşleşme bulunamayan şarkı sayısı: {sifir_eslesme} "
          f"(%{sifir_eslesme/toplam*100:.1f}) → pop/genel olarak etiketlendi")

    # Tür başına ortalama güven
    print("\n📈 TÜR BAŞINA ORTALAMA OLASILIK:")
    tur_guven = df.groupby("tur")["tur_olasilik"].mean().sort_values(ascending=False)
    for tur, guven in tur_guven.items():
        print(f"  {tur:<12} %{guven*100:.1f}")

    # Örnek şarkılar
    print("\n🎵 ÖRNEK SONUÇLAR (her türden 1 şarkı):")
    for tur in df["tur"].unique():
        row = df[df["tur"] == tur].iloc[0]
        print(f"\n  [{tur}]")
        print(f"   Sözler : {row['lyrics_onizleme']}")
        print(f"   Tür    : {row['tur']}  (olasılık: %{row['tur_olasilik']*100:.1f})")
        print(f"   Duygu  : {row['duygu']}  (olasılık: %{row['duygu_olasilik']*100:.1f})")
        print(f"   Tema   : {row['tema']}")

    print()
    print("=" * 60)


# ─────────────────────────────────────────
# ANA AKIŞ
# ─────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Türkçe şarkı sözü analizi — lexicon tabanlı, model gerektirmez"
    )
    parser.add_argument("--limit",       type=int, default=None,
                        help="Analiz edilecek maksimum şarkı sayısı (varsayılan: tümü)")
    parser.add_argument("--batch-rapor", type=int, default=100,
                        help="Kaç şarkıda bir checkpoint kaydedilsin (varsayılan: 100)")
    args = parser.parse_args()

    print("=" * 60)
    print("TÜRKÇE ŞARKI ANALİZİ — LEXICON TABANLI")
    print("Hazır model yok. Sadece kelime olasılıkları kullanılır.")
    print("=" * 60)

    lookup = lexicon_yukle()
    df     = veri_yukle(limit=args.limit)

    df_sonuc = toplu_analiz(df, lookup, batch_rapor=args.batch_rapor)

    df_sonuc.to_csv(CIKTI_YOLU, index=False, encoding="utf-8-sig")
    print(f"\n💾 Sonuçlar kaydedildi: {CIKTI_YOLU}")

    if os.path.exists(CHECKPOINT_YOLU):
        os.remove(CHECKPOINT_YOLU)

    rapor_yazdir(df_sonuc)

    print("\nSıradaki adım:")
    print("  python 3_test.py                         # interaktif test")
    print("  python 3_test.py --sarki 'sözler...'     # direkt test")
    print("─" * 60)


if __name__ == "__main__":
    main()