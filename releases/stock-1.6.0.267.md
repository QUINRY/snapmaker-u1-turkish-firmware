# Snapmaker U1 Stock 1.6.0.267 — Türkçe

Bu paket, Snapmaker U1'in **resmî Stock 1.6.0.267** firmware'i temel alınarak hazırlanmış Türkçe yerelleştirmedir. Ücretsiz, kâr amacı gütmeyen ve resmî olmayan bir topluluk çalışmasıdır; Snapmaker tarafından geliştirilmiş, desteklenmiş veya onaylanmış değildir.

## Doğru paket ve taban

- Kanal: **Stock / resmî firmware tabanlı**
- Taban firmware: `U1_1.6.0.267_20260815150420_upgrade.bin`
- Taban SHA-256: `9F446819E51A2E7A2F0516FDE0C025F2B1CD9C23396301E0F5C45E7859CD8AF4`
- UPFILE sürümü: `1.6.0.267`
- Derleme tarihi alanı: `20260815150420`
- Release asset: `TURKISH_QUINRY_U1_1.6.0.267_20260815150420_upgrade.bin`
- Asset boyutu: `279016192` bayt
- Asset SHA-256: `A8483C8B9909FC527904461F8521FA7D4D91780FC718343C6C89E7999D5197E5`

Bu asset yalnız **Stock 1.6.0.267** tabanı içindir. Extended 1.5.2 veya Extended 1.4.1 paketleriyle karıştırmayın. İndirme tamamlandıktan sonra dosya özetini `SHA256SUMS.txt` veya `manifests/stock-1.6.0.267.json` ile doğrulayın.

## Türkçe yerelleştirme

- Mevcut altı dil değiştirilmeden yedinci dil olarak `tr-TR` / `Türkçe` eklendi.
- 550 ana arayüz ve 458 hata kaydı, yalnız bu sürümün İngilizce kaynakları esas alınarak çevrildi.
- Türkçe karakterler UTF-8, NFC ve BOM'suz biçimde kullanıldı.
- 1.6.0'ın harici hata kataloğu yapısına uygun `exception_tr-TR.json` eklendi.

## Doğrulama

- UPFILE başlık checksum'u ve dört bölüm MD5'i geçti.
- RKFW son ASCII MD5 ve RKAF CRC kontrolleri geçti.
- Paket UPFILE → RKFW → RKAF → SquashFS olarak temiz bir klasöre yeniden açıldı.
- Kaynaktan farklı olması beklenmeyen MCU, loader, boot, U-Boot, misc, OEM ve userdata bileşenleri birebir korundu.
- Final GUI bağımsız doğrulamada `80/80 PASS` aldı; Türkçe seçim, enum, kalıcı ayar ve hata kataloğu yolları denetlendi.
- Rootfs karşılaştırması yalnız Türkçe hata kataloğu ile değiştirilmiş GUI içeriğini gösterdi. Araç kaynaklı seyrek-inode gösterim farklarında dosya SHA-256 değerleri değişmedi.

## Risk ve test durumu

Bu yayın için rapora kaydedilmiş fiziksel Snapmaker U1 flash, açılış veya gerçek ekran yerleşim testi **yoktur**. Paket statik, emüle edilmiş ve katman katman bütünlük kontrollerinden geçmiştir; bu kontroller fiziksel cihaz testinin yerini tutmaz. Firmware yükleme işlemi başarısız olursa cihaz kurtarma işlemi gerekebilir. Yükleme kararı ve sonuçları kullanıcı sorumluluğundadır; işlem sırasında güç kesilmemesini sağlayın.

## Lisans ve marka notu

Bu projenin özgün çeviri, araç ve belgeleri `GPL-3.0-only` kapsamında sunulur. Firmware içindeki Snapmaker ve diğer üçüncü taraf bileşenler kendi lisans ve telif koşullarına tabidir. Snapmaker adı yalnız uyumluluğu belirtmek amacıyla kullanılmıştır.
