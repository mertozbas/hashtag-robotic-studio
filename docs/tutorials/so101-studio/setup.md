---
layout: default
book: so101
guide_section: setup
title: "SO-101 Kurulum / Install"
description: "Hashtag Robotic Studio yazılımını kurma, müşteri ve GitHub preview yolları."
permalink: /tutorials/so101-studio/setup/
lang: tr
---

<header class="page-head">
  <p class="eyebrow">Chapter 01</p>
  <h1>Önce yazılımı kur, sonra robotu tanıt.</h1>
  <p class="lead">Müşteri ürününde hedef kurulum yolu installer’dır: kullanıcı pip veya git clone ile uğraşmaz. GitHub’daki açık preview ise geliştirici yolu olarak kalır; o yolda repo clone edilir ve lokal gateway çalıştırılır.</p>
</header>

<section class="doc-section">
  <div class="dashboard-map compact">
    <div class="screen-card ready" data-reveal>
      <span>Customer</span>
      <h3>Önerilen yol: installer</h3>
      <p>Hashtag Robotic Studio `.dmg`, `.exe` veya Linux paketi olarak kurulur. Bundled local gateway ve Python runtime app ile gelir. Kullanıcı robotu USB ile bağlayıp app’i açar.</p>
    </div>
    <div class="screen-card warning" data-reveal>
      <span>GitHub preview</span>
      <h3>Geliştirici yolu: git clone</h3>
      <p>Bu repo bugün ürünün açık geliştirme/preview alanıdır. App shell ve local gateway test edilir; gerçek hareket kapalıdır.</p>
    </div>
    <div class="screen-card" data-reveal>
      <span>Runtime</span>
      <h3>LeRobot + Feetech</h3>
      <p>SO-101 donanım, calibration, record/train/eval davranışı LeRobot tarafıyla uyumlu tutulur. Feetech motor desteği gerekir.</p>
    </div>
  </div>
</section>

<section class="doc-section">
  <div class="section-head">
    <div>
      <p class="eyebrow">Customer install</p>
      <h2>Müşteri robotu aldığında nasıl kuracak?</h2>
    </div>
    <p>Ürün dağıtımında hedef, terminal göstermeden çalışan bir kurulumdur. Bu kılavuzda terminal komutları teknik referans olarak durur; normal kullanıcı app içindeki onboarding adımlarını takip eder.</p>
  </div>
  <div class="timeline">
    <div class="timeline-row" data-reveal><span>01</span><div><h3>Studio installer’ı indir</h3><p>Satın alma sonrası verilen Hashtag Robotic Studio kurulum paketini indir. macOS için `.dmg`, Windows için `.exe`, Linux için AppImage/deb/rpm hedeflenir.</p></div></div>
    <div class="timeline-row" data-reveal><span>02</span><div><h3>Uygulamayı aç</h3><p>İlk açılışta Studio lokal gateway’i başlatır, runtime health check yapar ve fiziksel hareketi kilitli tutar.</p></div></div>
    <div class="timeline-row" data-reveal><span>03</span><div><h3>Admin passkey oluştur</h3><p>Scout rover’daki WebAuthn yaklaşımı gibi, ilk kurulumda cihaz kimliği oluşturulur. Face ID, Touch ID, Windows Hello veya güvenlik anahtarı ile yönetici unlock katmanı hazırlanır.</p></div></div>
    <div class="timeline-row" data-reveal><span>04</span><div><h3>Robot profilini seç</h3><p>`SO-101 follower`, `SO-101 leader + follower` veya `simulation only` profilinden biri seçilir.</p></div></div>
    <div class="timeline-row" data-reveal><span>05</span><div><h3>USB ve kameraları bağla</h3><p>Follower ve varsa leader USB kabloları takılır. Kamera kullanılıyorsa front/wrist camera bağlanır. Studio otomatik tarar ama port rolünü kullanıcıya doğrulatır.</p></div></div>
  </div>
</section>

<section class="doc-section">
  <div class="section-head">
    <div>
      <p class="eyebrow">Developer preview</p>
      <h2>GitHub’dan denemek isteyen geliştirici ne yapar?</h2>
    </div>
    <p>Bugünkü public repo müşteri installer’ı değildir; ürün shell’i, local gateway kontratları ve docs yayınını gösterir. Gerçek SO-101 hareketi bu preview’da kapalıdır.</p>
  </div>
  <pre class="terminal" data-reveal><code>git clone https://github.com/mertozbas/hashtag-robotic-studio.git
cd hashtag-robotic-studio

python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

uvicorn services.local_gateway.app:app --reload
# Sonra tarayıcıda:
# http://127.0.0.1:8000/app/</code></pre>
  <div class="callout warning">
    <h2>Preview modu robotu hareket ettirmez.</h2>
    <p>Gateway bugün `mode=local_fake` ve `physical_motion_enabled=false` döner. Bu iyi: docs, UI, API key vault, fake operation state machine ve SafetyGate davranışı donanım riski olmadan test edilir.</p>
  </div>
</section>

<section class="doc-section">
  <div class="section-head">
    <div>
      <p class="eyebrow">Robot runtime reference</p>
      <h2>SO-101 runtime tarafında pip mi git clone mu?</h2>
    </div>
    <p>Ürün bunu installer içinde paketlemeli. Geliştirici kurulumunda LeRobot resmi dokümanı Python 3.12 ortamı önerir; PyPI kurulumu hızlı deneme, source clone ise geliştirme ve patch için daha uygundur.</p>
  </div>
  <div class="split">
    <pre class="terminal" data-reveal><code># Hızlı runtime kurulumu
python3 -m venv .venv-robot
source .venv-robot/bin/activate
pip install "lerobot[feetech]"

# LeRobot üzerinde geliştirme yapacaksan:
git clone https://github.com/huggingface/lerobot.git
cd lerobot
pip install -e ".[feetech]"</code></pre>
    <div class="panel">
      <h2>Ürün kararı</h2>
      <p>Müşteriye “pip install yap” demek doğru final ürün deneyimi değil. Studio installer; LeRobot, Feetech, gateway ve desktop shell’i paketlemeli. GitHub kılavuzu ise teknik kullanıcıya alternatifleri açık göstermeli.</p>
    </div>
  </div>
</section>

<nav class="next-prev" aria-label="Bölüm gezinme">
  <a href="{{ '/tutorials/so101-studio/' | relative_url }}">Önceki: Başlangıç</a>
  <a href="{{ '/tutorials/so101-studio/first-run/' | relative_url }}">Sonraki: İlk Kullanım</a>
</nav>
