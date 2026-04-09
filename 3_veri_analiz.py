# ============================================================
# ADIM 3 — TAM VERİ ANALİZİ (DÜZELTİLMİŞ SÜRÜM)
#
# Değişiklikler:
#   ✅ Duygu label karışıklığı düzeltildi (positive/negative)
#   ✅ Tüm 5773 şarkı işleniyor (örnekleme kaldırıldı)
#   ✅ Checkpoint sistemi eklendi (kaldığı yerden devam)
#   ✅ Özetleme tekrar sorunu giderildi
#   ✅ Batch işleme ile duygu analizi hızlandırıldı
#
# SÜRE TAHMİNİ (Apple MPS):
#   Duygu analizi : ~5-8 dakika   (5773 şarkı)
#   Özetleme      : ~2.5-3 saat  (5773 şarkı × ~1.7sn)
#   → Sadece duygu için: python 3_veri_analiz.py --sadece-duygu
#
# Çalıştırma:
#   python 3_veri_analiz.py
#   python 3_veri_analiz.py --sadece-duygu
#   python 3_veri_analiz.py --sadece-duygu --batch-size 32
# ============================================================

import argparse
import os
import pandas as pd
import torch
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    AutoModelForSeq2SeqLM,
    pipeline,
)
from tqdm import tqdm
tqdm.pandas()

# ─────────────────────────────────────────
# AYARLAR
# ─────────────────────────────────────────
DATA_PATH       = "./909090.csv"
OUTPUT_PATH     = "./sarki_analiz_sonuclari.csv"
CHECKPOINT_PATH = "./sarki_analiz_checkpoint.csv"   # yarıda kalırsa buradan devam

SENTIMENT_MODEL_DIR = "./models/turkish_sentiment"
SUMMARY_MODEL_DIR   = "./models/turkish_summary"

# Cihaz seç
if torch.backends.mps.is_available():
    DEVICE = "mps"; PIPE_DEVICE = 0
elif torch.cuda.is_available():
    DEVICE = "cuda"; PIPE_DEVICE = 0
else:
    DEVICE = "cpu"; PIPE_DEVICE = -1

print(f"Kullanılan cihaz: {DEVICE}")

# ─────────────────────────────────────────
# TÜR HARİTASI
# ─────────────────────────────────────────
SINGER_GENRE_MAP = {
    # Sanat müziği
    "Zeki Müren":       "sanat müziği",
    "Müzeyyen Senar":   "sanat müziği",
    "Emel Sayın":       "sanat müziği",
    "Bülent Ersoy":     "sanat müziği",
    "Muazzez Ersoy":    "sanat müziği",
    "Muazzez Abacı":    "sanat müziği",
    # Arabesk
    "Müslüm Gürses":    "arabesk",
    "Orhan Gencebay":   "arabesk",
    "İbrahim Tatlıses": "arabesk",
    "Ferdi Tayfur":     "arabesk",
    "Azer Bülbül":      "arabesk",
    "Bergen":           "arabesk",
    "Murat Göğebakan":  "arabesk",
    "Cengiz Kurtoğlu":  "arabesk",
    "Sibel Can":        "arabesk",
    "Ebru Gündeş":      "arabesk",
    "Yıldız Tilbe":     "arabesk",
    "Hakan Altun":      "arabesk",
    "Sinan Özen":       "arabesk",
    "Kibariye":         "arabesk",
    "Güllü":            "arabesk",
    "Esmeray":          "arabesk",
    "Özdemir Erdoğan":  "arabesk",
    "Kamuran Akkor":    "arabesk",
    "Gülden Karaböcek": "arabesk",
    "Ümit Besen":       "arabesk",
    "Adnan Şenses":     "arabesk",
    "İbrahim Erkal":    "arabesk",
    "Kubat":            "arabesk",
    "Özgün":            "arabesk",
    "Mustafa Ceceli":   "arabesk",
    "Semicenk":         "arabesk",
    "Bilal Sonses":     "arabesk",
    "Serkan Kaya":      "arabesk",
    # Halk müziği
    "Neşet Ertaş":      "halk müziği",
    "Yeni Türkü":       "halk müziği",
    "Zülfü Livaneli":   "halk müziği",
    "Cengiz Özkan":     "halk müziği",
    "Volkan Konak":     "halk müziği",
    "Muharrem Aslan":   "halk müziği",
    "Grup Yorum":       "halk müziği",
    "Grup Laçin":       "halk müziği",
    "Edip Akbayram":    "halk müziği",
    "Ankaralı Namık":   "halk müziği",
    # Halk rock
    "Barış Manço":              "halk rock",
    "Ahmet Kaya":               "halk rock",
    "Cem Karaca":               "halk rock",
    "MFÖ":                      "halk rock",
    "Mazhar Fuat Özkan (MFÖ)":  "halk rock",
    "Erkin Koray":              "halk rock",
    "Haluk Levent":             "halk rock",
    # Rock
    "Duman":              "rock",
    "Mor Ve Ötesi":       "rock",
    "mor ve ötesi":       "rock",
    "Yüksek Sadakat":     "rock",
    "Şebnem Ferah":       "rock",
    "Murat Kekilli":      "rock",
    "Gripin":             "rock",
    "Redd":               "rock",
    "Büyük Ev Ablukada":  "rock",
    "Adamlar":            "rock",
    # Pop
    "Sezen Aksu":           "pop",
    "Serdar Ortaç":         "pop",
    "Sertab Erener":        "pop",
    "Tarkan":               "pop",
    "Hadise":               "pop",
    "Mustafa Sandal":       "pop",
    "Ajda Pekkan":          "pop",
    "Candan Erçetin":       "pop",
    "Kayahan":              "pop",
    "Nazan Öncel":          "pop",
    "Teoman":               "pop",
    "Mabel Matiz":          "pop",
    "Can Bonomo":           "pop",
    "Cem Adrian":           "pop",
    "Pinhani":              "pop",
    "Feridun Düzağaç":      "pop",
    "Yaşar":                "pop",
    "Göksel":               "pop",
    "Sıla":                 "pop",
    "Murat Boz":            "pop",
    "Kenan Doğulu":         "pop",
    "Gülşen":               "pop",
    "Hande Yener":          "pop",
    "Demet Akalın":         "pop",
    "Aleyna Tilki":         "pop",
    "Oğuzhan Koç":          "pop",
    "Atiye":                "pop",
    "Tan Taşçı":            "pop",
    "Halil Sezai":          "pop",
    "Funda Arar":           "pop",
    "Bengü":                "pop",
    "Gökhan Türkmen":       "pop",
    "Yalın":                "pop",
    "Fettah Can":           "pop",
    "Burak Kut":            "pop",
    "Hakan Peker":          "pop",
    "Ezhel":                "pop",
    "Zara":                 "pop",
    "Simge":                "pop",
    "Zeynep Dizdar":        "pop",
    "Yonca Evcimik":        "pop",
    "Nil Karaibrahimgil":   "pop",
    "Dolu Kadehi Ters Tut": "pop",
    "Gökhan Özen":          "pop",
    "Murat Dalkılıç":       "pop",
    "Buray":                "pop",
    "EDIS":                 "pop",
    "Ece Seçkin":           "pop",
    "Aydilge":              "pop",
    "Ozan Doğulu":          "pop",
    "Emre Altuğ":           "pop",
    # Rap / Hip-hop
    "Sagopa Kajmer":    "rap",
    "Ceza":             "rap",
    "Norm Ender":       "rap",
    "Şanışer":          "rap",
    "Patron":           "rap",
    "UZI":              "rap",
    "Lvbel C5":         "rap",
    "Gazapizm":         "rap",
    "Heijan":           "rap",
    "Ben Fero":         "rap",
    "Sefo":             "rap",
    "Khontkar":         "rap",
    "Şehinşah":         "rap",
    "Allame":           "rap",
    "Hidra":            "rap",
    "Canbay & Wolker":  "rap",
    "Tankurt Manas":    "rap",
    "Sansar Salvo":     "rap",
    "Cash Flow":        "rap",
    "Rota":             "rap",
    "Joker":            "rap",
    "Contra":           "rap",
    "Anıl Piyancı":     "rap",
    "Mode XL":          "rap",
    "Batuflex":         "rap",
    "cakal":            "rap",
    "Revart":           "rap",
    "Murda":            "rap",
    "Ati242":           "rap",
    "Ceg":              "rap",
}

# ─────────────────────────────────────────
# DUYGU HARİTALAMA  ← DÜZELTME BURADA
# ─────────────────────────────────────────
# savasy/bert-base-turkish-sentiment-cased modeli
# "positive" / "negative" string döndürüyor (LABEL_0/1 değil!)
# Eski kodda bu karışıktı → "Seni seviyorum" yanlış çıkıyordu.

def skor_ile_duygu(label: str, score: float) -> str:
    """
    label: model çıktısı — "positive" veya "negative"
           (bazı sürümlerde "LABEL_1" / "LABEL_0" da gelebilir, ikisi de handle edildi)
    score: 0.0 – 1.0 arası güven skoru
    """
    pozitif = label.lower() in ("positive", "label_1")

    if pozitif:
        if score > 0.90:   return "neşe/mutluluk 🎉"
        elif score > 0.70: return "umut/coşku 🌟"
        else:              return "sakin/nötr 😌"
    else:                                              # negative / label_0
        if score > 0.90:   return "derin hüzün/acı 💔"
        elif score > 0.75: return "özlem/melankoli 😢"
        elif score > 0.60: return "öfke/isyan 😡"
        else:              return "karamsarlık/umutsuzluk 😞"


# ─────────────────────────────────────────
# YARDIMCI FONKSİYONLAR
# ─────────────────────────────────────────

def tur_tahmin(singer: str) -> str:
    s = str(singer).lower()
    rap_ipuclari = ["uzi", "flow", "maho", "vio", "bege", "xir", "muti",
                    "reckol", "zen", "swag", "kayra", "aspova"]
    if any(k in s for k in rap_ipuclari):
        return "rap"
    return "pop"


def modelleri_kontrol_et(sadece_duygu: bool) -> bool:
    if not os.path.exists(SENTIMENT_MODEL_DIR):
        print("❌ Duygu modeli bulunamadı!")
        print("   Önce şunu çalıştır: python 2_model_indir_kaydet.py")
        return False
    if not sadece_duygu and not os.path.exists(SUMMARY_MODEL_DIR):
        print("❌ Özetleme modeli bulunamadı!")
        print("   Önce şunu çalıştır: python 2_model_indir_kaydet.py")
        return False
    return True


def veri_yukle() -> pd.DataFrame:
    print("\n📂 Veri yükleniyor...")
    df = pd.read_csv(
        DATA_PATH, sep=";", encoding="utf-8",
        on_bad_lines="skip", skiprows=1
    )
    df.columns = ["singer", "lyrics"]
    df = df.dropna(subset=["lyrics"])
    df = df[df["lyrics"].str.strip() != ""]
    df["lyrics"] = (
        df["lyrics"]
        .str.replace("\\n", " ", regex=False)
        .str.replace("\n",  " ", regex=False)
    )
    df["word_count"] = df["lyrics"].apply(lambda x: len(str(x).split()))
    df = df[df["word_count"] >= 10].reset_index(drop=True)
    df["lyrics_short"] = df["lyrics"].apply(
        lambda x: " ".join(str(x).split()[:400])
    )
    # Tür etiketleme
    df["genre"] = df["singer"].map(SINGER_GENRE_MAP)
    df["genre"] = df.apply(
        lambda row: row["genre"] if pd.notna(row["genre"])
        else tur_tahmin(row["singer"]),
        axis=1
    )
    print(f"✅ {len(df)} şarkı yüklendi")
    print("\nTür dağılımı:")
    print(df["genre"].value_counts().to_string())
    return df


def sentiment_yukle():
    print("\n🤖 Duygu modeli yükleniyor...")
    from transformers import AutoModelForSequenceClassification
    tok = AutoTokenizer.from_pretrained(SENTIMENT_MODEL_DIR)
    mod = AutoModelForSequenceClassification.from_pretrained(SENTIMENT_MODEL_DIR)
    pipe = pipeline(
        "sentiment-analysis",
        model=mod, tokenizer=tok,
        device=PIPE_DEVICE,
        truncation=True, max_length=512
    )
    print("✅ Duygu modeli hazır")
    return pipe


def summary_yukle():
    print("\n🤖 Özetleme modeli yükleniyor...")
    tok = AutoTokenizer.from_pretrained(SUMMARY_MODEL_DIR)
    mod = AutoModelForSeq2SeqLM.from_pretrained(SUMMARY_MODEL_DIR)
    print("✅ Özetleme modeli hazır")
    return tok, mod


def duygu_batch(pipe, lyrics_list: list, batch_size: int = 16) -> list:
    """
    Tüm şarkıları batch olarak işler — tek tek döngüden çok daha hızlı.
    Dönüş: [(duygu_str, skor_float), ...] listesi
    """
    sonuclar = []
    for i in tqdm(range(0, len(lyrics_list), batch_size),
                  desc="Duygu analizi", unit="batch"):
        batch = [str(x)[:512] for x in lyrics_list[i:i+batch_size]]
        try:
            tahminler = pipe(batch)
            for r in tahminler:
                duygu = skor_ile_duygu(r["label"], r["score"])
                sonuclar.append((duygu, round(r["score"], 3)))
        except Exception as e:
            # Batch hata verirse her birini tek tek dene
            for metin in batch:
                try:
                    r = pipe(metin)[0]
                    sonuclar.append((skor_ile_duygu(r["label"], r["score"]),
                                     round(r["score"], 3)))
                except:
                    sonuclar.append(("bilinmiyor", 0.0))
    return sonuclar


def ozet_uret(tok, mod, lyrics: str) -> str:
    try:
        metin = lyrics[:600]
        if len(metin.split()) < 20:
            return "Şarkı sözü özet için çok kısa."
        inputs = tok(metin, return_tensors="pt", truncation=True, max_length=512)
        cikti = mod.generate(
            **inputs,
            max_length=60,          # kısalttık — daha net özetler
            min_length=10,
            num_beams=4,
            length_penalty=1.5,
            repetition_penalty=3.5, # tekrar sorununu gidermek için artırıldı
            no_repeat_ngram_size=3, # aynı 3-gram'ı tekrar üretme  ← yeni
            early_stopping=True
        )
        return tok.decode(cikti[0], skip_special_tokens=True)
    except Exception as e:
        return f"Hata: {str(e)[:60]}"


# ─────────────────────────────────────────
# CHECKPOINT — kaldığı yerden devam
# ─────────────────────────────────────────

def checkpoint_yukle() -> set:
    """Daha önce işlenen index'leri döndürür."""
    if os.path.exists(CHECKPOINT_PATH):
        try:
            ck = pd.read_csv(CHECKPOINT_PATH, encoding="utf-8-sig")
            print(f"♻️  Checkpoint bulundu: {len(ck)} şarkı daha önce işlenmiş, "
                  "kaldığı yerden devam ediliyor...")
            return ck
        except:
            pass
    return None


def checkpoint_kaydet(df_islenmis: pd.DataFrame):
    """Her 50 şarkıda bir ara kayıt yapar."""
    df_islenmis.to_csv(CHECKPOINT_PATH, index=False, encoding="utf-8-sig")


# ─────────────────────────────────────────
# ANA ANALİZ
# ─────────────────────────────────────────

def tam_analiz(sadece_duygu: bool = False, batch_size: int = 16):
    if not modelleri_kontrol_et(sadece_duygu):
        return

    df = veri_yukle()

    # ── Checkpoint kontrolü ──
    ck_df = checkpoint_yukle()
    if ck_df is not None:
        # Zaten işlenenler hariç kalanları bul
        islenmis_idx = set(ck_df.index.tolist()) if "orig_idx" not in ck_df.columns \
                       else set(ck_df["orig_idx"].tolist())
        df["orig_idx"] = df.index
        kalan_df = df[~df["orig_idx"].isin(islenmis_idx)].copy()

        # Checkpoint'te özet yoksa ve özet isteniyorsa, özetlenecekleri de bul
        if not sadece_duygu and "summary_tr" not in ck_df.columns:
            ozet_bekleyen = ck_df.copy()
            ozet_bekleyen["summary_tr"] = "—"
        else:
            ozet_bekleyen = ck_df.copy()
    else:
        df["orig_idx"] = df.index
        kalan_df = df.copy()
        ozet_bekleyen = None

    print(f"\n📊 Toplam şarkı       : {len(df)}")
    print(f"   İşlenecek şarkı   : {len(kalan_df)}")
    if ck_df is not None:
        print(f"   Zaten işlenmiş    : {len(ck_df)}")

    if sadece_duygu:
        tahmini_sure = len(kalan_df) / 23 / 60
        print(f"\n⏱  Tahmini süre (duygu): ~{tahmini_sure:.0f} dakika")
    else:
        tahmini_sure = len(kalan_df) * 1.7 / 60
        print(f"\n⏱  Tahmini süre (özet dahil): ~{tahmini_sure:.0f} dakika "
              f"(~{tahmini_sure/60:.1f} saat)")
        print("   💡 İpucu: Sadece duygu için: python 3_veri_analiz.py --sadece-duygu")

    if len(kalan_df) == 0:
        print("\n✅ Tüm şarkılar zaten işlenmiş! Sonuçlar mevcut.")
        if os.path.exists(CHECKPOINT_PATH):
            import shutil
            shutil.copy(CHECKPOINT_PATH, OUTPUT_PATH)
            print(f"💾 {OUTPUT_PATH} güncellendi.")
        return

    # ── Duygu Analizi (batch) ──
    sentiment_pipe = sentiment_yukle()
    print(f"\n🔍 Duygu analizi başlıyor ({len(kalan_df)} şarkı, batch={batch_size})...")

    sonuclar = duygu_batch(sentiment_pipe, kalan_df["lyrics_short"].tolist(), batch_size)
    kalan_df = kalan_df.copy()
    kalan_df["predicted_emotion"]   = [s[0] for s in sonuclar]
    kalan_df["emotion_confidence"]  = [s[1] for s in sonuclar]
    print("✅ Duygu analizi tamamlandı")

    # ── Özetleme ──
    if not sadece_duygu:
        sum_tok, sum_mod = summary_yukle()
        print(f"\n📝 Özetleme başlıyor ({len(kalan_df)} şarkı)...")
        print("   Her 50 şarkıda bir otomatik ara kayıt yapılıyor.")

        ozetler = []
        for i, (_, row) in enumerate(tqdm(kalan_df.iterrows(),
                                          total=len(kalan_df),
                                          desc="Özetleme")):
            ozet = ozet_uret(sum_tok, sum_mod, row["lyrics_short"])
            ozetler.append(ozet)

            # Her 50 şarkıda checkpoint
            if (i + 1) % 50 == 0:
                gecici = kalan_df.iloc[:i+1].copy()
                gecici["summary_tr"] = ozetler
                if ozet_bekleyen is not None:
                    tumü = pd.concat([ozet_bekleyen, gecici], ignore_index=True)
                else:
                    tumü = gecici
                checkpoint_kaydet(tumü)
                print(f"   💾 Ara kayıt: {i+1}/{len(kalan_df)}")

        kalan_df["summary_tr"] = ozetler
        print("✅ Özetleme tamamlandı")
    else:
        kalan_df["summary_tr"] = "—"
        print("\nℹ️  Özetleme atlandı (--sadece-duygu modu)")

    # ── Tüm sonuçları birleştir ──
    if ozet_bekleyen is not None:
        df_final = pd.concat([ozet_bekleyen, kalan_df], ignore_index=True)
    else:
        df_final = kalan_df.copy()

    # ── Kaydet ──
    df_final.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")
    print(f"\n💾 Sonuçlar kaydedildi: {OUTPUT_PATH}")
    print(f"   Toplam satır: {len(df_final)}")

    # Checkpoint temizle (işlem bitti)
    if os.path.exists(CHECKPOINT_PATH):
        os.remove(CHECKPOINT_PATH)
        print("🗑  Checkpoint dosyası temizlendi.")

    # ── İstatistikler ──
    print("\n" + "=" * 55)
    print("TÜR × DUYGU TABLOSU")
    print("=" * 55)
    print(pd.crosstab(df_final["genre"],
                      df_final["predicted_emotion"]).to_string())

    print("\n" + "=" * 55)
    print("ÖRNEK SONUÇLAR (her türden 1 şarkı)")
    print("=" * 55)
    for tur in df_final["genre"].unique():
        row = df_final[df_final["genre"] == tur].iloc[0]
        print(f"\n🎵 {row['singer']}  [{tur}]")
        print(f"   Duygu : {row['predicted_emotion']}  (skor: {row['emotion_confidence']})")
        if not sadece_duygu:
            print(f"   Özet  : {row['summary_tr']}")

    print("\n" + "─" * 55)
    print("Sıradaki adım:")
    print("  python 4_sarki_test.py")
    print("─" * 55)


# ─────────────────────────────────────────
# GİRİŞ NOKTASI
# ─────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sadece-duygu",
        action="store_true",
        help="Özetlemeyi atla, sadece duygu analizi yap (~8 dakika)"
    )
    parser.add_argument(
        "--batch-size",
        type=int, default=16,
        help="Duygu analizi batch boyutu (varsayılan: 16, MPS'de 32 dene)"
    )
    args = parser.parse_args()
    tam_analiz(sadece_duygu=args.sadece_duygu, batch_size=args.batch_size)