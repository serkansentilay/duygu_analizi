# 🎭 Duygu Analizi

Bu proje, Türkçe metinler üzerinde duygu analizi gerçekleştiren bir makine öğrenmesi uygulamasıdır.
Test icin 1 tane sarki ile csv olusturunuz
Python dosyasi oldugu icin venv dosyasinizi baslatarak isleme baslayin 

# Oluştur
python -m venv venv

# Aktive et (Mac/Linux)
source venv/bin/activate

# Aktive et (Windows)
venv\Scripts\activate

# Deaktive et
deactivate


## 📦 Model Dosyaları

Model dosyaları boyutları nedeniyle Google Drive üzerinde barındırılmaktadır.

👉 [Model Dosyalarını İndir](https://drive.google.com/drive/folders/1Gu_lL2LFfH8lT83EABS40ZMru0Xrhmcr?usp=sharing)

`models/` klasörünü indirip proje dizinine çıkartın.

duygu_analizi/
├── models/          # Google Drive'dan indirilmeli


##  python 4_sarki_analiz.py --dosya ornekSarki1.csv
### 📝 Şarkı    : singer;lyrics
### Duman;"[Nakarat]
### Elleri havada,...
### ───────────────────────────────────────────────────────
###   🎵 Tür      : rock
###  % 95  ██████████████████████░░  Çok güvenilir
### 
###   💬 Duygu    : derin hüzün/acı 💔
###   % 97  ███████████████████████░  Çok güvenilir
### 
###   📋 Özet     :
###      Ünlü arabesk şarkıcı Duman;Bu aktroller daha iyi Kargaları y
###      ine kovamadık abi. Korkuluk çok enayi Kuşlar şeytani


## python 4_sarki_analiz.py --dosya ornek2.csv  
### 📝 Şarkı    : 
### singer;lyrics
### Tarkan;"[Bölüm]
### Takmış koluna ...
### ───────────────────────────────────────────────────────
###   🎵 Tür      : arabesk
###   % 62  ██████████████░░░░░░░░░░  Orta güven
### 
###   💬 Duygu    : derin hüzün/acı 💔
###   % 97  ███████████████████████░  Çok güvenilir
### 
###   📋 Özet     :
###      Tarkan'ın Tarkan türküsünden Tarkan;Seni gidi fındıkkıran Yı
###      lanı deliğinden çıkaran Kaderim, püsküllü belam Yakalarsam (
###      Muck, muck)


## python 4_sarki_analiz.py --dosya ornek3.csv
###  📝 Şarkı    : 
###  singer;lyrics
###  Rafet El Roman;"[Bölüm 1: Rafe...
###  ───────────────────────────────────────────────────────
###    🎵 Tür      : pop (eşleşme yok, varsayılan)
###    % 40  █████████░░░░░░░░░░░░░░░  Düşük güven — dikkatli yorumla
###  
###    💬 Duygu    : umut/coşku 🌟
###    % 70  ████████████████░░░░░░░░  Orta güven
###  
###    📋 Özet     :
###       Rafet El Roman & Derya;Benim acım aşkımdan sana ne İstemiyor
###       um gelmeElini başkası tutmuş bana ne Gözlerine yabancı dalmı
###       ş bana ne
###  ───────────────────────────────────────────────────────
###    ⚠️  Tür tahmini belirsiz — sanatçı adı verirsen daha doğru olur.



# 2. deneme  kelime agirlikli analiz
# Hazır model kullanılmaz. Tamamen turkce_sarki_lexicon.csv
# içindeki kelimelerin ağırlıklı geçiş olasılığına göre
# tür ve duygu tahmini yapılır.

## python3 third.py --dosya sozler1.csv
