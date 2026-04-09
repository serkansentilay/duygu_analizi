# ============================================================
# ADIM 4 — SARKI SOZU TEST / DEMO
#
# Kullanım:
#   python 4_sarki_test.py                        # interaktif
#   python 4_sarki_test.py --sarki "sözler..."    # direkt
#   python 4_sarki_test.py --dosya sarki.txt      # dosyadan
# ============================================================

import argparse
import os
import sys
import torch
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    AutoModelForSeq2SeqLM,
    pipeline,
)

# ─────────────────────────────────────────
# AYARLAR
# ─────────────────────────────────────────
SENTIMENT_MODEL_DIR = "./models/turkish_sentiment"
SUMMARY_MODEL_DIR   = "./models/turkish_summary"

if torch.backends.mps.is_available():
    PIPE_DEVICE = 0
elif torch.cuda.is_available():
    PIPE_DEVICE = 0
else:
    PIPE_DEVICE = -1

# ─────────────────────────────────────────
# GÜVEN SKORU GÖSTERGESİ
# ─────────────────────────────────────────
# Örnek çıktı:
#   %91  ████████████████████░░░░  Çok güvenilir
#   %63  █████████████░░░░░░░░░░░  Orta güven
#   %41  ████████░░░░░░░░░░░░░░░░  Düşük güven

def guven_goster(skor: float) -> str:
    yuzde = int(skor * 100)
    dolu  = int(skor * 24)
    bos   = 24 - dolu
    bar   = "█" * dolu + "░" * bos

    if skor >= 0.90:
        renk   = "\033[92m"   # yeşil
        etiket = "Çok güvenilir"
    elif skor >= 0.75:
        renk   = "\033[93m"   # sarı
        etiket = "Güvenilir"
    elif skor >= 0.60:
        renk   = "\033[33m"   # turuncu
        etiket = "Orta güven"
    else:
        renk   = "\033[91m"   # kırmızı
        etiket = "Düşük güven — dikkatli yorumla"

    RESET = "\033[0m"
    return f"  {renk}%{yuzde:3d}  {bar}  {etiket}{RESET}"


# ─────────────────────────────────────────
# TÜR TAHMİN — anahtar kelime tabanlı
# ─────────────────────────────────────────
TUR_ANAHTAR_KELIMELER = {
    "arabesk":      ["gurbet", "hasret", "ağlama", "yandım", "yanıyor", "kaderim",
                     "yazık", "vah", "yalnız", "gözlerim dolu", "kara baht",
                     "feryat", "dert", "derman", "çaresiz", "ağlar", "yanar"],
    "halk müziği":  ["dağlar", "yaylalar", "türkü", "anadolu", "köy", "bağ",
                     "bahçe", "dere", "kaynak", "gelin", "düğün", "efe", "yaren"],
    "halk rock":    ["toprak", "isyan", "direniş", "özgürlük", "kavga", "devrim",
                     "emek", "işçi", "yoksul", "halk", "meydan", "zindan"],
    "rock":         ["çığlık", "karanlık", "fırtına", "sert", "duman", "yıkıl",
                     "gece yarısı", "patla", "bağır", "metal", "elektro"],
    "rap":          ["flow", "beat", "kafiye", "sokak", "para", "güç", "sahne",
                     "mikrofon", "rime", "trap", "drill", "bars", "hook"],
    "sanat müziği": ["ney", "ud", "makam", "mey", "saz", "beste", "şiir",
                     "gazel", "divan", "klasik", "fasıl", "hicaz"],
}

def tur_tahmin_kelime(sarki_sozu: str) -> tuple:
    """
    Dönüş: (tur_str, guven_float)
    Güven hesabı: eşleşen kelimelerin baskınlık oranından türetilir.
    """
    metin  = sarki_sozu.lower()
    skorlar = {
        tur: sum(1 for k in kelimeler if k in metin)
        for tur, kelimeler in TUR_ANAHTAR_KELIMELER.items()
    }
    toplam = sum(skorlar.values())
    en_tur = max(skorlar, key=skorlar.get)

    if toplam == 0:
        return "pop (eşleşme yok, varsayılan)", 0.40

    guven = min(0.40 + (skorlar[en_tur] / toplam) * 0.55, 0.95)
    return en_tur, round(guven, 3)


# ─────────────────────────────────────────
# DUYGU HARİTALAMA
# ─────────────────────────────────────────

def skor_ile_duygu(label: str, score: float) -> str:
    pozitif = label.lower() in ("positive", "label_1")
    if pozitif:
        if score > 0.90:   return "neşe/mutluluk 🎉"
        elif score > 0.70: return "umut/coşku 🌟"
        else:              return "sakin/nötr 😌"
    else:
        if score > 0.90:   return "derin hüzün/acı 💔"
        elif score > 0.75: return "özlem/melankoli 😢"
        elif score > 0.60: return "öfke/isyan 😡"
        else:              return "karamsarlık/umutsuzluk 😞"


# ─────────────────────────────────────────
# MODELLERİ YÜKLE
# ─────────────────────────────────────────

def modelleri_yukle():
    if not os.path.exists(SENTIMENT_MODEL_DIR):
        print("❌ Modeller bulunamadı. Önce şunu çalıştır:")
        print("   python 2_model_indir_kaydet.py")
        sys.exit(1)

    print("🤖 Modeller yükleniyor...")

    s_tok  = AutoTokenizer.from_pretrained(SENTIMENT_MODEL_DIR)
    s_mod  = AutoModelForSequenceClassification.from_pretrained(SENTIMENT_MODEL_DIR)
    s_pipe = pipeline(
        "sentiment-analysis",
        model=s_mod, tokenizer=s_tok,
        device=PIPE_DEVICE, truncation=True, max_length=512
    )

    o_tok, o_mod = None, None
    if os.path.exists(SUMMARY_MODEL_DIR):
        o_tok = AutoTokenizer.from_pretrained(SUMMARY_MODEL_DIR)
        o_mod = AutoModelForSeq2SeqLM.from_pretrained(SUMMARY_MODEL_DIR)

    print("✅ Modeller hazır\n")
    return s_pipe, o_tok, o_mod


# ─────────────────────────────────────────
# TAHMİN FONKSİYONU
# ─────────────────────────────────────────

def tahmin_et(sarki_sozu: str, s_pipe, o_tok, o_mod) -> dict:
    metin      = sarki_sozu.strip()
    metin_kisa = " ".join(metin.split()[:400])

    # 1. Tür
    tur, tur_guven = tur_tahmin_kelime(metin_kisa)

    # 2. Duygu
    r            = s_pipe(metin_kisa[:512])[0]
    duygu        = skor_ile_duygu(r["label"], r["score"])
    duygu_guven  = round(r["score"], 3)

    # 3. Özet
    ozet = "Özetleme modeli yüklü değil."
    if o_tok is not None and o_mod is not None:
        try:
            if len(metin_kisa.split()) >= 20:
                inputs = o_tok(
                    metin_kisa[:600],
                    return_tensors="pt", truncation=True, max_length=512
                )
                cikti = o_mod.generate(
                    **inputs,
                    max_length=60, min_length=10,
                    num_beams=4, length_penalty=1.5,
                    repetition_penalty=3.5,
                    no_repeat_ngram_size=3,
                    early_stopping=True
                )
                ozet = o_tok.decode(cikti[0], skip_special_tokens=True)
            else:
                ozet = "Şarkı sözü özet için çok kısa."
        except Exception as e:
            ozet = f"Hata: {str(e)[:60]}"

    return {
        "tur":         tur,
        "tur_guven":   tur_guven,
        "duygu":       duygu,
        "duygu_guven": duygu_guven,
        "ozet":        ozet,
    }


# ─────────────────────────────────────────
# ÇIKTI YAZDIR
# ─────────────────────────────────────────

def sonuc_yazdir(sarki_sozu: str, sonuc: dict, sanatci: str = None):
    BOLD  = "\033[1m"
    RESET = "\033[0m"
    on_izleme = sarki_sozu[:45] + ("..." if len(sarki_sozu) > 45 else "")

    print()
    print(f"{BOLD}{'─'*55}{RESET}")
    if sanatci:
        print(f"  🎤 Sanatçı  : {sanatci}")
    print(f"  📝 Şarkı    : {on_izleme}")
    print(f"{'─'*55}")

    # Tür
    print(f"  🎵 Tür      : {BOLD}{sonuc['tur']}{RESET}")
    print(guven_goster(sonuc["tur_guven"]))

    print()

    # Duygu
    print(f"  💬 Duygu    : {BOLD}{sonuc['duygu']}{RESET}")
    print(guven_goster(sonuc["duygu_guven"]))

    print()

    # Özet — uzunsa satır satır kır
    print(f"  📋 Özet     :")
    ozet = sonuc["ozet"]
    for i in range(0, len(ozet), 60):
        print(f"     {ozet[i:i+60]}")

    print(f"{'─'*55}")

    # Uyarılar
    if sonuc["duygu_guven"] < 0.65:
        print("  ⚠️  Duygu tahmini düşük güvenle yapıldı.")
        print("     Şarkı belirsiz ya da karma duygular içeriyor olabilir.")
    if sonuc["tur_guven"] < 0.50:
        print("  ⚠️  Tür tahmini belirsiz — sanatçı adı verirsen daha doğru olur.")
    print()


# ─────────────────────────────────────────
# İNTERAKTİF MOD
# ─────────────────────────────────────────

def interaktif_mod(s_pipe, o_tok, o_mod):
    print("=" * 55)
    print("🎵 TÜRKÇE ŞARKI ANALİZ ARACI")
    print("   Çıkmak için: sadece Enter'a bas")
    print("=" * 55)

    while True:
        print()
        sanatci = input("Sanatçı adı (boş bırakabilirsin): ").strip()
        print("Şarkı sözlerini gir — bitirmek için tek satırda '---' yaz:")

        satirlar = []
        while True:
            satir = input()
            if satir.strip() == "---":
                break
            if satir.strip() == "" and not satirlar:
                print("👋 Görüşürüz!")
                return
            satirlar.append(satir)

        if not satirlar:
            print("⚠️  Şarkı sözü girilmedi, tekrar dene.")
            continue

        sarki_sozu = "\n".join(satirlar)
        sonuc = tahmin_et(sarki_sozu, s_pipe, o_tok, o_mod)
        sonuc_yazdir(sarki_sozu, sonuc, sanatci=sanatci or None)


# ─────────────────────────────────────────
# GİRİŞ NOKTASI
# ─────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Türkçe şarkı sözü → tür + duygu (güven skoruyla) + özet"
    )
    parser.add_argument("--sarki",   type=str, default=None,
                        help="Doğrudan şarkı sözü (tırnak içinde)")
    parser.add_argument("--dosya",   type=str, default=None,
                        help="Şarkı sözlerinin olduğu .txt dosyası")
    parser.add_argument("--sanatci", type=str, default=None,
                        help="Sanatçı adı (isteğe bağlı)")
    args = parser.parse_args()

    s_pipe, o_tok, o_mod = modelleri_yukle()

    if args.sarki:
        sonuc = tahmin_et(args.sarki, s_pipe, o_tok, o_mod)
        sonuc_yazdir(args.sarki, sonuc, args.sanatci)
    elif args.dosya:
        if not os.path.exists(args.dosya):
            print(f"❌ Dosya bulunamadı: {args.dosya}")
            sys.exit(1)
        with open(args.dosya, "r", encoding="utf-8") as f:
            sarki_sozu = f.read()
        sonuc = tahmin_et(sarki_sozu, s_pipe, o_tok, o_mod)
        sonuc_yazdir(sarki_sozu, sonuc, args.sanatci)
    else:
        interaktif_mod(s_pipe, o_tok, o_mod)