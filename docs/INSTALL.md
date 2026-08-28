# Kurulum Rehberi

Bu rehber yalnızca Snapmaker U1 için hazırlanmıştır. Başlamadan önce [sorumluluk reddini](../DISCLAIMER.md) okuyun.

## 1. Doğru paketi seçin

1. Yazıcının mevcut firmware sürümünü dokunmatik ekrandan not edin.
2. Cihazınızın **Snapmaker Stock** mı yoksa **Extended** kanalında mı olduğunu kesinleştirin.
3. [Releases](../../../releases) sayfasından yalnızca aynı kanal ve belirtilen taban sürüm için hazırlanmış Türkçe paketi indirin.
4. Release notunda fiziksel cihaz testi durumunu kontrol edin. Fiziksel test yapılmadıysa bunu değerlendirerek devam edin.

> [!WARNING]
> Stock → Extended veya Extended → Stock geçişi basit bir dil güncellemesi değildir. Release notu açıkça desteklediğini söylemedikçe bu rehberi kanal değiştirmek için kullanmayın. Farklı sürümlerin benzer dosya adlarına sahip olması uyumlu oldukları anlamına gelmez.

## 2. Dosyayı doğrulayın

İndirdiğiniz `.bin` dosyasının SHA-256 değerini **yüklemeden önce** hesaplayın. Sonucun release notundaki tam 64 karakterlik değerle birebir aynı olması gerekir.

Komutlar ve uyuşmazlık durumunda yapılacaklar için [Doğrulama rehberine](VERIFY.md) bakın. Doğrulama başarısızsa kuruluma devam etmeyin.

## 3. Yazıcıyı hazırlayın

- Devam eden baskıyı bitirin.
- Mümkünse cihaz ayarlarını ve ihtiyaç duyduğunuz verileri yedekleyin.
- Güncelleme boyunca kesilmeyecek kararlı bir güç kaynağı kullanın.
- Yazıcının doğru model ve mevcut sürüm bilgisini tekrar kontrol edin.
- Release notunda belirtilen özel ön koşullar varsa uygulayın.

## 4. USB belleği hazırlayın

USB belleği biçimlendirmek üzerindeki verileri siler; gerekli dosyaları önce başka yere kopyalayın.

1. Güvenilir bir USB belleği **FAT32** olarak biçimlendirin. Yazıcınız FAT32 belleği algılamıyor ve cihazınız destekliyorsa **exFAT** deneyin.
2. Doğruladığınız `.bin` dosyasını belleğin kök dizinine kopyalayın.
3. Karışıklığı önlemek için bellekte yalnızca yükleyeceğiniz tek firmware `.bin` dosyasını bırakın.
4. Dosyayı release notunda aksi yazmadıkça yeniden adlandırmayın.
5. Yazma işlemi tamamlandıktan sonra USB belleği işletim sisteminden güvenli biçimde çıkarın.

## 5. Yerel güncellemeyi başlatın

Menü adları kurulu dile veya sürüme göre biraz değişebilir.

1. USB belleği Snapmaker U1'e takın.
2. Dokunmatik ekranda **Ayarlar → Firmware Güncelleme → Yerel Güncelleme/USB'den Güncelleme** akışını açın.
3. Ekranda gösterilen dosya adının indirdiğiniz ve doğruladığınız paketle aynı olduğunu kontrol edin.
4. Güncellemeyi onaylayın ve ekrandaki talimatları izleyin.
5. İşlem tamamlanıp cihaz yeniden başlayana kadar gücü kesmeyin, USB belleği çıkarmayın ve ek bir güncelleme başlatmayın.

## 6. Kurulumu kontrol edin

1. Cihaz tamamen açıldıktan sonra firmware sürümünü kontrol edin.
2. Dil ayarlarını açın ve ayrı seçenek olarak görünen **Türkçe** dilini seçin.
3. Ana ekran, ayarlar ve uyarı ekranlarında metinlerin düzgün görüntülendiğini kontrol edin.
4. Temel cihaz durumlarını gözden geçirin; beklenmedik bir davranış varsa baskıya başlamadan önce sorunu araştırın.

## Güncelleme kabul edilmezse

- Aynı dosyayı tekrar tekrar yüklemeye çalışmayın.
- Cihaz modelini, Stock/Extended kanalını, taban sürümü ve tam dosya adını yeniden kontrol edin.
- SHA-256 değerini yeniden hesaplayın.
- USB belleği FAT32 olarak yeniden hazırlayın; cihazın desteklediğinden eminseniz exFAT'i deneyin.
- Başka bir güvenilir USB bellek deneyin.

Cihaz açılmıyorsa rastgele firmware veya kurtarma komutları kullanmayın. Resmî Snapmaker kurtarma/destek belgelerini izleyin ve sorun bildiriminize kullandığınız dosya adı, SHA-256, önceki sürüm ile ekrandaki hata bilgisini ekleyin.
