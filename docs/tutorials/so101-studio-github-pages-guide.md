---
layout: default
title: "SO-101 + Hashtag Robotic Studio Kullanım Kılavuzu"
description: "SO-101 robot kolu ve Hashtag Robotic Studio için görsel, GitHub Pages uyumlu kurulum, güvenlik, dataset, training ve agent operasyon kılavuzu."
permalink: /tutorials/so101-studio/
lang: tr
---

<div class="guide-shell">
  <aside class="toc" aria-label="Sayfa içi gezinme">
    <strong>SO-101 Studio Guide</strong>
    <a href="#start">Start</a>
    <a href="#loop">Studio döngüsü</a>
    <a href="#hardware">Robot ve parçalar</a>
    <a href="#dashboard">Dashboard ekranları</a>
    <a href="#safety">SafetyGate</a>
    <a href="#apikeys">API key vault</a>
    <a href="#record">Dataset kaydı</a>
    <a href="#train">Hugging Face eğitim</a>
    <a href="#agent">Agent modu</a>
    <a href="#sources">Kaynaklar</a>
  </aside>

  <article class="guide-main">
    <section id="start" class="hero">
      <div data-reveal>
        <p class="eyebrow">Hashtag Robotics · SO-101 customer cockpit</p>
        <h1>Robotu terminalden değil, cockpit’ten hazırla.</h1>
        <p class="lead">Bu kılavuz SO-101 leader + follower setini Hashtag Robotic Studio ile güvenli şekilde kurmak, dataset kaydetmek, Hugging Face üzerinde policy eğitimi hazırlamak ve agent operasyonlarını SafetyGate arkasında yönetmek için tasarlandı.</p>
        <div class="hero-actions">
          <a class="button primary" href="#dashboard">Dashboard akışına geç</a>
          <a class="button" href="https://github.com/mertozbas/hashtag-robotic-studio">GitHub reposu</a>
        </div>
        <div class="status-strip">
          <div class="metric"><span>Robot</span><strong>SO-101 follower + leader</strong></div>
          <div class="metric"><span>Runtime</span><strong>Local-first gateway</strong></div>
          <div class="metric"><span>Training</span><strong>Hugging Face</strong></div>
          <div class="metric"><span>Safety</span><strong>Motion locked by default</strong></div>
        </div>
      </div>
      <div data-reveal>
        <div class="hero-visual">
          <img src="{{ '/assets/media/leader-follower.jpg' | relative_url }}" alt="SO-101 leader ve follower robot kolları" loading="eager">
        </div>
        <div class="loop-card">
          <img src="{{ '/assets/so101-loop.svg' | relative_url }}" alt="SO-101 Studio kontrol döngüsü animasyonu" loading="eager">
        </div>
      </div>
    </section>

    <section id="loop" class="section">
      <div class="section-head">
        <div>
          <p class="eyebrow">Perceive · reason · gate · act</p>
          <h2>Studio döngüsü</h2>
        </div>
        <p>Strands Robots dokümantasyonundaki sim-first/hardware opt-in modelini ürün yüzeyine taşıyoruz: kullanıcı niyeti dashboard’a gelir, agent ve policy plan üretir, SafetyGate fiziksel dünyaya çıkmadan önce deterministik karar verir.</p>
      </div>
      <div class="pipeline">
        <div class="step-card" data-step="01" data-reveal>
          <h3>Observe</h3>
          <p>Gateway, port adayları, kamera adayları, calibration dosyaları ve package durumunu sadece okur.</p>
        </div>
        <div class="step-card" data-step="02" data-reveal>
          <h3>Plan</h3>
          <p>Dashboard veya agent, teleop, kayıt, dataset kalite kontrolü ya da training planı üretir.</p>
        </div>
        <div class="step-card" data-step="03" data-reveal>
          <h3>Gate</h3>
          <p>SafetyGate follower port, calibration id, süre limiti, acil stop ve workspace_clear alanlarını kontrol eder.</p>
        </div>
        <div class="step-card" data-step="04" data-reveal>
          <h3>Record</h3>
          <p>LeRobot uyumlu episode, camera key, state/action feature ve task metni ile dataset oluşur.</p>
        </div>
        <div class="step-card" data-step="05" data-reveal>
          <h3>Train</h3>
          <p>Hugging Face token bağlandıktan sonra ACT, Diffusion Policy veya SmolVLA eğitimi hazırlanır.</p>
        </div>
      </div>
    </section>

    <section id="hardware" class="section">
      <div class="section-head">
        <div>
          <p class="eyebrow">Robot anatomy</p>
          <h2>Robot ve parçalar</h2>
        </div>
        <p>SO-101 küçük bir masaüstü kol gibi görünür, ama ürün deneyimi gerçek robotik operasyon gibi ele alınır: servo, serial bus, kamera, calibration ve data pipeline aynı cockpit’te görünür olmalı.</p>
      </div>
      <div class="media-grid">
        <div class="media-card" data-reveal>
          <img src="{{ '/assets/media/hero-follower.webp' | relative_url }}" alt="SO-101 follower robot kol">
          <div><h3>Follower</h3><p>Görevi yapan fiziksel kol. Teleop, kayıt ve policy rollout bu tarafta gerçek hareket üretir.</p></div>
        </div>
        <div class="media-card" data-reveal>
          <img src="{{ '/assets/media/leader.webp' | relative_url }}" alt="SO-101 leader robot kol">
          <div><h3>Leader</h3><p>Operatörün elle yönlendirdiği kontrol kolu. Dataset kalitesi için mapping doğrulanır.</p></div>
        </div>
        <div class="media-card" data-reveal>
          <img src="{{ '/assets/media/part-servo.jpg' | relative_url }}" alt="Feetech STS3215 servo">
          <div><h3>STS3215 servo</h3><p>Serial bus servo katmanı. Motor komutu sadece approved operation runner üzerinden geçmelidir.</p></div>
        </div>
        <div class="media-card" data-reveal>
          <img src="{{ '/assets/media/part-board.png' | relative_url }}" alt="SO-101 kontrol kartı">
          <div><h3>Bus kartı</h3><p>USB/serial bağlantı noktası. Port adı varsayılmaz; dashboard aday ve confidence gösterir.</p></div>
        </div>
        <div class="media-card" data-reveal>
          <img src="{{ '/assets/media/part-gripper.png' | relative_url }}" alt="SO-101 gripper">
          <div><h3>Gripper</h3><p>Action dimension ve gripper range policy compatibility içinde ayrıca doğrulanır.</p></div>
        </div>
        <div class="media-card" data-reveal>
          <img src="{{ '/assets/media/part-lerobot.png' | relative_url }}" alt="LeRobot uyumluluğu">
          <div><h3>LeRobot uyumu</h3><p>Dataset schema, calibration semantics ve record/train/eval akışı LeRobot ile hizalı tutulur.</p></div>
        </div>
      </div>

      <div class="media-grid" style="margin-top: 14px">
        <div class="media-card" data-reveal>
          <video controls preload="metadata" poster="{{ '/assets/anatomy/Joint1.jpg' | relative_url }}">
            <source src="{{ '/assets/anatomy/Joint1.mp4' | relative_url }}" type="video/mp4">
          </video>
          <div><h3>Taban ekseni</h3><p>Shoulder pan hareketinin mekanik mantığı.</p></div>
        </div>
        <div class="media-card" data-reveal>
          <video controls preload="metadata" poster="{{ '/assets/anatomy/Joint2.jpg' | relative_url }}">
            <source src="{{ '/assets/anatomy/Joint2.mp4' | relative_url }}" type="video/mp4">
          </video>
          <div><h3>Omuz ekseni</h3><p>Leader/follower mapping sırasında en kritik eklem çiftlerinden biri.</p></div>
        </div>
        <div class="media-card" data-reveal>
          <video controls preload="metadata" poster="{{ '/assets/anatomy/Gripper.jpg' | relative_url }}">
            <source src="{{ '/assets/anatomy/Gripper.mp4' | relative_url }}" type="video/mp4">
          </video>
          <div><h3>Gripper</h3><p>Pick/place tasklarında veri kalitesini en çok etkileyen hareket.</p></div>
        </div>
      </div>
    </section>

    <section id="dashboard" class="section">
      <div class="section-head">
        <div>
          <p class="eyebrow">Cockpit map</p>
          <h2>Dashboard ekranları</h2>
        </div>
        <p>Studio bir landing page değil; fiziksel robotu bağlamaya hazır operasyon paneli. Her ekran bir risk veya veri kalitesi sorusunu cevaplamalı.</p>
      </div>
      <div class="card-grid">
        <div class="panel" data-reveal><h3>Başlangıç</h3><p>Readiness, SafetyGate, follower/leader durumu ve sonraki güvenli aksiyon.</p></div>
        <div class="panel" data-reveal><h3>Cihazlar</h3><p>Port adayları, kamera adayları, calibration presence ve no-motion inventory.</p></div>
        <div class="panel" data-reveal><h3>Kalibrasyon</h3><p>Dosya varlığı, robot role eşleşmesi ve overwrite kilidi.</p></div>
        <div class="panel" data-reveal><h3>Kayıt</h3><p>Task metni, dataset repo/path, FPS, episode süresi ve camera key mapping.</p></div>
        <div class="panel" data-reveal><h3>Policyler</h3><p>Hugging Face training hedefi, expected features, remote code trust ve real rollout blocker listesi.</p></div>
        <div class="panel" data-reveal><h3>Agent</h3><p>Diagnostic/simulation tool’ları açık, physical control tool’ları session scope olmadan kapalı.</p></div>
      </div>
    </section>

    <section id="safety" class="section">
      <div class="section-head">
        <div>
          <p class="eyebrow">Hardware-safe by default</p>
          <h2>SafetyGate fiziksel dünyaya çıkan kapıdır</h2>
        </div>
        <p>Fiziksel hareket başlatma, teleop, motor testi, kayıt ve real rollout kullanıcı unlock olmadan başlamaz. Dashboard hazır görünse bile operation contract eksikse hareket yok.</p>
      </div>
      <div class="split">
        <div class="panel danger" data-reveal>
          <h3>Bloklu kalması gereken durumlar</h3>
          <p>Kalibrasyon dosyasını yazma veya üzerine yazma, backup ve açık kullanıcı onayı olmadan kapalıdır.</p>
          <ul>
            <li>Follower port bilinmiyor veya role doğrulanmadı.</li>
            <li>Kalibrasyon id eşleşmiyor.</li>
            <li>Camera config veya image key mapping eksik.</li>
            <li>Policy action dimension ve unit conversion doğrulanmadı.</li>
            <li>Duration limit, emergency_stop veya workspace_clear yok.</li>
            <li>Agent fiziksel tool için session scope almadı.</li>
          </ul>
        </div>
        <pre class="terminal" data-reveal><code>type: run_real_policy
mode: real
safety_level: physical_motion
required_inputs:
  - follower_port
  - calibration_id
  - policy_checkpoint
  - feature_mapping
  - duration_limit
  - emergency_stop
  - workspace_clear</code></pre>
      </div>
    </section>

    <section id="apikeys" class="section">
      <div class="section-head">
        <div>
          <p class="eyebrow">Secrets stay masked</p>
          <h2>API key vault</h2>
        </div>
        <p>Model eğitimi Hugging Face üzerinden yapılacak; agent ve entegrasyon keyleri aynı ayar yüzeyinde tutulur. Secret değeri response, log veya support bundle içinde gösterilmez.</p>
      </div>
      <table>
        <thead><tr><th>Provider</th><th>Kullanım</th><th>UI davranışı</th></tr></thead>
        <tbody>
          <tr><td>Hugging Face</td><td>Dataset upload, remote training, model download</td><td>Training hazırlığı için required provider.</td></tr>
          <tr><td>OpenAI / Anthropic / Gemini</td><td>Agent LLM sağlayıcıları</td><td>Provider connected + last_four dışında secret render edilmez.</td></tr>
          <tr><td>GitHub</td><td>Issue sync, release notes, repo workflow</td><td>Publish ve support iş akışları için ayrı scope düşünülür.</td></tr>
          <tr><td>W&B / AWS / Custom MCP</td><td>Tracking, artifact storage, tool connectors</td><td>Opsiyonel entegrasyon; production’da OS keychain’e taşınmalı.</td></tr>
        </tbody>
      </table>
    </section>

    <section id="record" class="section">
      <div class="section-head">
        <div>
          <p class="eyebrow">LeRobot dataset discipline</p>
          <h2>Veri kaydı</h2>
        </div>
        <p>Dataset kaydı fiziksel hareket sayılır. Kayıt ekranı önce plan üretir, sonra SafetyGate ve kullanıcı unlock ile bounded session açılır.</p>
      </div>
      <div class="pipeline">
        <div class="step-card" data-step="A" data-reveal><h3>Task</h3><p>Tek davranışı tarif eden kısa task metni.</p></div>
        <div class="step-card" data-step="B" data-reveal><h3>Episode</h3><p>Süre, FPS, tekrar sayısı ve stop path.</p></div>
        <div class="step-card" data-step="C" data-reveal><h3>Camera keys</h3><p>front/wrist runtime mapping ve dataset key eşleşmesi.</p></div>
        <div class="step-card" data-step="D" data-reveal><h3>Quality</h3><p>Eksik frame, yarım episode, state/action tutarlılığı.</p></div>
        <div class="step-card" data-step="E" data-reveal><h3>Upload</h3><p>Hub push sadece açık kullanıcı aksiyonuyla.</p></div>
      </div>
    </section>

    <section id="train" class="section">
      <div class="section-head">
        <div>
          <p class="eyebrow">Policy studio</p>
          <h2>Hugging Face üzerinde eğitim</h2>
        </div>
        <p>Training işi maliyetli ve uzun olabilir; Studio otomatik başlatmaz. Dataset kalite kontrolü, token, output repo ve feature mapping tamamlanınca eğitim planı hazırlar.</p>
      </div>
      <div class="split">
        <div class="panel" data-reveal>
          <h3>Minimum hazırlık</h3>
          <ul>
            <li>Hugging Face API key bağlı.</li>
            <li>Dataset repo/path ve episode kalite durumu doğrulanmış.</li>
            <li>Policy family seçilmiş: ACT, Diffusion Policy veya SmolVLA.</li>
            <li>Output model repo belirlenmiş.</li>
            <li>Expected image/state/action feature eşleşmesi tamamlanmış.</li>
          </ul>
        </div>
        <pre class="terminal" data-reveal><code># Studio bunu doğrudan çalıştırmaz; güvenli plan olarak üretir.
hf auth login
lerobot-record --dataset.repo_id=&lt;user&gt;/&lt;dataset&gt;
lerobot-train --policy.type=act --dataset.repo_id=&lt;user&gt;/&lt;dataset&gt;</code></pre>
      </div>
    </section>

    <section id="agent" class="section">
      <div class="section-head">
        <div>
          <p class="eyebrow">Agent tools are contracts</p>
          <h2>Agent operasyon modu</h2>
        </div>
        <p>Agent bir sohbet kutusundan robotu serbest sürmez. Diagnose ve simulation güvenli tool’lardır; physical request/control tool’ları SafetyGate ve session scope olmadan kapalıdır.</p>
      </div>
      <div class="card-grid">
        <div class="panel" data-reveal><h3>diagnose_setup</h3><p>Kurulum blokajlarını okur. Fiziksel hareket yok.</p></div>
        <div class="panel" data-reveal><h3>simulate_policy</h3><p>Sim/dry-run planı üretir. Donanım opt-in değildir.</p></div>
        <div class="panel warning" data-reveal><h3>request_teleop_session</h3><p>Fiziksel hareket ister; kullanıcı unlock ve operation contract gerekir.</p></div>
        <div class="panel danger" data-reveal><h3>run_real_policy</h3><p>Real rollout. Mapping, calibration, duration ve stop path eksikse bloklu kalır.</p></div>
        <div class="panel" data-reveal><h3>support_bundle</h3><p>Tanılama export eder; secret değerleri dahil edilmez.</p></div>
        <div class="panel" data-reveal><h3>tool stream</h3><p>Kullanıcı agent’in hangi tool’u neden çağırdığını görür.</p></div>
      </div>
    </section>

    <section id="sources" class="section">
      <div class="section-head">
        <div>
          <p class="eyebrow">References</p>
          <h2>Kaynaklar</h2>
        </div>
        <p>Bu sayfa ürün assetleri, LeRobot resmi dokümanları ve Strands Robots’un dokümantasyon yaklaşımı incelenerek yeniden düzenlendi.</p>
      </div>
      <div class="source-grid">
        <div class="source-card"><strong>Hashtag Robotics SO-101 ürün sayfası</strong><a href="https://labs.hashtagworldcompany.com/product">https://labs.hashtagworldcompany.com/product</a></div>
        <div class="source-card"><strong>Strands Robots docs</strong><a href="https://strands-labs.github.io/robots/">https://strands-labs.github.io/robots/</a></div>
        <div class="source-card"><strong>LeRobot SO-101</strong><a href="https://huggingface.co/docs/lerobot/en/so101">https://huggingface.co/docs/lerobot/en/so101</a></div>
        <div class="source-card"><strong>LeRobot imitation learning</strong><a href="https://huggingface.co/docs/lerobot/en/il_robots">https://huggingface.co/docs/lerobot/en/il_robots</a></div>
        <div class="source-card"><strong>LeRobot ACT</strong><a href="https://huggingface.co/docs/lerobot/en/act">https://huggingface.co/docs/lerobot/en/act</a></div>
        <div class="source-card"><strong>LeRobotDataset v3</strong><a href="https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3">https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3</a></div>
        <div class="source-card"><strong>Hugging Face LeRobot GitHub</strong><a href="https://github.com/huggingface/lerobot">https://github.com/huggingface/lerobot</a></div>
        <div class="source-card"><strong>TheRobotStudio SO-ARM100 / SO-101</strong><a href="https://github.com/TheRobotStudio/SO-ARM100">https://github.com/TheRobotStudio/SO-ARM100</a></div>
      </div>
    </section>
  </article>
</div>
