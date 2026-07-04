---
layout: default
title: "SO-101 + Hashtag Robotic Studio Kullanım Kılavuzu"
description: "Hashtag Robotics SO-101 robot kolu ve Hashtag Robotic Studio dashboard için GitHub Pages uyumlu başlangıç, güvenlik, kayıt, eğitim ve agent operasyon kılavuzu."
permalink: /tutorials/so101-studio/
lang: tr
---

# SO-101 + Hashtag Robotic Studio Kullanım Kılavuzu

<figure class="tutorial-hero">
  <img src="{{ '/assets/leader-follower.jpg' | relative_url }}" alt="SO-101 leader ve follower robot kolları" loading="eager">
  <figcaption>SO-101 leader + follower seti, Hashtag Robotic Studio ile yerel dashboard üzerinden kuruluma hazırlanır.</figcaption>
</figure>

Bu kılavuz, Hashtag Robotics SO-101 robot kolunu Hashtag Robotic Studio ile kullanmak isteyen kullanıcı için hazırlanmıştır. Hedef, robotu güvenli şekilde tanımak, dashboard durumlarını okumak, API key ayarlarını yapmak, dataset kaydetmek, Hugging Face üzerinde model eğitimi hazırlamak ve agent modunu kontrollü kullanmaktır.

> Fiziksel hareket başlatma, teleop, dataset kaydı, real rollout ve kalibrasyon yazma işlemleri her zaman SafetyGate, kullanıcı unlock, süre limiti ve acil stop doğrulamasına bağlıdır. Bu doküman tek başına robotu hareket ettirme yetkisi vermez.

## 1. Bu kılavuz neyi kapsıyor?

Bu sayfa GitHub Pages üzerinde tek Markdown sayfası olarak yayınlanabilecek şekilde yazıldı. Daha sonra `labs.hashtagworldcompany.com` temasına taşınırken aynı başlıklar, görseller ve video yolları korunabilir.

Kapsam:

- SO-101 leader/follower mimarisi.
- Hashtag Robotic Studio dashboard ekranları.
- İlk bağlantı öncesi güvenlik kontrolü.
- API key vault: Hugging Face, agent LLM sağlayıcıları, GitHub, W&B, AWS ve Custom MCP.
- LeRobot uyumlu dataset kayıt akışı.
- Hugging Face üzerinde policy eğitimi hazırlığı.
- Policy uyumluluk kontrolü ve real rollout kapısı.
- Agent operasyon modu ve tool izinleri.
- Tanılama, support bundle ve sorun giderme.

Kapsam dışı:

- Gerçek motor hareketi başlatan komutları otomatik çalıştırma.
- Kalibrasyon dosyasını otomatik yazma.
- Kullanıcı onayı olmadan Hub upload, model download veya uzun training job başlatma.
- Üretim robotu güvenlik sertifikasyonu.

## 2. SO-101 nedir?

SO-101, LeRobot ekosistemiyle uyumlu masaüstü robot kol platformudur. Hashtag Robotics ürün sayfasındaki paket yaklaşımı, leader + follower setinin kurulu ve test edilmiş şekilde gelmesi üzerine kuruludur. Follower görev yapan koldur; leader ise operatörün elle yönlendirdiği kontrol koludur. Bu ikili yapı teleoperasyon, dataset toplama ve imitation learning için kullanılır.

Hashtag Robotics paketindeki temel donanım profili:

- 5 DOF + paralel gripper.
- 6 adet Feetech STS3215 seri bus servo.
- USB-C seri bus bağlantısı.
- 12V + 5V güç hattı.
- 3D baskı PLA/PETG gövde.
- Leader + follower kullanım modeli.
- LeRobot Python ekosistemiyle uyumlu yazılım akışı.
- Opsiyonel wrist ve scene kamera seti.

<figure>
  <img src="{{ '/assets/hero-follower.webp' | relative_url }}" alt="SO-101 follower robot kol" loading="lazy">
  <figcaption>Follower kol, görevleri yapan fiziksel robot tarafıdır.</figcaption>
</figure>

## 3. İlk açılış: dashboard mantığı

Hashtag Robotic Studio yerel çalışan bir robot cockpit uygulamasıdır. Dashboard, robotu hareket ettirmek için değil, önce robotun durumunu okumak ve riskli işlemleri kapılamak için açılır.

Ana ekranların görevi:

| Ekran | Kullanım amacı |
| --- | --- |
| Başlangıç | Gateway, follower, leader, kamera, kalibrasyon ve SafetyGate durumunu tek bakışta gösterir. |
| Cihazlar | USB port adayları, kamera adayları ve güvenli kullanım durumunu listeler. |
| Kalibrasyon | Kalibrasyon dosyalarını ve yazma kilidini gösterir. |
| Canlı Kontrol | Teleop hazırlığı, kamera preview ve operation template durumunu gösterir. |
| Kayıt | LeRobot uyumlu dataset kayıt planını hazırlar. |
| Datasetler | Episode sayısı, FPS, kamera keyleri ve kalite blokajlarını gösterir. |
| Policyler | Hugging Face training ayarı ve policy compatibility raporunu gösterir. |
| Agent | Agent tool izinlerini ve dry-run operasyon planını yönetir. |
| Tanılama | Gateway, inventory, policy ve masked secret durumunu destek için özetler. |
| Ayarlar | API key vault ve secret storage durumunu yönetir. |

Başlangıç ekranındaki readiness skoru bir izin sistemi değildir; sadece hazırlık göstergesidir. Real rollout izni ayrıca SafetyGate tarafından verilir.

## 4. İlk bağlantı öncesi güvenlik kontrolü

Robotu güç vermeden ve USB bağlamadan önce:

1. Robot tabanını sabit bir masaya yerleştir.
2. Follower kolun tüm çalışma hacmini boş bırak.
3. Güç adaptörü ve USB kablolarının kola takılmayacağını kontrol et.
4. Acil stop veya güç kesme yolunu fiziksel olarak erişilebilir tut.
5. Leader ve follower rollerini karıştırma; portları dashboard üzerinde aday olarak görmeden varsayım yapma.
6. Kamera takılı değilse bu bloklayıcı değildir; kamera olmayan observation-only akış desteklenir, fakat kayıt ve policy mapping daha sonra kamera keylerine ihtiyaç duyabilir.

Studio tarafında ilk kontrol:

- `Gateway` durumu `Bagli` olmalı.
- `Follower port` en az bir aday göstermeli.
- `Kalibrasyon` follower için mevcut görünmeli.
- `E-stop` manuel olarak doğrulanmalı.
- Fiziksel hareket gereken her operasyon için `duration_limit`, `emergency_stop` ve `workspace_clear` alanları tamamlanmalı.

Kalibrasyon dosyasını yazma veya üzerine yazma, açık kullanıcı onayı, robot rol doğrulaması ve backup olmadan yapılmaz.

## 5. API key vault ve model eğitimi

Model eğitimi ve agent özellikleri için API keyler Ayarlar ekranındaki API key vault üzerinden bağlanır. Uygulama secret değerlerini response, tanılama logu veya support bundle içinde göstermemelidir; ekranda sadece bağlı/bağlı değil durumu ve son dört karakter gibi masked bilgiler görünür.

Desteklenen provider matrisi:

| Provider | Ne için kullanılır? | Not |
| --- | --- | --- |
| Hugging Face | Dataset upload, remote training, model download | SO-101 model eğitimi için ana sağlayıcı. |
| OpenAI | Agent LLM | Robot tool planlama ve açıklama yüzeyleri için. |
| Anthropic | Agent LLM | Alternatif agent LLM sağlayıcısı. |
| Google Gemini | Agent LLM | Alternatif agent LLM sağlayıcısı. |
| GitHub | Issue sync, release notes | Dokümantasyon ve destek akışları için. |
| Weights & Biases | Training tracking | Deney takibi için. |
| AWS | Artifact storage | Büyük çıktı ve checkpoint saklama için. |
| Custom MCP Gateway | Tool connectors | Harici tool sistemleri için. |

Hugging Face token bağlanmadan Studio training hazırlığını tamamlanmış saymaz. Token için pratik kural:

- Dataset upload ve model repo push gerekiyorsa write yetkisi gerekir.
- Sadece model indirme gerekiyorsa read yetkisi yeterli olabilir.
- Token hiçbir zaman tutorial, issue, log veya support bundle içine yazılmaz.

## 6. Cihaz eşleştirme

Cihazlar ekranı robotu doğrudan hareket ettirmez. Sadece envanter okur ve adayları gösterir:

- USB/serial port adayları.
- Kamera adayları.
- Kalibrasyon dosyası adayları.
- Paket ve SDK görünürlüğü.

LeRobot resmi SO-101 dokümanlarında port bulma, follower setup, leader setup ve kalibrasyon akışları ayrı adımlar olarak anlatılır. Studio bu adımları ürün yüzeyine taşırken şu kuralı korur: port adayını görmek, portun güvenli şekilde kullanılacağı anlamına gelmez. Follower/leader rolü doğrulanmadan ve kalibrasyon eşleşmeden fiziksel hareket başlatılmaz.

## 7. Veri kaydı

Dataset kaydı fiziksel hareket sayılır. Kayıt ekranı önce plan hazırlar:

- Task metni: örnek `nesneyi kutuya yerlestir`.
- Dataset repo/path: örnek `mert/so101-demo`.
- Episode süresi.
- FPS.
- Kamera keyleri: örnek `observation.images.front`, `observation.images.wrist`.
- Leader/follower mapping.
- Kalibrasyon ID.
- Acil stop ve süre limiti.

LeRobot imitation learning akışı tipik olarak üç ana parçadan oluşur: dataset kaydı, policy eğitimi ve policy değerlendirme. Studio bu akışı dashboard ekranlarına böler:

1. Cihaz ve kalibrasyon doğrulanır.
2. Kayıt planı hazırlanır.
3. Kullanıcı fiziksel hareket için unlock verir.
4. Episode kayıtları kalite kontrol ekranında incelenir.
5. Dataset upload ancak açık kullanıcı aksiyonuyla yapılır.

Kalite kontrol sırasında özellikle şunlara bak:

- Episode sayısı beklenen kadar mı?
- FPS tutarlı mı?
- Kamera keyleri policy training ile aynı mı?
- Bozuk frame, eksik observation veya yarım kalmış episode var mı?
- Task metni her episode için aynı davranışı mı tarif ediyor?

## 8. Hugging Face üzerinde eğitim

Studio tarafında model eğitimi Policyler ekranından hazırlanır. Bugünkü ürün yönü, eğitimi Hugging Face tarafında veya yerel GPU hedefinde başlatmaya uygun bir plan üretmektir. Eğitim işi uzun sürebileceği ve dış kaynak kullanabileceği için otomatik başlatılmamalıdır.

Minimum eğitim hazırlığı:

- Hugging Face API key bağlı.
- Dataset repo/path doğrulanmış.
- Dataset kalite kontrolü tamamlanmış.
- Policy family seçilmiş: örnek ACT, Diffusion Policy, SmolVLA.
- Output model repo belirlenmiş.
- Training tracking gerekiyorsa W&B key bağlı.
- Compute hedefi seçilmiş.

ACT gibi imitation learning policy aileleri robot state, action ve kamera observation şemalarına duyarlıdır. Policy training öncesi feature mapping şu alanları eşleştirmelidir:

- `expected_image_keys`
- `expected_state_features`
- `expected_action_dimension`
- `camera_keys`
- `state_features`
- `action_dimension`
- unit conversion durumu

Training tamamlandıktan sonra checkpoint doğrudan real rollout'a gitmez. Önce compatibility raporu, sonra simülasyon veya dry-run, sonra kısa süreli ve kullanıcı unlock gerektiren fiziksel evaluation gerekir.

## 9. Policy compatibility ve real rollout kapısı

Policy compatibility ekranı, seçilen checkpoint'in robot runtime ile uyumlu olup olmadığını gösterir. Real rollout aşağıdaki durumlarda bloklu kalmalıdır:

- Policy checkpoint seçilmemişse.
- Remote code trust açıkça verilmemişse.
- Kamera mapping doğrulanmamışsa.
- Action dimension beklenen robot action boyutuyla uyuşmuyorsa.
- Unit conversion doğrulanmamışsa.
- Kalibrasyon veya follower port belirsizse.
- SafetyGate fiziksel hareketi kapatmışsa.

Real rollout için minimum operation contract:

```yaml
type: run_real_policy
mode: real
safety_level: physical_motion
required_inputs:
  - follower_port
  - calibration_id
  - policy_checkpoint
  - feature_mapping
  - duration_limit
  - emergency_stop
  - workspace_clear
```

Bu contract eksikse dashboard `Ready` görünse bile real rollout başlamaz.

## 10. Agent operasyon modu

Agent ekranı robotu serbest şekilde kontrol eden bir sohbet kutusu değildir. Agent yalnızca açık tool sözleşmeleri üzerinden çalışır.

Güvenli tool ayrımı:

| Tool tipi | Örnek | Hareket var mı? | Varsayılan |
| --- | --- | --- | --- |
| Diagnostic | `diagnose_setup` | Yok | Açık |
| Simulation | `simulate_policy` | Yok | Açık |
| Physical request | `request_teleop_session` | Kullanıcı unlock sonrası | Kapalı |
| Physical control | `run_real_policy` | Evet | Kapalı |

Agent için doğru kullanım:

- "Robotu incele, eksik bağlantıları raporla."
- "Dataset kaydı için blokajları listele."
- "Bu policy neden real rollout'a hazır değil?"
- "Teleop için gerekli operation contract taslağını hazırla."

Agent için yanlış kullanım:

- "Robotu hemen hareket ettir."
- "Kalibrasyonu otomatik yaz."
- "Policy'yi gerçek kolda dene, onay sorma."

Agent fiziksel hareketi bypass edemez. SafetyGate, operation contract, süre limiti ve kullanıcı unlock deterministik sistemde kalır.

## 11. Tanılama ve support bundle

Tanılama ekranı destek için gerekli teknik bilgileri toplar:

- Gateway health.
- Inventory.
- Dataset ve policy özetleri.
- Agent tool durumları.
- API key provider bağlantı durumları.
- Son olaylar.

Support bundle içine secret değerleri konmaz. API key için sadece provider, bağlı/bağlı değil ve masked son karakter bilgisi gibi güvenli alanlar kullanılmalıdır.

Sorun giderme tablosu:

| Belirti | Muhtemel neden | İlk aksiyon |
| --- | --- | --- |
| Gateway bekleniyor | Local gateway çalışmıyor | Gateway'i başlat, `/health` durumunu kontrol et. |
| Port adayı yok | USB kablo, güç veya driver görünmüyor | Kablo/güç kontrolü yap, port adaylarını yenile. |
| Kamera yok | Kamera takılı değil veya izin yok | Kamera olmadan observation-only devam et, kayıt için sonra mapping yap. |
| Kalibrasyon eksik | Robot ID eşleşmedi veya dosya yok | Mevcut dosyayı kontrol et; overwrite yapma. |
| HF token bağlı değil | Training/upload için token yok | Ayarlar ekranından Hugging Face key ekle. |
| Real rollout bloklu | Policy mapping veya SafetyGate eksik | Policy compatibility blocker listesini tek tek çöz. |
| Support bundle secret içeriyor şüphesi | Yanlış logging | Bundle üretimini durdur, secret alanlarını temizle. |

## 12. GitHub Pages medya planı

Bu tutorial şu medya yollarını bekler. Website entegrasyonu sırasında dosyalar ilgili `assets/` klasörlerine kopyalanabilir.

| Tutorial yolu | Lokal kaynak |
| --- | --- |
| `/assets/hero-follower.webp` | `/Users/macmert/hashtag-robotic/labs-redesign/assets/hero-follower.webp` |
| `/assets/leader-follower.jpg` | `/Users/macmert/hashtag-robotic/labs-redesign/assets/leader-follower.jpg` |
| `/assets/leader.webp` | `/Users/macmert/hashtag-robotic/labs-redesign/assets/leader.webp` |
| `/assets/part-servo.jpg` | `/Users/macmert/hashtag-robotic/labs-redesign/assets/part-servo.jpg` |
| `/assets/part-board.png` | `/Users/macmert/hashtag-robotic/labs-redesign/assets/part-board.png` |
| `/assets/anatomy/Joint1.mp4` | `/Users/macmert/hashtag-robotic/hashtag-robotics-montaj-animasyon/web/Joint1.mp4` |
| `/assets/anatomy/Joint2.mp4` | `/Users/macmert/hashtag-robotic/hashtag-robotics-montaj-animasyon/web/Joint2.mp4` |
| `/assets/anatomy/Joint3.mp4` | `/Users/macmert/hashtag-robotic/hashtag-robotics-montaj-animasyon/web/Joint3.mp4` |
| `/assets/anatomy/Joint4.mp4` | `/Users/macmert/hashtag-robotic/hashtag-robotics-montaj-animasyon/web/Joint4.mp4` |
| `/assets/anatomy/Joint5.mp4` | `/Users/macmert/hashtag-robotic/hashtag-robotics-montaj-animasyon/web/Joint5.mp4` |
| `/assets/anatomy/Gripper.mp4` | `/Users/macmert/hashtag-robotic/hashtag-robotics-montaj-animasyon/web/Gripper.mp4` |

GitHub Pages uyumlu video örneği:

```html
<figure class="tutorial-video">
  <video controls preload="metadata" poster="{{ '/assets/anatomy/Joint1.jpg' | relative_url }}">
    <source src="{{ '/assets/anatomy/Joint1.mp4' | relative_url }}" type="video/mp4">
  </video>
  <figcaption>Taban ekseni montaj animasyonu.</figcaption>
</figure>
```

Birden fazla büyük video aynı sayfaya konacaksa `preload="metadata"` kullanılmalı. Autoplay zorunlu değil; tutorial sayfasında kullanıcı kontrollü oynatma daha doğru.

## 13. Lab kullanıcıları için komut eşdeğerleri

Studio nihai kullanıcı yüzeyi olsa da, mühendislik ve lab ortamında LeRobot komutları referans alınır. Aşağıdaki örnekler öğreticidir; port, robot id, kamera keyi ve dataset adı doğrulanmadan çalıştırılmamalıdır.

Port adaylarını bulma:

```bash
lerobot-find-port
```

Follower veya leader kurulumunda port ve robot id değerleri LeRobot SO-101 dokümanındaki akışa göre seçilmelidir. Gerçek teleop komutu fiziksel hareket sayılır; başlamadan önce follower port, leader port, calibration id, süre limiti, acil stop ve çalışma alanı doğrulanmalıdır.

Dataset kaydı için lab prensibi:

```bash
# Örnek iskelet; gerçek değerleri dashboard ve LeRobot dokümanına göre doldur.
lerobot-record \
  --robot.type=so101_follower \
  --robot.id=<follower_id> \
  --robot.port=<follower_port> \
  --teleop.type=so101_leader \
  --teleop.id=<leader_id> \
  --teleop.port=<leader_port> \
  --dataset.repo_id=<hf_user>/<dataset_name> \
  --dataset.num_episodes=<episode_count> \
  --dataset.single_task="<task_text>"
```

Hugging Face authentication:

```bash
hf auth login
```

Studio ürün yüzeyinde bu komutlar doğrudan kopyala-çalıştır yerine, güvenli form alanları ve operation contract üzerinden hazırlanmalıdır.

## 14. Kaynaklar

Bu kılavuz hazırlanırken ürün sayfası, yerel website assetleri ve resmi/ana kaynaklar referans alındı:

- Hashtag Robotics SO-101 ürün sayfası: <https://labs.hashtagworldcompany.com/product>
- Hugging Face LeRobot SO-101 dokümantasyonu: <https://huggingface.co/docs/lerobot/en/so101>
- Hugging Face LeRobot imitation learning robot tutorial: <https://huggingface.co/docs/lerobot/en/il_robots>
- Hugging Face LeRobot ACT policy dokümantasyonu: <https://huggingface.co/docs/lerobot/en/act>
- Hugging Face LeRobotDataset v3 dokümantasyonu: <https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3>
- Hugging Face LeRobot GitHub repository: <https://github.com/huggingface/lerobot>
- TheRobotStudio SO-ARM100 / SO-101 kaynak projesi: <https://github.com/TheRobotStudio/SO-ARM100>

