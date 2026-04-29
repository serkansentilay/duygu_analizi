# ============================================================
# ADIM 1 — KURULUM VE ORTAM KONTROLÜ
#
# Önce gen.py'yi çalıştırarak lexicon CSV'sini oluştur:
#   python gen.py
#
# Sonra bu dosyayı çalıştır:
#   python 1_kurulum.py
#
# CSV formatı (ikisi de desteklenir):
#   Sadece lyrics:      lyrics
#   Sanatçı + lyrics:   singing;lyrics
# ============================================================

import sys
import os

print("=" * 60)
print("TÜRKÇE ŞARKI ANALİZİ — KURULUM KONTROLÜ")
print("=" * 60)
print(f"Python sürümü: {sys.version.split()[0]}")
print()

# ─────────────────────────────────────────
# PAKET KONTROLÜ
# ─────────────────────────────────────────
GEREKLI = {
    "pandas":     "pandas",
    "tqdm":       "tqdm",
}

print("Paket Kontrolü:")
eksik = []
for paket_adi, import_adi in GEREKLI.items():
    try:
        __import__(import_adi)
        print(f"  ✅ {paket_adi}")
    except ImportError:
        print(f"  ❌ {paket_adi}  ← EKSİK")
        eksik.append(paket_adi)

print()
if eksik:
    print("Eksik paketleri yüklemek için:")
    print(f"  pip install {' '.join(eksik)}")
    print()
    sys.exit(1)

# ─────────────────────────────────────────
# LEXICON KONTROLÜ
# ─────────────────────────────────────────
print("─" * 60)
print("Lexicon Kontrolü:")

LEXICON_YOLU = "./turkce_sarki_lexicon.csv"

if not os.path.exists(LEXICON_YOLU):
    print(f"  ❌ {LEXICON_YOLU} bulunamadı!")
    print("  → Önce şunu çalıştır: python gen.py")
    sys.exit(1)

import pandas as pd

lex = pd.read_csv(LEXICON_YOLU, encoding="utf-8-sig")
print(f"  ✅ Lexicon yüklendi: {len(lex)} kelime/ifade")
print(f"  Türler   : {sorted(lex['tur'].unique())}")
print(f"  Duygular : {sorted(lex['duygu'].unique())}")

# ─────────────────────────────────────────
# CSV DOSYASI KONTROLÜ
# ─────────────────────────────────────────
print()
print("─" * 60)
print("Veri Dosyası Kontrolü:")

CSV_YOLU = "./909090.csv"

if not os.path.exists(CSV_YOLU):
    print(f"  ❌ {CSV_YOLU} bulunamadı!")
    print()
    print("  Desteklenen CSV formatları:")
    print()
    print("  Format 1 — Sadece şarkı sözleri:")
    print("    lyrics")
    print("    sensiz geçen geceler...")
    print()
    print("  Format 2 — Sanatçı + şarkı sözleri:")
    print("    singing;lyrics")
    print("    Sezen Aksu;sensiz geçen geceler...")
    sys.exit(1)

# Ayırıcı ve sütun tespiti
with open(CSV_YOLU, encoding="utf-8") as f:
    ilk_satir = f.readline().strip()

ayirici = ";" if ";" in ilk_satir else ","
sutunlar = [s.strip().lower() for s in ilk_satir.split(ayirici)]

print(f"  ✅ {CSV_YOLU} bulundu")
print(f"  Ayırıcı  : '{ayirici}'")
print(f"  Sütunlar : {sutunlar}")

# Lyrics sütununu bul
lyrics_idx = None
for i, s in enumerate(sutunlar):
    if "lyric" in s or "sozu" in s or "söz" in s or "lyrics" in s:
        lyrics_idx = i
        break

if lyrics_idx is None:
    if len(sutunlar) == 1:
        lyrics_idx = 0
    elif len(sutunlar) == 2:
        # singing;lyrics → ikinci sütun
        lyrics_idx = 1
    else:
        lyrics_idx = len(sutunlar) - 1  # son sütun

print(f"  Lyrics sütunu indeksi: {lyrics_idx} ('{sutunlar[lyrics_idx]}')")

singing_idx = None
for i, s in enumerate(sutunlar):
    if "sing" in s or "sanat" in s or "artist" in s or "isim" in s:
        singing_idx = i
        break

if singing_idx is not None:
    print(f"  Sanatçı sütunu   : {singing_idx} ('{sutunlar[singing_idx]}') — analizde kullanılmayacak")

# Veri önizleme
df = pd.read_csv(
    CSV_YOLU, sep=ayirici, encoding="utf-8",
    on_bad_lines="skip", nrows=5, header=None, skiprows=1
)

if lyrics_idx < len(df.columns):
    ornek = df.iloc[:, lyrics_idx]
    print()
    print("  İlk 3 şarkı sözü önizleme:")
    for i, satir in enumerate(ornek.head(3)):
        onizleme = " ".join(str(satir).split()[:10])
        print(f"    [{i+1}] {onizleme}...")
else:
    print("  ⚠️  Lyrics sütunu okunamadı, CSV formatını kontrol et.")

# Toplam satır
df_tam = pd.read_csv(CSV_YOLU, sep=ayirici, encoding="utf-8",
                     on_bad_lines="skip", header=None, skiprows=1)
print()
print(f"  Toplam şarkı sayısı: {len(df_tam)}")

# ─────────────────────────────────────────
# SONUÇ
# ─────────────────────────────────────────
print()
print("─" * 60)
print("✅ Her şey hazır!")
print()
print("Sıradaki adım:")
print("  python 2_analiz.py                    # tüm CSV'yi analiz et")
print("  python 2_analiz.py --limit 100        # ilk 100 şarkıyı dene")
print("─" * 60)