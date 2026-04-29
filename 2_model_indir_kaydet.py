# ============================================================
# ADIM 2 — MODELLERİ İNDİR VE LOCALE KAYDET
#
# Bu dosyayı sadece 1 kez çalıştır.
# Modeller ./models/ klasörüne kaydedilir.
# Sonra internet olmadan da çalışır.
#
# İndirilecek modeller:
#   - savasy/bert-base-turkish-sentiment-cased   (~450 MB)
#     → Türkçe duygu analizi (pozitif/negatif)
#   - mukayese/mt5-base-turkish-summarization    (~580 MB)
#     → Türkçe özetleme
#
# Toplam disk: ~1 GB
#
# Çalıştırma:
#   python 2_model_indir_kaydet.py
# ============================================================

import os
from transformers import (
    AutoTokenizer, 
    AutoModelForSequenceClassification,
    AutoModelForSeq2SeqLM,
)
#AutoTokenizer metni sayıya çevirir (modelin anlayacağı dile)
#AutoModelForSequenceClassification → duygu analizi yapar
#AutoModelForSeq2SeqLM → özet çıkarır
# ─────────────────────────────────────────
# Kaydedilecek klasörler
# ─────────────────────────────────────────
SENTIMENT_KAYIT_DIR = "./models/turkish_sentiment"
SUMMARY_KAYIT_DIR   = "./models/turkish_summary"

# HuggingFace'teki model isimleri
SENTIMENT_HF = "savasy/bert-base-turkish-sentiment-cased"
SUMMARY_HF   = "mukayese/mt5-base-turkish-summarization"


def indir_ve_kaydet_sentiment():
    print("\n" + "=" * 55)
    print("1/2 — DUYGU MODELİ")
    print("=" * 55)

    if os.path.exists(SENTIMENT_KAYIT_DIR):
        # Klasör var mı kontrol et — ama içi boş olabilir
        dosyalar = os.listdir(SENTIMENT_KAYIT_DIR)
        if any(f.endswith(".json") for f in dosyalar):
            print(f"✅ Zaten indirilmiş: {SENTIMENT_KAYIT_DIR}")
            print("   Atlanıyor... (tekrar indirmek için klasörü sil)")
            return
    
    print(f"⬇️  İndiriliyor: {SENTIMENT_HF}")
    print("   Bu işlem internet hızına göre 2-5 dakika sürebilir...")
    print()

    tokenizer = AutoTokenizer.from_pretrained(SENTIMENT_HF)
    model = AutoModelForSequenceClassification.from_pretrained(SENTIMENT_HF)

    os.makedirs(SENTIMENT_KAYIT_DIR, exist_ok=True)
    tokenizer.save_pretrained(SENTIMENT_KAYIT_DIR)
    model.save_pretrained(SENTIMENT_KAYIT_DIR)

    print(f"✅ Duygu modeli kaydedildi: {SENTIMENT_KAYIT_DIR}")


def indir_ve_kaydet_summary():
    print("\n" + "=" * 55)
    print("2/2 — ÖZETLEME MODELİ")
    print("=" * 55)

    if os.path.exists(SUMMARY_KAYIT_DIR):
        dosyalar = os.listdir(SUMMARY_KAYIT_DIR)
        if any(f.endswith(".json") for f in dosyalar):
            print(f"✅ Zaten indirilmiş: {SUMMARY_KAYIT_DIR}")
            print("   Atlanıyor... (tekrar indirmek için klasörü sil)")
            return

    print(f"⬇️  İndiriliyor: {SUMMARY_HF}")
    print("   Bu işlem internet hızına göre 5-10 dakika sürebilir...")
    print()

    tokenizer = AutoTokenizer.from_pretrained(SUMMARY_HF)
    model = AutoModelForSeq2SeqLM.from_pretrained(SUMMARY_HF)

    os.makedirs(SUMMARY_KAYIT_DIR, exist_ok=True)
    tokenizer.save_pretrained(SUMMARY_KAYIT_DIR)
    model.save_pretrained(SUMMARY_KAYIT_DIR)

    print(f"✅ Özetleme modeli kaydedildi: {SUMMARY_KAYIT_DIR}")


def model_hizli_test():
    """
    İndirilen modellerin düzgün çalışıp çalışmadığını
    3 örnek cümleyle test eder.
    """
    print("\n" + "=" * 55)
    print("HIZLI TEST — modeller doğru çalışıyor mu?")
    print("=" * 55)

    import torch
    from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

    # Cihaz seç
    if torch.backends.mps.is_available():
        pipe_device = 0
    elif torch.cuda.is_available():
        pipe_device = 0
    else:
        pipe_device = -1

    # ── Duygu testi ──
    print("\n[Duygu Analizi Testi]")
    from transformers import AutoModelForSequenceClassification
    s_tok = AutoTokenizer.from_pretrained(SENTIMENT_KAYIT_DIR)
    s_mod = AutoModelForSequenceClassification.from_pretrained(SENTIMENT_KAYIT_DIR)
    s_pipe = pipeline(
        "sentiment-analysis",
        model=s_mod, tokenizer=s_tok,
        device=pipe_device, truncation=True, max_length=512
    )

    test_cumleleri = [
        "Seni seviyorum, çok mutluyum bugün",          # pozitif beklenir
        "Her şeyi kaybettim, içim yanıyor",             # negatif beklenir
        "Yollar uzun, gözlerim dolu, ayrılık acı",     # negatif beklenir
    ]

    # Skor → 6 duygu haritalama (adım 3 ve 4 ile aynı mantık)
    def skor_ile_duygu(label, score):
        if label == "LABEL_1":
            if score > 0.90: return "neşe/mutluluk 🎉"
            elif score > 0.70: return "umut/coşku 🌟"
            else: return "sakin/nötr 😌"
        else:
            if score > 0.90: return "derin hüzün/acı 💔"
            elif score > 0.75: return "özlem/melankoli 😢"
            elif score > 0.60: return "öfke/isyan 😡"
            else: return "karamsarlık/umutsuzluk 😞"

    for cumle in test_cumleleri:
        r = s_pipe(cumle)[0]
        duygu = skor_ile_duygu(r["label"], r["score"])
        print(f"  Girdi : {cumle}")
        print(f"  Çıktı : {duygu}  (ham: {r['label']}, skor: {r['score']:.3f})")
        print()

    # ── Özetleme testi ──
    print("[Özetleme Testi]")
    o_tok = AutoTokenizer.from_pretrained(SUMMARY_KAYIT_DIR)
    o_mod = AutoModelForSeq2SeqLM.from_pretrained(SUMMARY_KAYIT_DIR)

    test_sarki = (
        "Bir mavi otobüs gelirdi seni alır giderdi "
        "kaldırımlar kaldırımlar varya seni alır giderdi "
        "o mavi otobüs varya uzaklara giderdi "
        "bu şehrin yolları seni götürür benden uzaklara "
        "ne zaman dönersin bilmiyorum ama beklerim seni "
        "kapının önünde her sabah umutla bakarım "
    )
    inputs = o_tok(test_sarki, return_tensors="pt", truncation=True, max_length=512)
    output = o_mod.generate(
        **inputs, max_length=80, min_length=15,
        num_beams=4, length_penalty=2.0,
        repetition_penalty=2.5, early_stopping=True
    )
    ozet = o_tok.decode(output[0], skip_special_tokens=True)
    print(f"  Girdi : {test_sarki[:80]}...")
    print(f"  Özet  : {ozet}")

    print()
    print("=" * 55)
    print("✅ Her iki model de çalışıyor!")
    print()
    print("Sıradaki adım:")
    print("  python 3_veri_analiz.py")
    print("=" * 55)


# ─────────────────────────────────────────
# ANA AKIŞ
# ─────────────────────────────────────────
if __name__ == "__main__":
    indir_ve_kaydet_sentiment()
    indir_ve_kaydet_summary()
    model_hizli_test()