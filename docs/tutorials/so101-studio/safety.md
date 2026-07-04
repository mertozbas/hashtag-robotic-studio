---
layout: default
book: so101
guide_section: safety
title: "SafetyGate"
description: "SO-101 fiziksel operasyonları için SafetyGate ve operation contract modeli."
permalink: /tutorials/so101-studio/safety/
lang: tr
---

<header class="page-head">
  <p class="eyebrow">Chapter 04</p>
  <h1>SafetyGate fiziksel dünyaya çıkan kapıdır.</h1>
  <p class="lead">Fiziksel hareket başlatma, teleop, motor testi, kayıt ve real rollout kullanıcı unlock olmadan başlamaz. Dashboard hazır görünse bile operation contract eksikse hareket yok.</p>
  <p class="lead narrow">Her fiziksel operation için süre limiti, acil stop ve workspace_clear alanları açıkça doğrulanır.</p>
</header>

<section class="doc-section">
  <div class="split">
    <div class="panel danger" data-reveal>
      <h2>Bloklu kalması gereken durumlar</h2>
      <ul>
        <li>Follower port bilinmiyor veya role doğrulanmadı.</li>
        <li>Kalibrasyon id eşleşmiyor.</li>
        <li>Camera config veya image key mapping eksik.</li>
        <li>Policy action dimension ve unit conversion doğrulanmadı.</li>
        <li>Süre limiti, acil stop veya workspace_clear yok.</li>
        <li>Agent fiziksel tool için session scope almadı.</li>
        <li>Kalibrasyon dosyasını yazma veya üzerine yazma için backup ve açık kullanıcı onayı yok.</li>
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
  - workspace_clear
  - user_unlock</code></pre>
  </div>
</section>

<section class="doc-section">
  <div class="state-strip">
    <div class="state-pill blocked">Blocked</div>
    <div class="state-pill ready">Ready</div>
    <div class="state-pill running">Running</div>
    <div class="state-pill stopped">Stopped</div>
  </div>
  <p class="lead narrow">Bu state modeli UI’da renk dışında metin ve ikonla da desteklenmeli. Stop her zaman görünür kalır; agent işbirliğine bağlı değildir.</p>
</section>

<nav class="next-prev" aria-label="Bölüm gezinme">
  <a href="{{ '/tutorials/so101-studio/dashboard/' | relative_url }}">Önceki: Dashboard</a>
  <a href="{{ '/tutorials/so101-studio/api-keys/' | relative_url }}">Sonraki: API Key Vault</a>
</nav>
