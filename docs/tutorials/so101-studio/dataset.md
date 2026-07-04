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
  <p class="lead">Kayıt ekranı önce plan üretir. Kullanıcı task, episode, FPS, camera key ve stop path alanlarını tamamlar; SafetyGate geçmeden gerçek kayıt session açılmaz.</p>
</header>

<section class="doc-section">
  <div class="pipeline">
    <div class="step-card" data-step="A" data-reveal><h3>Task</h3><p>Tek davranışı tarif eden kısa task metni.</p></div>
    <div class="step-card" data-step="B" data-reveal><h3>Episode</h3><p>Süre, FPS, tekrar sayısı ve stop path.</p></div>
    <div class="step-card" data-step="C" data-reveal><h3>Camera keys</h3><p>front/wrist runtime mapping ve dataset key eşleşmesi.</p></div>
    <div class="step-card" data-step="D" data-reveal><h3>Quality</h3><p>Eksik frame, yarım episode, state/action tutarlılığı.</p></div>
    <div class="step-card" data-step="E" data-reveal><h3>Upload</h3><p>Hub push sadece açık kullanıcı aksiyonuyla.</p></div>
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
