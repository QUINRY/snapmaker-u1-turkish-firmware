# Extended 2.0.0-paxx12-develop-7188aab Türkçe — Derleme raporu

## Kaynak ve çıktı

- Kaynak yayın: [paxx12 rolling](https://github.com/paxx12-snapmaker-u1/SnapmakerU1-Extended-Firmware/releases/tag/rolling)
- Sabit kaynak commit: `7188aab2fc8c671bc467925a0ad8cdea6d8668f1`
- Çeşit: standart Extended; rolling/develop ön sürümü.
- Kaynak dosya: `U1_extended_2.0.0-paxx12-develop-7188aab_upgrade.bin`
- Kaynak boyutu: `250415876` bayt
- Kaynak SHA-256: `FCFDD99CA6D6B4C3B7566BDA625A2C24FF8F7C359A073F151E3E073080647976`
- Türkçe dosya: `TURKISH_QUINRY_U1_extended_2.0.0-paxx12-develop-7188aab_upgrade.bin`
- Türkçe boyutu: `256600836` bayt
- Türkçe SHA-256: `828588305BAA882CBA676A0066D5411174B55C867E0318AEDA4EE1A90C599DCB`
- Korunan UPFILE sürümü/tarihi: `2.0.0.2047188aab` / `20260907182340`

## Çeviri ve ekran uygulaması

Yeni firmware ayrı klasöre açıldı. Yedi dilin kendi tabloları ve hata kaynakları çıkarıldı. 550 ana metnin 13'ü ve 466 hata kaydının 14'ü yeni/değişmiş İngilizce kaynaktan çevrildi. Kalan 989 kayıtta eski Türkçe karşılığın kullanılabilmesi için hem anahtarın hem İngilizce metnin aynı olması şartı doğrulandı. Eski sürümden kaldırılmış anahtarlar yeni tabloya eklenmedi.

Türkçe UTF-8, NFC ve BOM'suzdur. Anahtar sırası, yer tutucular, sayılar, satır sonları, biçimlendirme ve hata ayraçları kontrol edildi. Kaynağın HarmonyOS ve Roboto fontları Türkçe karakterleri kapsar.

- Ana metin SHA-256: `1AD34EE9BD210D15CED0006ADA29BDD663CB086DFAEAE2B615FA9319C973F557`
- Hata metni SHA-256: `E86C7675F698F1F05D4C2EF23154E29A53D679D50052AFD8A27040F6CFC16C20`
- Final GUI SHA-256: `E06CCAFBCC673CF0FAE804D96FCD2D4384AD6AF0819A75CD29FEBC9B3D04B05E`
- Mevcut diller: 7; Türkçe sıra: 8; enum: 7.

2.0.0'daki Fransızca kaydı ve mevcut dil tabloları korundu. Türkçe için genişletilmiş dil kaydı ve sekizinci menü seçeneği oluşturuldu. Sürümün genel `exception_%s.json` yolu kullanılarak `exception_tr-TR.json` eklendi.

## HelixScreen 1.0.0 Türkçe

- Kaynak: [HelixScreen v1.0.0](https://github.com/prestonbrown/helixscreen/releases/tag/v1.0.0), Snapmaker U1 paketi.
- Kaynak arşiv SHA-256: `49c9aae95c1be859ea6d75691f55dc8d69cc0bd679da6cf1d58d9ca14a82844a`.
- 2.868 güncel metin: 23 yeni çeviri, 2.845 birebir anahtar/İngilizce eşleşmesi.
- Mevcut dokuz dil korunur; Türkçe onuncu seçenektir.
- Yerel dil yaması 41/41 kontrolü geçti; on dilin indeks eşleşmeleri, iki ayar menüsü yolu, kurulum sihirbazı tıklamaları ve hoş geldiniz döngüsü kontrollü AArch64 emülasyonunda sınandı.
- Orijinal indirme adresi ve SHA-256 doğrulaması korunur. Türkçe yalnız bu doğrulanmış sürüme uygulanır.
- Kurulumdan sonra ve önceden kurulu uygulamanın açılışında aynı idempotent kurucu kullanılır. Ayarlar değiştirilmez, bilinmeyen sürüm/özelleştirmelere dokunulmaz.
- Kurucu: 12 test geçti; 1 test Windows dosya sembolik bağlantı yetkisi nedeniyle atlandı. Dizin bağlantıları gerçek NTFS junction ile sınandı; POSIX izinleri Windows testlerinde modellendi.
- Orijinal uygulamanın 871 dosyalı yalıtılmış kopyasında gerçek payload kurulumu, tüm dosyaların karşılaştırması ve ikinci çalıştırmanın değişiklik yapmaması doğrulandı. Fiziksel yazıcı testi değildir.
- [Yeniden üretim araçları](https://github.com/QUINRY/snapmaker-u1-turkish-firmware/tree/main/tools/helixscreen-1.0.0-u1) ve Türkçe kaynaklar depoda bulunmaktadır.

## Paketleme ve doğrulama

- SquashFS 4.0 / Zstandard / 131072 bayt blok boyutu korundu.
- Dosya sistemi zamanı: `1789137790`.
- Rootfs: `217075712` bayt; bölüm sınırı `314572800` bayt.
- Rootfs SHA-256: `06026D6C97D4093DE59D729A1D92B13FE7219A07A421E6502E8B9A261A62FD2B`
- RKAF SHA-256: `A5AA7BCE73BAA2AC3AC98AEA53999F7C53CCC93A8698348E4E3BCE176BC6D90B`
- RKFW SHA-256: `51FB3387F7EE610F40ACF8B29DA1818AC1D6ABC58DB5B33AB3A8620B36A539B8`
- SquashFS bayrakları: `0x00c0 → 0x02e0`; bilinen paketleyici bilgilendirme bitleri ayrıca denetlendi.

Kaynağın 13432 TAR girdisi yeniden açılan final dosya sistemiyle karşılaştırıldı. Değişiklikler Snapmaker GUI, Türkçe hata dosyası, iki HelixScreen kurulum bağlantısı ve `/usr/local/share/helixscreen-turkish` kaynaklarıyla sınırlandırıldı; mevcut dosyaların sahiplikleri, izinleri, zamanları ve bağlantıları korundu.

Final `.bin` UPFILE → RKFW → RKAF → SquashFS olarak yeniden açıldı. Başlıklar, bölüm yerleşimi, UPFILE checksum/MD5, RKFW MD5 ve RKAF CRC kontrolleri geçti. MCU, loader ve rootfs dışındaki tüm bölümler kaynakla aynıdır. Çıkarılan GUI ve Türkçe hata dosyası onaylanan dosyalarla birebir eşleşti.

Final GUI **85/85 PASS** aldı. Bu yeni firmware'in fiziksel yazıcıda yükleme/açılış testi henüz bildirilmedi.
