# ============================================================
# ADIM 3 — TEK ŞARKI TEST / DEMO
#
# Verilen şarkı sözlerini analiz eder, tür ve duygu için
# ağırlıklı olasılık dağılımını gösterir.
#
# Kullanım:
#   python 3_test.py                          # interaktif mod
#   python 3_test.py --sarki "sözler..."      # direkt
#   python 3_test.py --dosya sarki.txt        # dosyadan
#   python 3_test.py --aciklamali             # eşleşen kelimeleri göster
#   python 3_test.py --tum-dagilim            # tüm olasılık tablosunu göster
# ============================================================

import argparse
import os
import re
import sys
from collections import defaultdict

# ─────────────────────────────────────────
# LEXICON YÜKLE
# ─────────────────────────────────────────
LEXICON_YOLU = "./turkce_sarki_lexicon.csv"


def lexicon_yukle():
    if not os.path.exists(LEXICON_YOLU):
        print(f"❌ {LEXICON_YOLU} bulunamadı!")
        print("   Önce şunu çalıştır: python gen.py")
        sys.exit(1)

    import csv
    lookup: dict[str, list] = defaultdict(list)
    satir_sayisi = 0

    with open(LEXICON_YOLU, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            kelime = row["kelime"].strip().lower()
            lookup[kelime].append({
                "tur":     row["tur"],
                "duygu":   row["duygu"],
                "tema":    row["tema"],
                "agirlik": float(row["agirlik"]),
            })
            satir_sayisi += 1

    print(f"✅ Lexicon: {satir_sayisi} giriş yüklendi\n")
    return lookup


# ─────────────────────────────────────────
# ANALİZ
# ─────────────────────────────────────────

def metin_temizle(metin: str) -> list[str]:
    metin = metin.lower()
    metin = re.sub(r"[^\w\s]", " ", metin)
    return metin.split()


def sarki_analiz_et(lyrics: str, lookup: dict) -> dict:
    """
    Şarkı sözündeki kelimeleri lexiconda arar.
    Her eşleşme için ağırlık puanı biriktirir.
    Toplam puana bölerek olasılık hesaplar.
    """
    tokenlar    = metin_temizle(lyrics)
    metin_lower = lyrics.lower()

    tur_puan:   dict[str, float] = defaultdict(float)
    duygu_puan: dict[str, float] = defaultdict(float)
    tema_puan:  dict[str, float] = defaultdict(float)

    eslesen_kelimeler: list[dict] = []

    # 1. Tek kelime eşleşmeleri
    for token in tokenlar:
        if token in lookup:
            for kayit in lookup[token]:
                tur_puan[kayit["tur"]]     += kayit["agirlik"]
                duygu_puan[kayit["duygu"]] += kayit["agirlik"]
                tema_puan[kayit["tema"]]   += kayit["agirlik"]
                eslesen_kelimeler.append({
                    "kelime":  token,
                    "tur":     kayit["tur"],
                    "duygu":   kayit["duygu"],
                    "agirlik": kayit["agirlik"],
                })

    # 2. Çok kelimeli ifade eşleşmeleri
    for kelime, kayitlar in lookup.items():
        if " " in kelime and kelime in metin_lower:
            sayi = metin_lower.count(kelime)
            for kayit in kayitlar:
                bonus = kayit["agirlik"] * sayi * 1.5
                tur_puan[kayit["tur"]]     += bonus
                duygu_puan[kayit["duygu"]] += bonus
                tema_puan[kayit["tema"]]   += bonus
                eslesen_kelimeler.append({
                    "kelime":  f'"{kelime}" (çok kelime)',
                    "tur":     kayit["tur"],
                    "duygu":   kayit["duygu"],
                    "agirlik": round(bonus, 3),
                })

    toplam_tur   = sum(tur_puan.values())
    toplam_duygu = sum(duygu_puan.values())
    toplam_tema  = sum(tema_puan.values())

    if toplam_tur == 0:
        return {
            "tur": "pop", "tur_olasilik": 0.0,
            "duygu": "genel", "duygu_olasilik": 0.0,
            "tema": "genel",
            "eslesen_kelimeler": [],
            "tur_dagilim": {}, "duygu_dagilim": {},
        }

    tur_dagilim   = {k: v / toplam_tur   for k, v in tur_puan.items()}
    duygu_dagilim = {k: v / toplam_duygu for k, v in duygu_puan.items()}
    tema_dagilim  = {k: v / toplam_tema  for k, v in tema_puan.items()}

    en_tur   = max(tur_dagilim,   key=tur_dagilim.get)
    en_duygu = max(duygu_dagilim, key=duygu_dagilim.get)
    en_tema  = max(tema_dagilim,  key=tema_dagilim.get)

    return {
        "tur":            en_tur,
        "tur_olasilik":   tur_dagilim[en_tur],
        "duygu":          en_duygu,
        "duygu_olasilik": duygu_dagilim[en_duygu],
        "tema":           en_tema,
        "eslesen_kelimeler": eslesen_kelimeler,
        "tur_dagilim":    dict(sorted(tur_dagilim.items(),   key=lambda x: -x[1])),
        "duygu_dagilim":  dict(sorted(duygu_dagilim.items(), key=lambda x: -x[1])),
    }


# ─────────────────────────────────────────
# GÖRSEL ÇIKTI
# ─────────────────────────────────────────

BOLD  = "\033[1m"
RESET = "\033[0m"
YESIL = "\033[92m"
SARI  = "\033[93m"
TURUNCU = "\033[33m"
KIRMIZI = "\033[91m"
MAVI  = "\033[94m"


def olasilik_bar(oran: float, genislik: int = 30) -> str:
    dolu = int(oran * genislik)
    bos  = genislik - dolu
    if oran >= 0.60:
        renk = YESIL
    elif oran >= 0.40:
        renk = SARI
    elif oran >= 0.25:
        renk = TURUNCU
    else:
        renk = KIRMIZI
    return f"{renk}{'█' * dolu}{'░' * bos}{RESET} {oran*100:5.1f}%"


def dagilim_yazdir(baslik: str, dagilim: dict, en_deger: str, tum: bool = False):
    print(f"\n  {BOLD}{baslik}{RESET}")
    sirali = sorted(dagilim.items(), key=lambda x: -x[1])
    goster = sirali if tum else sirali[:4]

    for etiket, oran in goster:
        isaretci = " ◄" if etiket == en_deger else ""
        print(f"  {etiket:<14} {olasilik_bar(oran)}{BOLD}{isaretci}{RESET}")

    if not tum and len(sirali) > 4:
        print(f"  ... (tamamı için --tum-dagilim kullan)")


def sonuc_yazdir(lyrics: str, sonuc: dict, aciklamali: bool = False, tum_dagilim: bool = False):
    onizleme = " ".join(lyrics.split()[:10]) + "..."
    eslesen  = len(sonuc["eslesen_kelimeler"])
    toplam_k = len(lyrics.split())

    print()
    print(f"{BOLD}{'─'*60}{RESET}")
    print(f"  📝 Şarkı sözü : {onizleme}")
    print(f"  Toplam kelime : {toplam_k}  |  Eşleşen: {eslesen}")
    print(f"{'─'*60}")

    # Ana sonuç
    print(f"\n  {BOLD}🎵 TÜR   →  {sonuc['tur'].upper()}{RESET}")
    dagilim_yazdir("Tür Olasılık Dağılımı:", sonuc["tur_dagilim"], sonuc["tur"], tum_dagilim)

    print(f"\n  {BOLD}💬 DUYGU →  {sonuc['duygu'].upper()}{RESET}")
    dagilim_yazdir("Duygu Olasılık Dağılımı:", sonuc["duygu_dagilim"], sonuc["duygu"], tum_dagilim)

    print(f"\n  🏷  Tema     :  {sonuc['tema']}")

    # Uyarılar
    if eslesen == 0:
        print(f"\n  ⚠️  Lexiconda hiç eşleşme bulunamadı.")
        print(f"     Şarkı sözünde çok az Türkçe kelime olabilir,")
        print(f"     ya da lexicona eklenmemiş kelimeler kullanılmış.")
    elif sonuc["tur_olasilik"] < 0.40:
        print(f"\n  ⚠️  Tür tahmini belirsiz — birden fazla türe ait sinyal var.")
    if sonuc["duygu_olasilik"] < 0.30:
        print(f"  ⚠️  Duygu tahmini belirsiz — karma duygular tespit edildi.")

    # Açıklamalı mod: eşleşen kelimeler
    if aciklamali and sonuc["eslesen_kelimeler"]:
        print(f"\n  {MAVI}🔍 Eşleşen Kelimeler (ilk 15):{RESET}")
        for ek in sonuc["eslesen_kelimeler"][:15]:
            print(f"    {ek['kelime']:<28} tür={ek['tur']:<12} duygu={ek['duygu']:<14} ağırlık={ek['agirlik']:.2f}")
        if len(sonuc["eslesen_kelimeler"]) > 15:
            print(f"    ... ve {len(sonuc['eslesen_kelimeler'])-15} kelime daha")

    print(f"\n{'─'*60}")


# ─────────────────────────────────────────
# İNTERAKTİF MOD
# ─────────────────────────────────────────

def interaktif_mod(lookup: dict, aciklamali: bool, tum_dagilim: bool):
    print("=" * 60)
    print("🎵 TÜRKÇE ŞARKI ANALİZ ARACI")
    print("   Model gerektirmez — tamamen lexicon tabanlı")
    print("   Çıkmak için: boş satırda sadece Enter")
    print("=" * 60)

    while True:
        print()
        print("Şarkı sözlerini gir.")
        print("Bitirmek için tek satırda  ---  yaz:")
        print()

        satirlar = []
        while True:
            try:
                satir = input()
            except EOFError:
                print("\n👋 Görüşürüz!")
                return

            if satir.strip() == "---":
                break
            if satir.strip() == "" and not satirlar:
                print("👋 Görüşürüz!")
                return
            satirlar.append(satir)

        if not satirlar:
            print("⚠️  Şarkı sözü girilmedi.")
            continue

        lyrics = "\n".join(satirlar)
        sonuc  = sarki_analiz_et(lyrics, lookup)
        sonuc_yazdir(lyrics, sonuc, aciklamali=aciklamali, tum_dagilim=tum_dagilim)


# ─────────────────────────────────────────
# GİRİŞ NOKTASI
# ─────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Türkçe şarkı sözü → tür + duygu olasılık analizi (lexicon tabanlı)"
    )
    parser.add_argument("--sarki",      type=str, default=None,
                        help="Doğrudan şarkı sözü (tırnak içinde)")
    parser.add_argument("--dosya",      type=str, default=None,
                        help="Şarkı sözlerinin olduğu .txt dosyası")
    parser.add_argument("--aciklamali", action="store_true",
                        help="Eşleşen kelimeleri ve ağırlıklarını göster")
    parser.add_argument("--tum-dagilim", action="store_true",
                        help="Tüm tür ve duygu olasılıklarını göster")
    args = parser.parse_args()

    lookup = lexicon_yukle()

    if args.sarki:
        sonuc = sarki_analiz_et(args.sarki, lookup)
        sonuc_yazdir(args.sarki, sonuc,
                     aciklamali=args.aciklamali, tum_dagilim=args.tum_dagilim)

    elif args.dosya:
        if not os.path.exists(args.dosya):
            print(f"❌ Dosya bulunamadı: {args.dosya}")
            sys.exit(1)
        with open(args.dosya, "r", encoding="utf-8") as f:
            lyrics = f.read()
        sonuc = sarki_analiz_et(lyrics, lookup)
        sonuc_yazdir(lyrics, sonuc,
                     aciklamali=args.aciklamali, tum_dagilim=args.tum_dagilim)

    else:
        interaktif_mod(lookup, aciklamali=args.aciklamali, tum_dagilim=args.tum_dagilim)