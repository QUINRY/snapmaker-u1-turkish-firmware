# İndirme Doğrulama Rehberi

SHA-256 kontrolü, indirdiğiniz firmware dosyasının yayınlanan dosyayla bit düzeyinde aynı olup olmadığını gösterir. Bu kontrol cihaz uyumluluğunu, üçüncü taraf lisanslarını veya firmware'in üretici tarafından imzalandığını tek başına kanıtlamaz.

## Beklenen değeri bulun

1. Paketi indirdiğiniz [release sayfasını](../../../releases) açın.
2. Seçtiğiniz dosyanın tam adını ve tam **64 karakterlik SHA-256** değerini bulun.
3. Varsa aynı release içindeki `.sha256`/checksum dosyasını da indirin.

Kısaltılmış (`ABCD…1234` gibi) bir özetle doğrulama yapmayın. Büyük/küçük harf farkı önemli değildir; 64 onaltılık karakterin tamamı aynı olmalıdır.

## Windows PowerShell

PowerShell'i indirilen dosyanın bulunduğu klasörde açın:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath ".\DOSYA_ADI.bin"
```

`Hash` sütunundaki sonucu release notundaki değerle karşılaştırın. Dosya adında boşluk varsa tırnakları koruyun.

## Manifest ile otomatik doğrulama

Python 3 kuruluysa depodaki doğrulama aracını ilgili manifest ve firmware dosyasıyla çalıştırabilirsiniz:

```sh
python tools/verify_release.py manifests/stock-1.6.0.267.json "TURKISH_QUINRY_U1_1.6.0.267_20260815150420_upgrade.bin"
```

Araç dosya adını, byte boyutunu ve SHA-256 değerini birlikte denetler. Yalnız `PASS` sonucu alındığında kuruluma devam edin.

## macOS

Terminal'i açın ve indirme klasörüne geçtikten sonra çalıştırın:

```sh
shasum -a 256 "DOSYA_ADI.bin"
```

İlk sütundaki sonucu release notundaki değerle karşılaştırın.

## Linux

Terminal'i açın ve indirme klasörüne geçtikten sonra çalıştırın:

```sh
sha256sum "DOSYA_ADI.bin"
```

İlk sütundaki sonucu release notundaki değerle karşılaştırın.

## Sonuç eşleşmiyorsa

Firmware'i **yüklemeyin**.

1. Dosyanın seçtiğiniz hedef release ve hedef Stock/Extended kanalından geldiğini kontrol edin.
2. Eksik/yarım indirmeyi silip release sayfasından yeniden indirin.
3. SHA-256 değerini tekrar hesaplayın.
4. Release notunda yayımlanan dosya boyutuyla yerel dosya boyutunu da karşılaştırın.
5. İkinci indirme de uyuşmuyorsa release altında issue açın; uyuşmayan dosyayı cihaza vermeyin.

## Kurulumdan önce son kontrol

- Cihaz modeli: Snapmaker U1
- Hedef kanal: kurmak istediğiniz Stock veya Extended release
- Hedef sürüm: release notuyla birebir uyumlu
- Dosya adı: doğru release eki
- Dosya boyutu: release notuyla uyumlu
- SHA-256: tam 64 karakter birebir eşleşiyor
- Fiziksel test kapsamı: release notundan okundu; flash/boot/Türkçe arayüz smoke testi ile tam regresyonun farklı olduğu anlaşıldı

Bu maddelerden biri belirsizse kurulumu erteleyin.
