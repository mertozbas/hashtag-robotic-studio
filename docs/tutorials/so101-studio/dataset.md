---
layout: default
book: so101
guide_section: dataset
title: "Dataset Kaydı"
description: "SO-101 ile LeRobot uyumlu dataset kayıt ve kalite kontrol akışı."
permalink: /tutorials/so101-studio/dataset/
lang: tr
---

<header class="page-head">
  <p class="eyebrow">Chapter 06</p>
  <h1>Dataset kaydı fiziksel hareket sınıfındadır.</h1>
  <p class="lead">Kayıt ekranı önce plan üretir. Kullanıcı task, episode, FPS, camera key ve stop path alanlarını tamamlar; passkey unlock ve SafetyGate geçmeden gerçek kayıt session açılmaz.</p>
</header>

<section class="doc-section">
  <div class="section-head">
    <div>
      <p class="eyebrow">Customer workflow</p>
      <h2>Eğitim verisi nasıl toplanır?</h2>
    </div>
    <p>Kullanıcı “Kayıt” ekranında terminal komutu yazmaz. Studio LeRobot uyumlu record planını üretir, kullanıcıya ne kaydedileceğini gösterir ve sadece onaydan sonra bounded session açar.</p>
  </div>
  <div class="pipeline">
    <div class="step-card" data-step="A" data-reveal><h3>Task</h3><p>Tek davranışı tarif eden kısa task metni.</p></div>
    <div class="step-card" data-step="B" data-reveal><h3>Episode</h3><p>Süre, FPS, tekrar sayısı ve stop path.</p></div>
    <div class="step-card" data-step="C" data-reveal><h3>Camera keys</h3><p>front/wrist runtime mapping ve dataset key eşleşmesi.</p></div>
    <div class="step-card" data-step="D" data-reveal><h3>Quality</h3><p>Eksik frame, yarım episode, state/action tutarlılığı.</p></div>
    <div class="step-card" data-step="E" data-reveal><h3>Upload</h3><p>Hub push sadece açık kullanıcı aksiyonuyla.</p></div>
  </div>
</section>

<section class="doc-section">
  <div class="timeline">
    <div class="timeline-row" data-reveal><span>01</span><div><h3>Task metnini yaz</h3><p>Örnek: “Siyah küpü kavra ve kutuya bırak.” Tek dataset, tek davranış hedeflemeli.</p></div></div>
    <div class="timeline-row" data-reveal><span>02</span><div><h3>Episode planını seç</h3><p>Başlangıç için 5 test episode’u; gerçek eğitim için aynı davranışı farklı başlangıç pozisyonlarında en az 50 episode hedeflenir.</p></div></div>
    <div class="timeline-row" data-reveal><span>03</span><div><h3>Kamera açılarını sabitle</h3><p>Front camera objeyi ve gripper’ı görmeli. Kamera mapping değişirse training ve rollout compatibility yeniden kontrol edilir.</p></div></div>
    <div class="timeline-row" data-reveal><span>04</span><div><h3>Leader ile davranışı göster</h3><p>Leader + follower teleop session açılır. Kullanıcı her episode’da aynı task’ı temiz ve tutarlı yapar.</p></div></div>
    <div class="timeline-row" data-reveal><span>05</span><div><h3>Dataset Studio’da kalite kontrol yap</h3><p>Eksik frame, kesilmiş episode, yanlış camera key, bozuk state/action boyutu veya başarısız task işaretlenir.</p></div></div>
    <div class="timeline-row" data-reveal><span>06</span><div><h3>Hub upload kararını ver</h3><p>Hugging Face upload açık kullanıcı aksiyonudur. Lokal dataset önce incelenebilir; sonra Hub’a gönderilebilir.</p></div></div>
  </div>
</section>

<section class="doc-section">
  <pre class="terminal" data-reveal><code>dataset:
  repo_id: "&lt;user&gt;/&lt;task-dataset&gt;"
  fps: 30
  cameras:
    runtime_front: "front"
    dataset_front: "observation.images.front"
  state_features:
    - shoulder_pan.pos
    - shoulder_lift.pos
    - elbow_flex.pos
    - wrist_flex.pos
    - wrist_roll.pos
    - gripper.pos
  action_dimension: 6</code></pre>
</section>

<nav class="next-prev" aria-label="Bölüm gezinme">
  <a href="{{ '/tutorials/so101-studio/api-keys/' | relative_url }}">Önceki: API Key Vault</a>
  <a href="{{ '/tutorials/so101-studio/training/' | relative_url }}">Sonraki: Hugging Face Eğitim</a>
</nav>
