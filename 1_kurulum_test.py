# ============================================================
# ADIM 1 — KURULUM VE ORTAM KONTROLÜ
# Bu dosyayı ilk önce çalıştır.
# Eksik kütüphane varsa sana söyler.
#
# Çalıştırma:
#   python 1_kurulum_test.py
# ============================================================

import sys
import subprocess

print("=" * 55)
print("Python sürümü:", sys.version)
print("=" * 55)

# paket_adi: import_adi  (ikisi farklı olabilir)
GEREKLI_PAKETLER = {
    "torch":        "torch",
    "transformers": "transformers",
    "pandas":       "pandas",
    "scikit-learn": "sklearn",
    "matplotlib":   "matplotlib",
    "seaborn":      "seaborn",
    "tqdm":         "tqdm",
    "sentencepiece":"sentencepiece",
    "protobuf":     "google.protobuf",   # pip adı ≠ import adı
}

eksik = []

for paket_adi, import_adi in GEREKLI_PAKETLER.items():
    try:
        __import__(import_adi)
        print(f"  ✅ {paket_adi}")
    except ImportError:
        print(f"  ❌ {paket_adi}  ← EKSİK")
        eksik.append(paket_adi)

print()

if eksik:
    print("Eksik paketler bulundu. Şu komutu terminalde çalıştır:")
    print()
    print(f"  pip install {' '.join(eksik)}")
    print()
else:
    print("✅ Tüm paketler yüklü!")
    print()

    # Cihaz kontrolü
    import torch
    print("─" * 40)
    print("Cihaz Kontrolü:")
    if torch.backends.mps.is_available():
        print("  ✅ Apple Silicon MPS mevcut → hızlı çalışır")
        cihaz = "mps"
    elif torch.cuda.is_available():
        print("  ✅ NVIDIA CUDA mevcut → hızlı çalışır")
        cihaz = "cuda"
    else:
        print("  ℹ️  CPU kullanılacak → biraz daha yavaş ama çalışır")
        cihaz = "cpu"

    print(f"  Seçilen cihaz: {cihaz}")
    print()

    # CSV dosyası kontrolü
    import os
    print("─" * 40)
    print("Dosya Kontrolü:")
    if os.path.exists("./909090.csv"):
        import pandas as pd
        df = pd.read_csv(
            "./909090.csv", sep=";", encoding="utf-8",
            on_bad_lines="skip", skiprows=1, nrows=5
        )
        print("  ✅ 909090.csv bulundu")
        print(f"  İlk 5 satır önizleme:")
        print(df.to_string())
    else:
        print("  ❌ 909090.csv bulunamadı!")
        print("  → Bu scripti 909090.csv ile aynı klasöre koy.")

    print()
    print("─" * 40)
    print("Her şey tamam! Sıradaki adım:")
    print("  python 2_model_indir_kaydet.py")
    print("─" * 40)