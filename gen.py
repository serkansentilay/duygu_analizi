import csv

rows = []

def ekle(kelimeler, tur, tema, duygu, agirlik):
    for k in kelimeler:
        rows.append({"kelime": k.strip(), "tur": tur, "tema": tema, "duygu": duygu, "agirlik": agirlik})

# ARABESK
ekle(["gurbet","gurbette","gurbetçi","garip","yabancı","sürgün","memleket","yurt","vatan","hasretim","hasret"],
     "arabesk","özlem","hüzün",0.95)
ekle(["kader","kadere","kaderim","yazgı","alın","alınyazısı","baht","talih","nasip","felek","feleğin"],
     "arabesk","kader","çaresizlik",0.95)
ekle(["dert","derdim","dertli","dertliyim","ah","ahım","ahlar","feryat","feryada","inle","iniler"],
     "arabesk","acı","hüzün",0.90)
ekle(["çaresiz","çaresizim","çaresizlik","biçare","aciz","zavallı","mahzun","mahzunum","kederli","keder"],
     "arabesk","kader","çaresizlik",0.90)
ekle(["zalim","zalime","zulüm","ezilmek","eziyet","acımasız","merhametsiz","insafsız"],
     "arabesk","isyan","öfke",0.88)
ekle(["terk","terk ettim","terk edilmek","bırakıldım","bıraktı","vefasız","vefasızlık","nankörlük"],
     "arabesk","ayrılık","hüzün",0.90)
ekle(["ağla","ağlıyorum","ağladım","gözyaşı","gözyaşları","yaşlarım","gözlerim dolu","gözlerim"],
     "arabesk","hüzün","hüzün",0.88)
ekle(["yandım","yanıyorum","yanar","yanık","tutuşmak","alev","aleve","yanan"],
     "arabesk","acı","hüzün",0.87)
ekle(["duman","dumanlı","sis","karanlık gece","loş","loşluk"],
     "arabesk","karanlık","hüzün",0.80)
ekle(["sevda","sevdaya","sevdadan","sevdalı","sevdalandım","aşka düştüm","vuruldum"],
     "arabesk","aşk","aşk",0.88)
ekle(["meyhane","meyhanede","içki","rakı","şarap","kadeh","sarhoş","sarhoşum"],
     "arabesk","yalnızlık","hüzün",0.82)
ekle(["yalnız","yalnızım","yalnızlık","yapayalnız","kimsesiz","kimsem yok","tek başına","ıssız"],
     "arabesk","yalnızlık","yalnızlık",0.90)
ekle(["derman","dermanım","dermansız","mecalsiz","halsiz","bitkin","yorgun","tükendim"],
     "arabesk","acı","hüzün",0.83)
ekle(["vah","vay","of","uf","yazık","eyvah","lanet","lanetli"],
     "arabesk","kader","çaresizlik",0.78)
ekle(["ölüm","ölümüm","öldüm","ölüyorum","son nefes","son nefesim"],
     "arabesk","karanlık","hüzün",0.90)
ekle(["acı","acılar","acıdım","sızı","sızıyor","sızladı","içim yanıyor"],
     "arabesk","acı","hüzün",0.92)
ekle(["ihanet","ihanetini","hainlik","hain","dönek","döneklik","yalancı"],
     "arabesk","ayrılık","öfke",0.88)
ekle(["ayrılık","ayrılmak","ayrıldık","elveda","veda","vedalaştık","son görüş","bir daha göremem"],
     "arabesk","ayrılık","hüzün",0.95)
ekle(["inlemek","inliyorum","sızlamak","sızlıyor","yakınmak","yakınıyorum"],
     "arabesk","acı","hüzün",0.85)
ekle(["gönül","gönlüm","gönlüne","yürek","yüreğim","bağrım","bağrıma taş bastım"],
     "arabesk","aşk","hüzün",0.82)
ekle(["yitirmek","yitirdim","kayıp","kayboldu","kaybolmak","yok oldu"],
     "arabesk","hüzün","hüzün",0.87)
ekle(["sabır","sabrediyorum","sabret","dayan","dayanmak","zor"],
     "arabesk","kader","hüzün",0.80)
ekle(["haram","helal","günah","günahlıyım","af","affet","bağışla","yargılama"],
     "arabesk","kader","hüzün",0.80)
ekle(["dua","dua ediyorum","yalvarıyorum","yalvardım","el açtım"],
     "arabesk","kader","hüzün",0.78)
ekle(["gözlerim yolda","yüreğim sızlıyor","bağrım yanık","can evimden vurdu",
      "içim kan ağlıyor","gözüm yaşlı","kara günler","kara talih","kimsem yok bu dünyada"],
     "arabesk","acı","hüzün",0.92)
ekle(["gün ola devran döne","ne oldum ne olacağım","kaderime küstüm","acılar içinde"],
     "arabesk","kader","çaresizlik",0.85)
# ARABESK — ek kelimeler
ekle(["ah çekiyorum","iniltiler","feryadım","sessiz çığlık","iç sızlısı","damla damla",
      "kana kana","mahvettim","mahvoldum","helak oldum"],
     "arabesk","acı","hüzün",0.90)
ekle(["gözüm yaşlı kaldı","yaşlarım dindi","gözyaşlarım kurumaz","ağlamaktan gözlerim şişti"],
     "arabesk","hüzün","hüzün",0.88)
ekle(["haram olsun","lanet olsun","beddua","bedduam","Allah'a havale","yüzüne bakmam"],
     "arabesk","isyan","öfke",0.82)
ekle(["kaderin cilvesi","eller ne der","ne yapsam","ne eylesem","başım derde girdi"],
     "arabesk","kader","çaresizlik",0.83)
ekle(["kimsem yok dünyada","şu gurbette","yıllardır","bu çileli yolda","yıkık gönül"],
     "arabesk","yalnızlık","hüzün",0.87)
ekle(["rakı içtim","içkiye verdim kendimi","sarhoş ettim kederimi","kafayı çektim"],
     "arabesk","yalnızlık","hüzün",0.80)
ekle(["mezar","mezarda","kabir","toprağa düşmek","son toprak","göçüp gitmek"],
     "arabesk","karanlık","hüzün",0.85)
ekle(["yazık bana","yazık sana","ne idim ne oldum","bir zamanlar","eskiden"],
     "arabesk","kader","hüzün",0.80)
ekle(["dağlar kadar derdim var","deniz gibi gözyaşım","sel gibi aktı","fırtına koptu içimde"],
     "arabesk","acı","hüzün",0.88)
ekle(["geç artık","git artık","bırak beni","rahat bırak","yeter bu acılar"],
     "arabesk","ayrılık","öfke",0.83)
ekle(["gönül yarası","yürek yarası","yara sarılmaz","iz kaldı","skat","hasret çekiyorum"],
     "arabesk","ayrılık","hüzün",0.87)
ekle(["vicdansız","merhametsiz","kalpsiz","taş kalpli","buz gibi","soğuk yürekli"],
     "arabesk","isyan","öfke",0.85)     

# HALK
ekle(["yayla","yaylada","yaylalar","yaylım","dağ","dağlar","dağda","dağbaşı","dağ yolu"],
     "halk","doğa","huzur",0.92)
ekle(["türkü","türküler","türkücü","türkü yakmak","deyiş","ağıt","koşma","semah","mani","bozlak"],
     "halk","gelenek","nostalji",0.95)
ekle(["anadolu","anadolum","anadolu toprakları","memleket","yurt","ova","bozkır","bozkırda"],
     "halk","vatan","nostalji",0.92)
ekle(["köy","köyde","köyüm","köylü","mezra","bağ","bahçe","bahçede"],
     "halk","doğa","nostalji",0.88)
ekle(["saz","sazım","bağlama","bağlamam","telli","mızrap","tel"],
     "halk","gelenek","huzur",0.90)
ekle(["efe","efeler","zeybek","meydan","yiğit","yiğitlik","delikanlı","bahadır"],
     "halk","yiğitlik","gurur",0.88)
ekle(["yaren","yarenler","ahbap","dost","dost meclisi","sohbet","muhabbet"],
     "halk","dostluk","mutluluk",0.85)
ekle(["oba","obada","konar göçer","göç","yörük","oymak"],
     "halk","gelenek","nostalji",0.87)
ekle(["kaynak","pınar","pınarda","çeşme","dere","dereden","akarsu"],
     "halk","doğa","huzur",0.82)
ekle(["gelin","gelini","düğün","toy","kına","kına gecesi","davul zurna"],
     "halk","sevinç","mutluluk",0.85)
ekle(["ocak","ocakta","ocakbaşı","ateş başında","semaver","çay"],
     "halk","gelenek","huzur",0.80)
ekle(["atım","at","yolcu","yolculuk","uzak yollar","kervan"],
     "halk","yolculuk","özlem",0.83)
ekle(["sürgün","sürgünde","baskı","zulüm","zalim","ağa","bey"],
     "halk","isyan","öfke",0.85)
ekle(["çoban","çobanlık","sürü","koyun","kuzu","otlak","yayla yolu"],
     "halk","doğa","huzur",0.80)
ekle(["ekin","tarla","tarlada","çift","çiftçi","tohumlar","toprak","kazma"],
     "halk","emek","gurur",0.80)
ekle(["kınalı","kınalı eller","nazlı","ince belli","boynu bükük"],
     "halk","aşk","hüzün",0.82)
ekle(["keklik","turaç","bülbül","kuş","güvercin","kartal","serçe"],
     "halk","doğa","huzur",0.78)
ekle(["çiçek","gül","gül bahçesi","lale","papatya","menekşe","karanfil"],
     "halk","doğa","mutluluk",0.78)
ekle(["irmak","nehir","göl","kıyı","dalgalar","kumsal","sahil"],
     "halk","doğa","huzur",0.78)
ekle(["köylüm","hemşerim","hemşehrilerim","ağabey","kardeş","komşu","ahali"],
     "halk","gelenek","nostalji",0.78)
ekle(["nefes","nefesler","ilahi","ilahiler"],
     "halk","gelenek","nostalji",0.85)
ekle(["Anadolu'nun bağrı","yurt hasreti","diyar diyar","el kapısı","öz yurt"],
     "halk","vatan","nostalji",0.88)
ekle(["horasan","İran","Rumeli","Balkanlar","göçmen","göç yolu","yurt özlemi"],
     "halk","gelenek","nostalji",0.83)
ekle(["derviş meşrebi","pir aşkı","yol kardeşi","can kardeşi","cem","cemde"],
     "halk","gelenek","huzur",0.85)
ekle(["armut","elma","erik","vişne","kiraz","meyve bahçesi","bağbozumu"],
     "halk","doğa","mutluluk",0.75)
ekle(["kar yağıyor","kar altında","kış uykusu","donan toprak","dondurucu"],
     "halk","doğa","hüzün",0.75)
ekle(["harman","harman yeri","döven","tahıl","buğday","arpa","çavdar"],
     "halk","emek","gurur",0.78)
ekle(["ağıt yaktım","ağıt yakan","mersiye","mersiyeler","kara haber"],
     "halk","hüzün","hüzün",0.85)
ekle(["gelin alayı","güvey","damat","düğün evi","halay","kol kola"],
     "halk","sevinç","mutluluk",0.82)
ekle(["tülbent","yemeni","boncuk","gümüş takı","tel kırma","oya"],
     "halk","gelenek","nostalji",0.78)
ekle(["dede","nine","büyükanne","büyükbaba","ocak başında","aile sofrası"],
     "halk","gelenek","nostalji",0.80)
ekle(["kar üstünde iz","ayak izi","yol izi","dağ izi","selvi boylu"],
     "halk","özlem","hüzün",0.80)
ekle(["sabah namazı","ezan sesi","minare","cami","camii avlusu"],
     "halk","gelenek","huzur",0.78)
ekle(["yurt burcu","yurt kokusu","toprak kokusu","çimen kokusu","çiy kokusu"],
     "halk","doğa","huzur",0.78)
ekle(["dilek diledim","murada erdim","niyet ettim","adak adadım"],
     "halk","gelenek","huzur",0.76)

# HALK ROCK
ekle(["toprak","toprağım","toprağa","bu topraklar","vatan toprağı","ana toprak","kara toprak"],
     "halk_rock","vatan","gurur",0.90)
ekle(["isyan","isyanım","isyan ettim","başkaldırı","başkaldırdım","ayaklanma","direniş","direniyorum"],
     "halk_rock","isyan","öfke",0.95)
ekle(["özgürlük","özgürlüğüm","özgür olmak","özgürüm","bağımsız","bağımsızlık","hürriyet","serbestlik"],
     "halk_rock","özgürlük","umut",0.93)
ekle(["kavga","kavgada","kavgamız","mücadele","savaşım","direnmek","direniyorum"],
     "halk_rock","isyan","öfke",0.88)
ekle(["devrim","devrimci","devrimcilik","değişim","kalkışma","halk hareketi"],
     "halk_rock","isyan","öfke",0.90)
ekle(["emek","emeğim","emekçi","emekçiler","alın teri","çalışan","işçi","işçiler"],
     "halk_rock","emek","gurur",0.88)
ekle(["yoksul","yoksulluk","fakir","fakirlik","açlık","açlar","sefalet","sefil"],
     "halk_rock","eşitsizlik","öfke",0.87)
ekle(["zindan","zindanda","hapishane","hapis","tutuklu","esir","esaret","zulüm"],
     "halk_rock","isyan","öfke",0.90)
ekle(["sömürü","sömürüyor","sömürge","baskı altında","boyunduruk","kölelik","köle"],
     "halk_rock","eşitsizlik","öfke",0.92)
ekle(["zincirleri kırmak","özgürleşmek","kurtuluş","kurtulmak","kurtuluş yolu"],
     "halk_rock","özgürlük","umut",0.90)
ekle(["meydan","alanlarda","sokaklarda","yürüyüş","yürüdük","yürüyoruz","halkım"],
     "halk_rock","dayanışma","umut",0.85)
ekle(["ana yüreği","ana sütü","anamın ak sütü","yuvamı yıktılar","yurdumdan"],
     "halk_rock","vatan","hüzün",0.83)
ekle(["boyun eğmeyeceğim","zulme dur demek","halkın sesi","birlikte güçlüyüz","yeni bir dünya"],
     "halk_rock","isyan","öfke",0.90)
ekle(["haksız","haksızlık","adaletsiz","adalet yok","vicdansız","vicdansızlık"],
     "halk_rock","isyan","öfke",0.87)
ekle(["özgürce uçmak"],
     "halk_rock","özgürlük","umut",0.85)
ekle(["halkın türküsü","halk için","ezilenler","ezilen halk","sömürülen"],
     "halk_rock","eşitsizlik","öfke",0.90)
ekle(["ülkem için","yurdun için","vatan için","şehit","şehitler","can verdik"],
     "halk_rock","vatan","gurur",0.88)
ekle([" grev","direniş","barikat","barikatta","ön cephede","ön saflarda"],
     "halk_rock","isyan","öfke",0.88)
ekle(["haksız düzen","bozuk düzen","çürük sistem","bu düzen bozulacak"],
     "halk_rock","isyan","öfke",0.90)
ekle(["söz hakkımız","sesimizi kısma","susturamassın","haykırmaya devam"],
     "halk_rock","isyan","öfke",0.92)
ekle(["dayanışma","el ele","omuz omuza","birlik","beraberlik","birlikte güçlüyüz"],
     "halk_rock","dayanışma","umut",0.87)
ekle(["toprak reformu","köy enstitüsü","eğitim hakkı","okuma yazma"],
     "halk_rock","emek","gurur",0.80)
ekle(["Pir Sultan","Karacaoğlan","Dadaloğlu","Köroğlu","Yunus","Yunus Emre"],
     "halk_rock","gelenek","nostalji",0.85)
ekle(["özgür dünya","daha iyi yarın","yeni düzen","eşit dünya","adil dünya"],
     "halk_rock","özgürlük","umut",0.88)
ekle(["kavgamız sürecek","mücadelemiz bitmez","yılmayacağız","geri adım atmak yok"],
     "halk_rock","isyan","öfke",0.90)

# ROCK
ekle(["çığlık","çığlığım","çığlık atmak","bağır","bağırıyorum","haykırmak","haykırıyorum"],
     "rock","isyan","öfke",0.95)
ekle(["karanlık","karanlıkta","karanlığa","karanlığım","gecenin karanlığı","gece yarısı"],
     "rock","karanlık","korku",0.90)
ekle(["fırtına","fırtınayla","kasırga","şimşek","yıldırım","gök gürültüsü"],
     "rock","güç","öfke",0.88)
ekle(["yıkıl","yıkılmak","çöktüm","çöküyor","dağılmak","paramparça","parçalandım"],
     "rock","çöküş","öfke",0.88)
ekle(["kaos","kaostan","kaotik","anarşi","başıbozukluk","vahşi","sert"],
     "rock","karanlık","öfke",0.87)
ekle(["öfke","öfkeli","öfkeyle","kızgın","kızgınlık","gazap","gazapla"],
     "rock","isyan","öfke",0.92)
ekle(["metal","metalik","sert ses","sert ritim","gitar","gitar rifleri","davul"],
     "rock","güç","güç",0.85)
ekle(["savaş","savaşta","savaşmak","dövüşmek","muharebe","cephe","silah"],
     "rock","isyan","öfke",0.88)
ekle(["yalan dünya","yalan","yalancı","sahte","sahtelik","ikiyüzlü","maskeyi düşür"],
     "rock","isyan","öfke",0.87)
ekle(["kırıl","parça parça","paramparça","dağıl","çöküş","enkaz","yıkım","harabeye"],
     "rock","çöküş","hüzün",0.85)
ekle(["şeytan","şeytanla","iblis","cehennem","cehenneme","lanet","lanetli"],
     "rock","karanlık","korku",0.82)
ekle(["kan","kanlı","kan dökmek","kanım","yara","yaralı","yara izi"],
     "rock","acı","öfke",0.87)
ekle(["nefret","nefret ediyorum","nefretle","iğreniyorum","tiksiniyorum"],
     "rock","isyan","öfke",0.93)
ekle(["içimde fırtınalar","her şey yalan","gece bitmez sandım"],
     "rock","isyan","öfke",0.88)
ekle(["distorsiyon","riff","heavy","grunge","punk","metal çığlığı","amplifikatör"],
     "rock","müzik","güç",0.83)
ekle(["duman içinde","dumanlı sahne","siyah giysi","siyah bayrak","karanlık sahne"],
     "rock","karanlık","korku",0.80)
ekle(["çığlık atmak","bağıra bağıra","kahretsin","kahrolsun","defol"],
     "rock","isyan","öfke",0.90)
ekle(["iç çöküşü","ruhsal çöküş","zihin karanlığı","beyin yıkama","manipülasyon"],
     "rock","karanlık","öfke",0.87)
ekle(["yıkıntı arasında","küllerden doğmak","yeniden dirilmek","feniksin gibi"],
     "rock","çöküş","güç",0.83)
ekle(["özgür ruh","bağımsız ruh","etiket yok","kural tanımıyorum","sınır tanımam"],
     "rock","özgürlük","güç",0.87)
ekle(["sis içinde","sisin içinde","yok oluyorum","varlık yokluk","anlamsızlık"],
     "rock","karanlık","hüzün",0.83)
ekle(["acımasız dünya","acımasızca","kanlı tırnak","dişler çıktı","savaşan ruh"],
     "rock","isyan","öfke",0.87)
ekle(["duman tüten","kül olmuş","yanıp kül","toz duman","enkaz altında"],
     "rock","çöküş","hüzün",0.83)
ekle(["nefes alamıyorum","boğuluyorum","sıkışıp kaldım","kafes içinde","hapsoldum"],
     "rock","isyan","öfke",0.85)
ekle(["yaşamak istemiyorum","ölmek gibi hissediyorum","ruhum çıktı","içim boşaldı"],
     "rock","karanlık","hüzün",0.82)
ekle(["adrenalin","adrenalini","reaksiyon","patlama","patlamaya hazır","volkan"],
     "rock","güç","güç",0.85)


# RAP
ekle(["flow","flowum","flow atmak","kafiye","bars","bar attım","verse","rime"],
     "rap","müzik","güç",0.95)
ekle(["beat","beatin","beat drop","ritim","trap beat","drill beat","boom bap","sample","loop"],
     "rap","müzik","güç",0.92)
ekle(["sokak","sokaklarda","sokak çocuğu","sokak hayatı","mahalle","semt","gecekondu"],
     "rap","gerçeklik","gerçeklik",0.90)
ekle(["para","paramı","para kazanmak","zengin","servet","altın","nakit"],
     "rap","güç","hırs",0.85)
ekle(["mikrofon","mikrofonumu","sahnede","sahne","klip","stüdyo","kayıt"],
     "rap","müzik","güç",0.88)
ekle(["freestyle","freestyle atmak","cipher","battle","battle rap","diss","diss track"],
     "rap","müzik","güç",0.88)
ekle(["swag","tarz","tarzım","stil","stilim","özgün","kendime özgü"],
     "rap","kimlik","gurur",0.82)
ekle(["trap","trapci","drill","gangsta","geto","getoda","blok"],
     "rap","gerçeklik","gerçeklik",0.87)
ekle(["gerçek","gerçeği","gerçek konuşmak","yüzleş","sansür","yasak"],
     "rap","gerçeklik","gerçeklik",0.88)
ekle(["şan","şöhret","ün","ünlü olmak","tanınmak","fenomen","viral"],
     "rap","güç","hırs",0.82)
ekle(["sistem","sistemi yık","düzene isyan","düzeni boz"],
     "rap","isyan","öfke",0.87)
ekle(["yoksulluk","yoksul","fakir büyüdüm","getto","dar gelirli","açlık","aç"],
     "rap","gerçeklik","hüzün",0.85)
ekle(["anneme","annemi","annem için","babam","ailem","büyüdüm","çocukluğum"],
     "rap","gerçeklik","nostalji",0.80)
ekle(["sokak bizi yetiştirdi","gerçeği söylüyorum","mikrofon elimde","sözlerim keskin","kafiye diziyorum","beat üstüne"],
     "rap","müzik","güç",0.88)
ekle(["sahte dostlar","ihanet","yalnız bıraktı"],
     "rap","yalnızlık","öfke",0.83)
ekle(["mix","miksaj","prodüksiyon","prodüktör","yapım","kayıt stüdyosu","albüm"],
     "rap","müzik","güç",0.83)
ekle(["sahada","sahada büyüdük","mahallede","geceyi gündüz ettim","yolun başında"],
     "rap","gerçeklik","gerçeklik",0.85)
ekle(["altın kolye","marka","lüks","araba","Porsche","ayakkabı","sneaker"],
     "rap","güç","hırs",0.78)
ekle(["haters","haset","çekemeyenler","bana çamur atanlar","kıskanç bakışlar"],
     "rap","kimlik","öfke",0.82)
ekle(["özgünlük","özgünum","taklit yok","kendi sesim","kendim gibiyim"],
     "rap","kimlik","gurur",0.83)
ekle(["toplumsal baskı","şartlanma","önyargı","önyargılarla savaş","klişe"],
     "rap","isyan","öfke",0.83)
ekle(["sabırlıyım","sabredeceğim","emek vereceğim","çalışmak","çalışıyorum"],
     "rap","emek","gurur",0.80)
ekle(["türkçe rap","yerli müzik","yer altı","underground","bağımsız","indie"],
     "rap","müzik","güç",0.80)
ekle(["punch line","hook","nakarat","bridge","intro","outro"],
     "rap","müzik","güç",0.80)
ekle(["şehrin lambası","gece yarısı şehri","sokak lambası","karanlık sokak"],
     "rap","gerçeklik","hüzün",0.80)
ekle(["kimliğim var","köküm var","nereden geldiğimi bilirim","geçmişim var"],
     "rap","kimlik","gurur",0.83)
ekle(["dedim ya","anladın mı","bak buraya","dinle beni","dikkat et"],
     "rap","gerçeklik","güç",0.75)
ekle(["diss yedim","diss attım","yanıt verdim","hesap sorduk","hesaplaştık"],
     "rap","isyan","öfke",0.82)


# SANAT
ekle(["ney","neyin","neyle","ney sesi","kaval","ud","ude"],
     "sanat","müzik","huzur",0.95)
ekle(["makam","makamda","hicaz","rast","uşşak","nihavend","segah","saba","hüzzam"],
     "sanat","müzik","huzur",0.92)
ekle(["beste","bestelerim","besteci","bestekâr","eser","güfte","güftesi"],
     "sanat","müzik","huzur",0.90)
ekle(["gazel","gazelden","divan","divan şiiri","nazire","kaside","kıta"],
     "sanat","gelenek","nostalji",0.88)
ekle(["fasıl","fasılda","meşk","meşkte","icra","seslendirmek","yorumlamak"],
     "sanat","müzik","huzur",0.87)
ekle(["kanun","kanun çalmak","tanbur","keman","lavta","rebap"],
     "sanat","müzik","huzur",0.88)
ekle(["tasavvuf","tasavvufi","derviş","dervişlik","tekke","zikir","semah"],
     "sanat","ruhanilik","huzur",0.88)
ekle(["gönüle","can","candan","ruh","ruhuma","ruhana"],
     "sanat","ruhanilik","huzur",0.85)
ekle(["aşk-ı ilahi","ilahi aşk","ilahiler","zikir","tevekkül","teslimiyet"],
     "sanat","ruhanilik","huzur",0.90)
ekle(["mürşit","pir","pirim","üstat","üstadım","hoca"],
     "sanat","ruhanilik","huzur",0.82)
ekle(["şiir","şiirim","mısra","mısralar","dize","dizeler","nazım"],
     "sanat","şiir","huzur",0.85)
ekle(["hat sanatı","tezhip","ebru","minyatür","çini","mozaik","sedefkârlık"],
     "sanat","gelenek","huzur",0.82)
ekle(["divân edebiyatı","divan şairi","aruz","hece","redif","kafiye"],
     "sanat","şiir","huzur",0.83)
ekle(["tekkede","dergahta","halvette","sohbette","ders halkasında"],
     "sanat","ruhanilik","huzur",0.85)
ekle(["Mevlana","Hacı Bektaş","Yunus","Fuzuli","Baki","Nedim","Şeyh Galip"],
     "sanat","gelenek","nostalji",0.85)
ekle(["neyzen","udî","kemençe","kanunî","hafız","müezzin","ilahici"],
     "sanat","müzik","huzur",0.85)
ekle(["sema","semah","zikir halkası","zikir sesi","tekbir","salavat"],
     "sanat","ruhanilik","huzur",0.88)
ekle(["adab","erkân","yol","erkan","talip","muhibban"],
     "sanat","ruhanilik","huzur",0.82)
ekle(["terennüm","nağme","nağmeler","makam perdesi","koma","seyir"],
     "sanat","müzik","huzur",0.85)
ekle(["gönül erleri","hakikat yolu","irfan meclisi","ehl-i dil","ehl-i aşk"],
     "sanat","ruhanilik","huzur",0.83)
ekle(["osmanlı","osmanlıca","beyit","kıta","murabba","muhammes","terci"],
     "sanat","gelenek","nostalji",0.80)
ekle(["ses titremesi","vibrato","portamento","glissando","duygusal ton"],
     "sanat","müzik","huzur",0.80)



# POP
ekle(["dans","dans et","dans ediyorum","dans edelim","hareket","hareket et","oyna"],
     "pop","eğlence","mutluluk",0.90)
ekle(["eğlence","eğlenceli","eğlenmek","parti","kutlama","neşe","neşeyle"],
     "pop","eğlence","mutluluk",0.92)
ekle(["mutlu","mutluyum","mutluluk","sevinç","coşku","coşkuyla","aydınlık"],
     "pop","sevinç","mutluluk",0.90)
ekle(["aşkım","aşkıma","sevgilim","seviyor musun","sev beni","seviyorum","seni seviyorum"],
     "pop","aşk","aşk",0.88)
ekle(["gel","gel gidelim","gel bana","yanıma gel","hadi gel","beklerim","bekliyorum"],
     "pop","aşk","aşk",0.82)
ekle(["sabah","sabahında","sabah güneşi","yeni gün","yeni sabah","günaydın","şafak"],
     "pop","umut","mutluluk",0.80)
ekle(["hayat","hayatım","hayat güzel","yaşam","yaşıyorum","yaşayalım","ömür"],
     "pop","yaşam","mutluluk",0.82)
ekle(["şarkı","şarkım","söyle","söylüyorum","müzik","melodi","notalar"],
     "pop","müzik","mutluluk",0.82)
ekle(["öp","öpüşmek","öptüm","dudaklar","dokunmak","sarılmak","kucak"],
     "pop","aşk","aşk",0.83)
ekle(["tatil","plaj","deniz","kumsal","güneş","yaz","yaz geldi"],
     "pop","eğlence","mutluluk",0.78)
ekle(["güzel","çok güzel","çok güzelsin","harika","mükemmel","muhteşem"],
     "pop","aşk","mutluluk",0.78)
ekle(["neşeli","keyifli","keyifle","güzel vakit","güzel an"],
     "pop","sevinç","mutluluk",0.80)
ekle(["playlist","şarkı listesi","kulaklık","kulaklıkla","repeat","yeniden dinle"],
     "pop","müzik","mutluluk",0.72)
ekle(["sosyal medya","paylaşım","reels","hikaye","story","gönderi","beğeni"],
     "pop","eğlence","mutluluk",0.68)
ekle(["gece çıktık","bar","kulüp","klüp","gece hayatı","sahne aldım"],
     "pop","eğlence","mutluluk",0.75)
ekle(["ayna karşısında","makyaj","saç","stil değişimi","dönüşüm","yeni ben"],
     "pop","kimlik","gurur",0.72)
ekle(["tatil planları","uçak bileti","valize","bavul","yola düştüm"],
     "pop","eğlence","mutluluk",0.70)
ekle(["iki bardak","kadeh kaldır","tost","kutlama zamanı","şerefe"],
     "pop","eğlence","mutluluk",0.75)
ekle(["mor","sarı","kırmızı","mavi renk","rengarenk","renkli dünya"],
     "pop","sevinç","mutluluk",0.68)
ekle(["fısıldıyorsun","kulağıma","gözlerinden","bakışlarından","dokunuşunda"],
     "pop","aşk","aşk",0.83)
ekle(["taksi","metro","bus","akşam saatinde","şehir ışıkları","trafikte"],
     "pop","yalnızlık","hüzün",0.70)
ekle(["kalbim hızlı atıyor","nefesim kesildi","dili tutuldu","söz bulamadım"],
     "pop","aşk","aşk",0.83)
ekle(["ilk görüşte","anlık","o an","o saniye","ilk bakış","ilk söz"],
     "pop","aşk","aşk",0.82)
ekle(["şirinsin","tatlısın","ne kadar güzelsin","mükemmelsin","harikasın"],
     "pop","aşk","mutluluk",0.78)
ekle(["uyuyamıyorum","gözüme uyku girmiyor","sabaha kadar","bekliyorum seni"],
     "pop","özlem","hüzün",0.83)
ekle(["mesafe","uzaklık","kilometre","deniz aşırı","farklı şehirlerde"],
     "pop","özlem","hüzün",0.82)
ekle(["sevgi dili","dokunuş","hediye","zaman","söz","beklenti","anlayış"],
     "pop","aşk","aşk",0.78)
ekle(["sarıldığında","koklarken","gülüşünde","sesinde","sende","yalnız sende"],
     "pop","aşk","aşk",0.85)
ekle(["kırgınlık","kırıldım","incidin mi","üzdüm mü","özür dilerim"],
     "pop","ayrılık","hüzün",0.80)
ekle(["bitmek bilmiyor","bitmiyor mu","ne zaman bitecek","bitmesini istedim"],
     "pop","ayrılık","hüzün",0.80)
ekle(["küstüm","küs oldum","barışalım mı","küskünüz","barışmak istiyorum"],
     "pop","kıskançlık","hüzün",0.80)



# AŞK / AYRILIK / ÖZLEM
ekle(["aşk","aşkım","sevgi","sevgim","sevda","yar","yarım","tutku","tutkuyla","arzu"],
     "pop","aşk","aşk",0.95)
ekle(["ayrılık","ayrılmak","ayrıldık","elveda","veda","bitti","bitmek","sona erdi","son"],
     "pop","ayrılık","hüzün",0.95)
ekle(["gitmek","gidiyorum","gitme","gittin","neden gidiyorsun","bırakıp gitme","bırakma beni"],
     "pop","ayrılık","hüzün",0.92)
ekle(["terk","terk ettim","bıraktı","bırakıldım","yüzüstü bırakıldım"],
     "pop","ayrılık","hüzün",0.92)
ekle(["aldatma","aldattın","aldatıldım","ihanet","aldatmak","hainlik","dönek"],
     "pop","ayrılık","öfke",0.92)
ekle(["yalnız kaldım","yalnız bıraktı","yalnızım","yapayalnızım","kimsem yok","tek başıma"],
     "pop","yalnızlık","hüzün",0.90)
ekle(["gözyaşı","gözyaşlarım","ağladım","ağlıyorum","çok ağladım"],
     "pop","ayrılık","hüzün",0.88)
ekle(["eksik","eksiksin","seni hissediyorum","seni arıyorum","seni görmek istiyorum"],
     "pop","özlem","hüzün",0.87)
ekle(["özlem","özlüyorum","özledim","hasret","hasretim","hasretle"],
     "pop","özlem","hüzün",0.95)
ekle(["anı","anılar","hatıra","hatırladım","eski","eski günler","o günler","geçmiş"],
     "pop","nostalji","nostalji",0.90)
ekle(["çocukluk","çocukluğum","çocukken","gençlik","gençliğim"],
     "pop","nostalji","nostalji",0.88)
ekle(["memleket","memleketim","doğduğum yer","büyüdüğüm yer","köküm"],
     "arabesk","nostalji","nostalji",0.88)
ekle(["pencere","pencereden","camdan bakıyorum","bekliyorum","yolunu gözlüyorum","bekleyiş"],
     "arabesk","özlem","hüzün",0.83)
ekle(["fotoğraf","fotoğrafına","resim","hayalin","hayalinde"],
     "pop","nostalji","nostalji",0.82)
ekle(["seninle","seninle olmak","birlikte","beraber","beraberlik","ikimiz"],
     "pop","aşk","aşk",0.85)
ekle(["kalp","kalbim","kalbime","kalp atışı","kalp çarpıyor","heyecan","nabzım"],
     "pop","aşk","aşk",0.85)
ekle(["hasretini","hasretinle","seni özledim","seni bekliyorum","gözlerim yolda"],
     "pop","özlem","hüzün",0.88)
ekle(["ay","ay ışığında","yıldızlar","gece gökyüzü","bulutlar","rüzgâr"],
     "pop","aşk","huzur",0.78)
ekle(["el ele","yan yana","baş başa","göz göze","dudak dudağa"],
     "pop","aşk","aşk",0.85)
ekle(["sensiz olmaz","sensiz yapamam","seni çok özledim","gel geri","dön bana","kalbim seninle"],
     "pop","özlem","hüzün",0.88)
ekle(["nerede sen","seni arıyorum","yapayalnız bıraktın","hiçbir şey eskisi gibi","eski günleri özledim"],
     "pop","özlem","hüzün",0.88)

# YALNIZLlK
ekle(["yalnız","yalnızım","yalnızlık","yapayalnız","tek başıma"],
     "pop","yalnızlık","yalnızlık",0.97)
ekle(["kimsesiz","kimsesizim","kimsem yok","kimse yok","dünyada tek","terk edilmiş"],
     "pop","yalnızlık","yalnızlık",0.93)
ekle(["sessiz","sessizlik","sessizce","suskunluk","susmak","boşluk","boşlukta"],
     "pop","yalnızlık","hüzün",0.88)
ekle(["boş","boş oda","boş ev","boş yatağım","boş sandalye","boşluk"],
     "pop","yalnızlık","hüzün",0.87)
ekle(["soğuk","soğukluk","soğuk gece","soğuk sabah","donuk","buz gibi"],
     "pop","yalnızlık","hüzün",0.82)
ekle(["içim boş","içim yanıyor","içimde","derinden","kaybolmak","düşüyorum"],
     "pop","yalnızlık","hüzün",0.85)

# UMUT
ekle(["umut","umutla","umutluyum","umut var","ümit","ümitle","ümitliyim"],
     "pop","umut","umut",0.95)
ekle(["güneş","güneş doğdu","güneşli","aydınlık","ışık","ışıkla","ışık var"],
     "pop","umut","mutluluk",0.90)
ekle(["yarın","yarına","gelecek","ilerisi","yeni başlangıç"],
     "pop","umut","umut",0.88)
ekle(["başlangıç","yeni başlangıç","yeniden başlamak","hayata tutunmak"],
     "pop","umut","umut",0.87)
ekle(["güçlü","güçlüyüm","ayağa kalkmak","dimdik durmak","dik dur","baş eğme"],
     "pop","güç","güç",0.85)
ekle(["sevinç","sevinçle","sevinçli","neşe","neşeli","coşku","mutlu son"],
     "pop","sevinç","mutluluk",0.88)
ekle(["kanatlanmak","uçmak","özgürce","serbest","engel yok","sınır yok"],
     "pop","özgürlük","umut",0.83)
ekle(["özgüven","özgüvenim","kendime güveniyorum","kendin ol","kim olduğunu bil"],
     "pop","güç","gurur",0.80)

# KISKANÇLIK
ekle(["kıskanç","kıskançlık","kıskanıyorum","kıskandım","kıskandırma","gözüm sende"],
     "pop","kıskançlık","öfke",0.90)
ekle(["aldattın","aldatıldım","başkasıyla","başkası var","başkasını sevdin"],
     "pop","ihanet","öfke",0.93)
ekle(["şüphe","şüpheli","şüphelendim","emin değilim","güvenemiyorum"],
     "pop","kıskançlık","öfke",0.85)
ekle(["ihanet","ihanet ettin","sırt döndün","hançerlendi","hançer"],
     "pop","ihanet","öfke",0.92)
ekle(["yalan","yalancı","yalan söyledin","beni kandırdın","oyun oynadın"],
     "pop","ihanet","öfke",0.88)

# GENEL DUYGULAR
ekle(["korku","korkuyorum","korktum","korkusuz","cesur","cesaret"],
     "pop","korku","korku",0.88)
ekle(["üzüntü","üzgün","üzgünüm","üzüldüm","keder","kederli","hüzünlüyüm"],
     "pop","hüzün","hüzün",0.90)
ekle(["mutluluk","mutlu","mutluyum","sevinç","sevinçli","keyif","memnun","tatmin"],
     "pop","sevinç","mutluluk",0.90)
ekle(["şaşkın","şaşkınlık","şaşırdım","inanamıyorum","hayret","beklemedim"],
     "pop","şaşkınlık","şaşkınlık",0.82)
ekle(["gurur","gururlu","gurur duyuyorum","onur","onurlu","şeref","şerefli"],
     "pop","gurur","gurur",0.82)
ekle(["utanç","utanıyorum","utandım","mahcup","aşağılandım","rezil"],
     "pop","utanç","utanç",0.82)
ekle(["heyecan","heyecanlı","coştu","titriyor","titriyorum","beklenti"],
     "pop","heyecan","mutluluk",0.82)
ekle(["pişmanlık","pişmanım","pişman oldum","keşke","keşke yapmasaydım"],
     "pop","pişmanlık","hüzün",0.85)
ekle(["merak","merak ediyorum","bilmek istiyorum","sır","sırlar"],
     "pop","merak","şaşkınlık",0.75)
ekle(["bıktım","bıktım artık","bunaldım","çıldırıyorum","sabrım kalmadı"],
     "pop","isyan","öfke",0.88)
# ELEKTRONİK / POP DANS — yeni tür eklentisi
ekle(["drop","beat drop","bass","bas","bum bum","elektronik","synth","synthesizer"],
     "pop","müzik","güç",0.85)
ekle(["dancefloor","dans pisti","pist","gece yarısı dans","vücut","ritme kapıldım"],
     "pop","eğlence","mutluluk",0.83)
ekle(["neon ışık","lazer","sahne ışıkları","soyut","renk cümbüşü"],
     "pop","eğlence","mutluluk",0.75)
ekle(["echo","yankı","reverb","ince ses","ses efekti","arpej"],
     "pop","müzik","huzur",0.72)

# YENİ DUYGULAR — ek
ekle(["affetmek","affettim","affedebilir miyim","içimdeki kini bıraktım"],
     "pop","pişmanlık","huzur",0.80)
ekle(["teşekkür ederim","minnettarım","şükür","şükrediyorum"],
     "pop","sevinç","mutluluk",0.75)
ekle(["inanmıyorum","kabul edemiyorum","reddediyorum","hayır demek","dur demek"],
     "pop","isyan","öfke",0.80)
ekle(["ne hissediyorum","duygulanmak","duygulandım","gözlerim doldu","boğazım düğümlendi"],
     "pop","hüzün","hüzün",0.80)
ekle(["çelişki","çelişiyorum","ikircikli","kararsızım","ne yapmalıyım"],
     "pop","korku","şaşkınlık",0.72)
ekle(["kendini yok saydın","görmezden geldin","umursamadın","değer vermedin"],
     "pop","ayrılık","öfke",0.85)
ekle(["anlayış","anlamak","anla beni","beni anla","kimse anlamıyor"],
     "pop","yalnızlık","hüzün",0.80)
ekle(["ego","egom var","gururumu eğmedim","eğmem","kibir","kibirli"],
     "pop","kimlik","güç",0.75)

# DOĞA / ÇEVRE
ekle(["ormanda","orman içinde","çam kokusu","çam ormanı","ağaç gövdesi"],
     "halk","doğa","huzur",0.80)
ekle(["kuş sesi","kuş şakıması","sabah kuşları","ötüyor","ötüşü"],
     "halk","doğa","huzur",0.78)
ekle(["yağmur","yağmur altında","yağmurlu gün","damla damla","yağmur sesi"],
     "pop","yalnızlık","hüzün",0.78)
ekle(["şimşek çaktı","gök gürültüsü","fırtına öncesi","bulutlar toplandı"],
     "rock","karanlık","korku",0.78)
ekle(["mevsim değişiyor","sonbahar","sararan yapraklar","dökülen yaprak","güz"],
     "pop","nostalji","hüzün",0.78)
ekle(["ilkbahar çiçekleri","bahar yağmuru","bahar havası","tomurcuklar açtı"],
     "pop","umut","mutluluk",0.75)
ekle(["güneş batıyor","batmakta olan güneş","akşam gökyüzü","kızıl bulutlar"],
     "pop","hüzün","hüzün",0.75)
ekle(["okyanusta","denizin dibinde","dalgaların altında","suya daldım"],
     "pop","özlem","hüzün",0.75)

# ZIT DUYGULAR
ekle(["hem seviyorum hem nefret ediyorum","aşk mı nefret mi","karmaşık duygular"],
     "pop","kıskançlık","öfke",0.80)
ekle(["ağlarken gülmek","gülerken ağlamak","gülen gözlerle ağlamak"],
     "pop","hüzün","hüzün",0.80)
ekle(["karanlıkta umut","acıdan güç almak","dertlerimden ders aldım"],
     "arabesk","kader","hüzün",0.80)
ekle(["bitmek üzere ama bitmedi","tükenmek üzere ama durdum","son nefeste","son anda"],
     "arabesk","kader","hüzün",0.83)

# FİİL TÜREVLERİ
fiil_ekler = [
    (["sev","sevil","seviş","seviyorum","sevmedim","sevemiyorum"],"pop","aşk","aşk",0.88),
    (["öp","öpüş","öpüşmek","öpüldüm"],"pop","aşk","aşk",0.85),
    (["sarıl","sarılmak","sarıldım","sarılıyorum"],"pop","aşk","aşk",0.85),
    (["bekle","beklet","beklettim","bekletiliyorum"],"pop","özlem","hüzün",0.82),
    (["ağla","ağlat","ağlatma","ağlatıyorsun"],"pop","hüzün","hüzün",0.88),
    (["git","gitme","gitmeyeceksin","gidiyorum"],"pop","ayrılık","hüzün",0.90),
    (["gel","gelme","gelmeyeceksin","geliyor musun"],"pop","özlem","hüzün",0.82),
    (["yak","yakma","yaktın","yakıyorsun"],"arabesk","acı","hüzün",0.85),
    (["bırak","bırakma","bıraktın","bırakıyorsun"],"pop","ayrılık","hüzün",0.88),
    (["kaç","kaçma","kaçtın","kaçıyorsun"],"pop","ayrılık","hüzün",0.82),
    (["dön","dönme","döndün","dönüyorsun"],"pop","özlem","umut",0.85),
    (["unut","unutma","unuttun","unutuyorsun"],"pop","ayrılık","hüzün",0.87),
    (["anımsa","anımsıyorum","anımsadım","anımsamak"],"pop","nostalji","nostalji",0.83),
    (["haykır","haykırıyorum","haykırdım","haykırmak"],"rock","isyan","öfke",0.88),
    (["kavuş","kavuşmak","kavuşamıyorum","kavuştum"],"arabesk","özlem","umut",0.85),
    (["yanmak","yanıyorum","yandım","yanar"],"arabesk","acı","hüzün",0.87),
    (["solmak","soluyorum","soldum","solar"],"pop","hüzün","hüzün",0.80),
    (["titremek","titriyorum","titredim","titrer"],"pop","korku","korku",0.80),
    (["yıkılmak","yıkılıyorum","yıkıldım","yıkılır"],"rock","çöküş","hüzün",0.85),
]
for kelimeler, tur, tema, duygu, agirlik in fiil_ekler:
    ekle(kelimeler, tur, tema, duygu, agirlik)

# SIFAT TÜREVLERİ
sifat_ekler = [
    (["sevinçli","sevinçsiz","sevinçle","sevinçten"],"pop","sevinç","mutluluk",0.85),
    (["hüzünlü","hüzünsüz","hüzünle","hüzünden"],"pop","hüzün","hüzün",0.88),
    (["kederli","kedersiz","kederle","kederden"],"arabesk","hüzün","hüzün",0.85),
    (["umutlu","umutsuz","umutla","umutten"],"pop","umut","umut",0.88),
    (["korkulu","korkusuz","korkuyla","korkudan"],"pop","korku","korku",0.85),
    (["öfkeli","öfkesiz","öfkeyle","öfkeden"],"rock","isyan","öfke",0.88),
    (["yalnızca","yalnızdım","yalnız kaldım","yalnız mıyım"],"pop","yalnızlık","yalnızlık",0.88),
    (["sessizce","sessizim","sessiz kaldım"],"pop","yalnızlık","hüzün",0.82),
    (["karanlıkta","karanlıkça","karanlık dünya"],"rock","karanlık","korku",0.85),
    (["ışıklı","ışıksız","ışıkla","ışıktan"],"pop","umut","mutluluk",0.82),
    (["güçlü","güçsüz","güçle","güçten"],"pop","güç","güç",0.83),
    (["özgür","özgürce","özgürsüz"],"halk_rock","özgürlük","umut",0.88),
    (["mutluca","mutluyken","mutlu olmak"],"pop","sevinç","mutluluk",0.85),
    (["acıyla","acılı","acısız","acıdan"],"arabesk","acı","hüzün",0.88),
    (["derinden","derin","derinlemesine"],"pop","hüzün","hüzün",0.78),
    (["tutkuyla","tutkulu","tutkusuz","tutkudan"],"pop","aşk","aşk",0.87),
    (["sevgiyle","sevgili","sevgisiz","sevgiden"],"pop","aşk","aşk",0.88),
    (["hasretle","hasretli","hasretsiz","hasretten"],"arabesk","özlem","hüzün",0.90),
    (["gurbetle","gurbetli","gurbet çeken","gurbet yolu"],"arabesk","özlem","hüzün",0.88),
    (["vefasız","vefasızca","vefasızlıktan"],"arabesk","ayrılık","öfke",0.87),
    (["zalimce","zalimlik","zalimden"],"arabesk","isyan","öfke",0.85),
    (["çaresizce","çaresizlik","çaresizden"],"arabesk","kader","çaresizlik",0.88),
]
for kelimeler, tur, tema, duygu, agirlik in sifat_ekler:
    ekle(kelimeler, tur, tema, duygu, agirlik)

# ZAMAN/MEKÂN
mekan_tur = [
    (["gece","geceden","geceye","geceler","geceleri","gece gece","gece boyu","gece yarıları"],"pop","yalnızlık","hüzün",0.78),
    (["sabah","sabahtan","sabaha","sabahlar","sabah sabah","her sabah"],"pop","umut","mutluluk",0.75),
    (["kapı","kapıdan","kapıya","kapı önünde","kapıyı çalmak"],"pop","özlem","hüzün",0.75),
    (["ev","evden","eve","evde","evim","evime","evi özledim"],"pop","nostalji","nostalji",0.75),
    (["göz","gözden","göze","gözleri","gözlerimden","gözlerinde"],"arabesk","hüzün","hüzün",0.80),
    (["yürek","yürekten","yüreğe","yüreğim","yüreğimde","yüreğime"],"arabesk","acı","hüzün",0.85),
    (["el","elden","ele","eller","elleri","ellerim","ellerinden"],"pop","aşk","aşk",0.75),
    (["ses","sesten","sese","sesler","sesi","sesini","sesim yok"],"pop","özlem","hüzün",0.78),
    (["rüzgar","rüzgardan","rüzgara","rüzgarla","rüzgar gibi"],"halk","doğa","huzur",0.75),
    (["ateş","ateşten","ateşe","ateşim","ateşle","ateş gibi"],"arabesk","acı","hüzün",0.82),
    (["gün","günden","güne","günler","günlerim","her gün","o gün","o günler"],"pop","nostalji","nostalji",0.72),
    (["yaz","yazdan","yaza","yazın","yaz gelince","o yazlar"],"pop","nostalji","nostalji",0.75),
    (["kış","kıştan","kışa","kışlar","kışın","soğuk kış","uzun kış"],"pop","yalnızlık","hüzün",0.75),
    (["bahar","bahara","bahardan","baharlar","baharda","ilkbahar","bahar geldi"],"pop","umut","mutluluk",0.78),
    (["toprak","topraktan","toprağa","topraklar","toprağım","topraklarımda"],"halk","doğa","nostalji",0.80),
    (["dağ","dağdan","dağa","dağlar","dağlarda","dağ başı","dağ yolu","karlı dağlar"],"halk","doğa","huzur",0.82),
]
for kelimeler, tur, tema, duygu, agirlik in mekan_tur:
    ekle(kelimeler, tur, tema, duygu, agirlik)

# EŞ ANLAMLILAR
es_anl = [
    (["keder","ıstırap","sıkıntı","bunaltı","kasvet","melankoli","melankolim",
      "karamsarlık","karamsarlığım","pes etmek","umutsuzluk","umutsuzum",
      "çöküntü","hayal kırıklığı"],"pop","hüzün","hüzün",0.87),
    (["seviniyorum","neşe","neşeli","coşku","coşkun","keyif","keyifli","memnuniyet",
      "memnunum","tatmin","tatminlik","huzur","huzurluyum","rahatlık","rahatladım",
      "ferahlık","ferahladım"],"pop","sevinç","mutluluk",0.87),
    (["sinir","sinirli","kızgın","kızgınlık","hiddet","hiddetli","gazap","gazaplı",
      "isyankâr","kin","kin besliyorum","düşmanlık","düşman","hasmım"],"rock","isyan","öfke",0.87),
    (["ümit","beklenti","beklentili","inanç","inançla","güven","güveniyorum",
      "inanıyorum","geleceğe bakıyorum","iyimser","iyimserlik","pozitif"],"pop","umut","umut",0.87),
    (["özlüyorum","arayış","arıyorum","bekliyorum","yolunu gözlüyorum",
      "neredeydin","neredesin","görüşmek istiyorum","sesini duymak istiyorum"],"pop","özlem","hüzün",0.87),
    (["korkuyorum","endişe","endişeliyim","kaygı","kaygılıyım","tedirgin","tedirginim",
      "ürkek","ürküyorum","dehşet","panik"],"pop","korku","korku",0.85),
    (["ıssızlık","ıssız","kimsesizlik","kimsesizim","boşluk","boşluktayım",
      "terk edilmişlik","dışlanmak","dışlandım","ihmal","ihmal edildim"],"pop","yalnızlık","yalnızlık",0.90),
    (["nostaljik","geçmişe dönmek","o zamanlar","o günler","genç günlerim",
      "gençlik","gençliğim"],"pop","nostalji","nostalji",0.87),
]
for kelimeler, tur, tema, duygu, agirlik in es_anl:
    ekle(kelimeler, tur, tema, duygu, agirlik)

# Ekstralar
ekle(["telefon","mesaj","arama","aramak","arıyorum","sesini duymak","sesini özledim"],
     "pop","özlem","hüzün",0.78)
ekle(["buluşmak","buluşalım","randevu","görüşelim","yeniden görmek"],
     "pop","aşk","mutluluk",0.78)
ekle(["rüya","rüyamda","düşlerim","hayal","hayalim","hayal kuruyorum"],
     "pop","umut","genel",0.75)
ekle(["yol","yolculuk","yola çıkmak","yol almak","uzun yol","yol ayrımı","ayrı yollar"],
     "pop","özlem","genel",0.72)
ekle(["nefes","nefes alıyorum","nefes kesiliyor","nefes ver","derin nefes","soluk"],
     "pop","genel","genel",0.70)
ekle(["bazen","ara sıra","zaman zaman","her zaman","her gün","günler geçiyor"],
     "pop","nostalji","nostalji",0.65)

# ── TEKRAR TEMİZLE ─────────────────────────────────────────────
print(f"Ham toplam: {len(rows)}")
seen = set()
unique = []
for r in rows:
    key = (r["kelime"].lower(), r["tur"])
    if key not in seen:
        seen.add(key)
        unique.append(r)

print(f"Tekrarsız: {len(unique)}")

with open("./turkce_sarki_lexicon.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["kelime","tur","tema","duygu","agirlik"])
    writer.writeheader()
    writer.writerows(unique)

print("CSV kaydedildi: turkce_sarki_lexicon.csv")