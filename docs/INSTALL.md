# Kurulum Rehberi

Bu rehber yalnızca Snapmaker U1 için hazırlanmıştır. Başlamadan önce [sorumluluk reddini](../DISCLAIMER.md) okuyun.

## Hızlı kurulum

> [!NOTE]
> Türkçe firmware henüz kurulmadığı için aşağıdaki menü adları yazıcıda göreceğiniz İngilizce biçimiyle verilmiştir.

1. Yazıcınızın kanalına ve taban sürümüne uygun `.bin` dosyasını [Releases](../../../releases) sayfasından indirin ve release notundaki tam SHA-256 değeriyle doğrulayın.
2. Dosyayı **FAT32** biçimli USB belleğin kök dizinine kopyalayın. Bellekte yalnızca yükleyeceğiniz tek firmware `.bin` dosyasını bırakın ve belleği yazıcıya takın.
3. **Settings → About** bölümünü açın ve **Firmware Version** satırına dokunun.
4. Sağ üstteki **Local Update** seçeneğine girin.
5. USB bellekteki `.bin` dosyasını seçip güncellemeyi onaylayın.
6. Güncelleme tamamlanıp yazıcı yeniden başlayana kadar gücü kesmeyin ve USB belleği çıkarmayın.
7. Yeniden başlatmanın ardından **Settings** içindeki dil ayarını açıp **Türkçe** seçeneğini etkinleştirin.

### Resimli anlatım

<details>
<summary><strong>5 adımlı resimli kurulum anlatımını göster</strong></summary>

#### Görsel 1 — `Settings`

Ana ekranda sol taraftaki **Settings** simgesine dokunun.

<p align="center"><img src="images/installation/01-settings.jpg" alt="Ana ekranda Settings simgesini gösteren kırmızı ok" width="480"></p>

#### Görsel 2 — `About`

**Settings** ekranında **About** satırını seçin.

<p align="center"><img src="images/installation/02-about.jpg" alt="Settings ekranında About satırını gösteren kırmızı ok" width="480"></p>

#### Görsel 3 — `Firmware Version`

**About** ekranında **Firmware Version** satırına dokunun.

<p align="center"><img src="images/installation/03-firmware-version-redacted.png" alt="About ekranında Firmware Version satırını gösteren kırmızı ok" width="480"></p>

Gizlilik amacıyla bu görseldeki cihaz seri numarası kapatılmıştır.

#### Görsel 4 — `Local Update`

**Firmware Version** ekranında sağ üstteki **Local Update** düğmesini seçin.

<p align="center"><img src="images/installation/04-local-update.jpg" alt="Firmware Version ekranında Local Update düğmesini gösteren kırmızı ok" width="480"></p>

#### Görsel 5 — Firmware paketini seçin

Cihaz kanalınıza ve taban sürümünüze uygun, SHA-256 değerini doğruladığınız `.bin` dosyasını seçip güncellemeyi onaylayın.

<p align="center"><img src="images/installation/05-select-package.jpg" alt="USB bellekteki firmware paketleri arasından doğru dosyayı seçme ekranı" width="480"></p>

> [!WARNING]
> Örnek görselde birden fazla Stock ve Extended paketi birlikte görünmektedir. Gerçek kurulumda USB bellekte yalnızca yükleyeceğiniz tek doğrulanmış `.bin` dosyasını bırakın. Stock ve Extended kanallarını veya farklı taban sürümlerini karıştırmayın.

</details>

## Ayrıntılı ve güvenli kurulum

### 1. Doğru paketi seçin

1. Yazıcının mevcut firmware sürümünü **Settings → About → Firmware Version** ekranından not edin.
2. Cihazınızın **Snapmaker Stock** mı yoksa **Extended** kanalında mı olduğunu kesinleştirin.
3. [Releases](../../../releases) sayfasından yalnızca aynı kanal ve belirtilen taban sürüm için hazırlanmış Türkçe paketi indirin.
4. Release notunda fiziksel cihaz testi durumunu kontrol edin. Fiziksel test yapılmadıysa bunu değerlendirerek devam edin.

> [!WARNING]
> Stock → Extended veya Extended → Stock geçişi basit bir dil güncellemesi değildir. Release notu açıkça desteklediğini söylemedikçe bu rehberi kanal değiştirmek için kullanmayın. Farklı sürümlerin benzer dosya adlarına sahip olması uyumlu oldukları anlamına gelmez.

### 2. Dosyayı doğrulayın

İndirdiğiniz `.bin` dosyasının SHA-256 değerini **yüklemeden önce** hesaplayın. Sonucun release notundaki tam 64 karakterlik değerle birebir aynı olması gerekir.

Komutlar ve uyuşmazlık durumunda yapılacaklar için [Doğrulama rehberine](VERIFY.md) bakın. Doğrulama başarısızsa kuruluma devam etmeyin.

### 3. Yazıcıyı hazırlayın

- Devam eden baskıyı bitirin.
- Mümkünse cihaz ayarlarını ve ihtiyaç duyduğunuz verileri yedekleyin.
- Güncelleme boyunca kesilmeyecek kararlı bir güç kaynağı kullanın.
- Yazıcının doğru model ve mevcut sürüm bilgisini tekrar kontrol edin.
- Release notunda belirtilen özel ön koşullar varsa uygulayın.

### 4. USB belleği hazırlayın

USB belleği biçimlendirmek üzerindeki verileri siler; gerekli dosyaları önce başka yere kopyalayın.

1. Güvenilir bir USB belleği **FAT32** olarak biçimlendirin. Yazıcınız FAT32 belleği algılamıyor ve cihazınız destekliyorsa **exFAT** deneyin.
2. Doğruladığınız `.bin` dosyasını belleğin kök dizinine kopyalayın.
3. Karışıklığı önlemek için bellekte yalnızca yükleyeceğiniz tek firmware `.bin` dosyasını bırakın.
4. Dosyayı release notunda aksi yazmadıkça yeniden adlandırmayın.
5. Yazma işlemi tamamlandıktan sonra USB belleği işletim sisteminden güvenli biçimde çıkarın.

### 5. Yerel güncellemeyi başlatın

Türkçe firmware henüz kurulmadığı için menü adları cihazda göründüğü İngilizce biçimiyle verilmiştir.

1. USB belleği Snapmaker U1'e takın.
2. Dokunmatik ekranda **Settings → About** bölümünü açın.
3. **Firmware Version** satırına dokunun.
4. Sağ üstteki **Local Update** seçeneğine girin.
5. Ekranda gösterilen dosya adının indirdiğiniz ve doğruladığınız paketle aynı olduğunu kontrol edin.
6. Dosyayı seçin, güncellemeyi onaylayın ve ekrandaki talimatları izleyin.
7. İşlem tamamlanıp cihaz yeniden başlayana kadar gücü kesmeyin, USB belleği çıkarmayın ve ek bir güncelleme başlatmayın.

### 6. Kurulumu kontrol edin

1. Cihaz tamamen açıldıktan sonra firmware sürümünü kontrol edin.
2. **Settings** içindeki dil ayarını açın ve ayrı seçenek olarak görünen **Türkçe** dilini seçin.
3. Ana ekran, ayarlar ve uyarı ekranlarında metinlerin düzgün görüntülendiğini kontrol edin.
4. Temel cihaz durumlarını gözden geçirin; beklenmedik bir davranış varsa baskıya başlamadan önce sorunu araştırın.

### Güncelleme kabul edilmezse

- Aynı dosyayı tekrar tekrar yüklemeye çalışmayın.
- Cihaz modelini, Stock/Extended kanalını, taban sürümü ve tam dosya adını yeniden kontrol edin.
- SHA-256 değerini yeniden hesaplayın.
- USB belleği FAT32 olarak yeniden hazırlayın; cihazın desteklediğinden eminseniz exFAT'i deneyin.
- Başka bir güvenilir USB bellek deneyin.

Cihaz açılmıyorsa rastgele firmware veya kurtarma komutları kullanmayın. Resmî Snapmaker kurtarma/destek belgelerini izleyin ve sorun bildiriminize kullandığınız dosya adı, SHA-256, önceki sürüm ile ekrandaki hata bilgisini ekleyin.
