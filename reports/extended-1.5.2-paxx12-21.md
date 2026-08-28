# Snapmaker U1 Türkçe UTF-8 Firmware Derleme Raporu

## Teslim dosyası

- Dosya: `U1_extended_1.5.2-paxx12-21_TR_UTF8_upgrade.bin`
- Boyut: `259859532` bayt
- SHA-256: `6EFE052669494B91801139C426C17E85DEE212EAF32E3F891F01AAAE7C033086`
- UPFILE sürümü: `1.5.2.132a88932`
- UPFILE derleme tarihi: `20260722102206`

Kaynak firmware ve önceki ASCII Türkçe teslimi değiştirilmedi:

- Kaynak: `U1_extended_1.5.2-paxx12-21_upgrade.bin`; SHA-256: `F85BBD0FC15FC4029ABB7EE15B5D61805AA16E47C9D4B5AA1289204D42835C0E`
- ASCII Türkçe: `U1_extended_1.5.2-paxx12-21_TR_upgrade.bin`; SHA-256: `946C237BEF593A30021120B01A78B06104244BAE488BF50E7A4A7E623226DF19`

## Türkçe dil yapısı

Türkçe, mevcut dillerden hiçbiri değiştirilmeden yedinci dil olarak eklendi.

- Dil kodu: `tr-TR`
- Menü etiketi: `Türkçe`
- Kodlama ve normalizasyon: UTF-8, NFC, BOM yok
- Ana metin: `530` kayıt
- Hata metni: `446` kayıt
- `main.json` SHA-256: `6FB01108BC1678AF325C48098043FE6D7C9E43DF922089389FC8C105A4B4F8C1`
- `errors.json` SHA-256: `A133F74173A007E89B4A67F63111FC13908657CC3733C50551E798BAE4430E5D`
- Türkçeye özgü karakter kullanımı: `9910` adet

Placeholder, satır sonu, anahtar sırası, alt çizgi ve sayısal belirteç kontrolleri geçti. Uzun bir düğme etiketi olan `Oturumu Kapat`, doğal ve kısa `Çıkış` olarak düzenlendi; okunaksız harf düşürmeli kısaltma kullanılmadı.

## Font ve yerleşim denetimi

`ç, ğ, ı, ö, ş, ü, Ç, Ğ, İ, Ö, Ş, Ü` karakterlerinin tamamı aşağıdaki beş gömülü fontta `12/12` çizilebilir durumdadır:

- `Roboto-Medium.ttf`
- `Roboto-Bold.ttf`
- `HarmonyOS_Sans_SC_Regular.ttf`
- `NotoSansHebrew-Regular.ttf`
- `barlowsemicondensed-extrabold.ttf`

Ana arayüzdeki `530` metin Roboto Medium 24 px ile ölçüldü. Türkçe karakterli metinlerin ASCII karşılıklarına göre minimum/maksimum genişlik farkı `0.00 px`, genişleyen kayıt sayısı `0` çıktı. Bu nedenle Türkçe karakterlerin kendisi önceki ASCII Türkçe yapıya göre yeni bir taşma üretmiyor.

## GUI yaması

- Patched GUI boyutu: `7960560` bayt
- Patched GUI SHA-256: `F09884406204B747471E140BA3834377346B971BD97643B5813A398EBEACD44C`
- Kaynak GUI SHA-256: `66289CB48445AF7EC678BAD29BB93D1E3112562C3656974838285034B86FDE80`
- Dahili yapısal ve davranışsal doğrulama: `59/59 PASS`
- Mevcut altı dilin descriptor, tablo, anahtar ve değerleri değişmedi.
- Yeni Türkçe descriptor'u, yedinci seçim satırı ve NULL sentinel doğrulandı.
- `tr-TR` seçimi, kalıcı kayıt ve yeniden yükleme yolları doğrulandı.
- ARM64 branch, hook, ADRP, GOT ve RELA hedefleri gerçek çıktı baytları üzerinden doğrulandı.
- Gerçek ARM64 kod yolları Angr/pyvex ile çalıştırıldı.
- Yeni veri segmenti yazılabilir, çalıştırılamaz ve orijinal BSS alanıyla çakışmaz.

Bağımsız ELF ve font çapraz denetimi adayı **KABUL** etti. Denetimde `15352` relocation, yeni segment izinleri, yedinci descriptor/sentinel, selector–event–persistence zinciri ve `976` metnin gerçek font yönlendirmesi tekrar incelendi; eksik glif veya crash/brick göstergesi bulunmadı. `Türkçe` etiketi yaklaşık `55.53 px`, `460 px` seçim satırına rahatça sığıyor. Code-cave ayrı section taşımadığı için GUI üzerinde paketleme sonrasında `strip`, `objcopy` veya `patchelf` çalıştırılmadı ve çalıştırılmamalıdır.

## Paketleme ve sıfırdan açma doğrulaması

- Rootfs: `220336128` bayt; SHA-256 `E732839784645972C68782D6F221E649D9D28756EF689A9BF9DDEA00128D96FE`
- RKAF: `259297284` bayt; SHA-256 `3EA0765E8E6D3FC509FF7A027178E55048D3986AE09B5F4B08BDE96D0DAA6BDD`
- RKFW: `259766858` bayt; SHA-256 `1E9780CDD7B372409488EBF784F0A804894B393CF32460C3109304A67024B48D`
- SquashFS: sürüm `4.0`, gzip, blok `131072`, `12800` inode, `1020` fragment; bölüm sınırı `314572800` bayt
- RKAF CRC ve RKFW son ASCII MD5 değeri doğrulandı.
- UPFILE başlık checksum'u, dört giriş checksum'u ve dört dosya MD5 değeri doğrulandı.
- Teslim `.bin` dosyası boş bir klasöre UPFILE → RKFW → RKAF → SquashFS sırasıyla yeniden açıldı.
- Kaynakla semantik SquashFS karşılaştırmasında yalnız `/usr/bin/gui` farklıdır.
- Son firmware'den çıkarılan GUI'nin SHA-256 değeri patched GUI ile birebir eşleşti ve `59/59` kontrolden tekrar geçti.
- MCU dosyaları, boot, bootloader, uboot, misc, oem, userdata, parameter ve package-file kaynakla SHA-256 olarak aynıdır.

SquashFS yazıcısı `ALWAYS_FRAGMENTS` ve `NO_XATTRS` bilgilendirme bitlerini ayarlar (`flags=0x2e0`). Orijinalde de xattr tablosu yoktur; dosya/metadata karşılaştırması yalnız GUI farkını gösterdi. Superblock elle değiştirilmedi.

## Sınır

Firmware statik, emüle edilmiş ve katman katman yeniden-açma kontrollerinden geçti. Fiziksel Snapmaker U1 üzerinde flash/boot ve gerçek ekran yerleşim testi yapılmadı. Custom firmware flash işlemi her zaman cihaz kurtarma gerektirebilecek bir risk taşır.
