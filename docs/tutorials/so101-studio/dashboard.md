---
layout: default
book: so101
guide_section: dashboard
title: "Hashtag Robotic Studio Dashboard"
description: "SO-101 için cockpit ekranları ve readiness modeli."
permalink: /tutorials/so101-studio/dashboard/
lang: tr
---

<header class="page-head">
  <p class="eyebrow">Chapter 03</p>
  <h1>Dashboard bir landing page değil, robot hazırlık cockpit’i.</h1>
  <p class="lead">Her ekran tek bir operasyon sorusunu cevaplamalı: cihaz hazır mı, calibration doğru mu, kayıt güvenli mi, policy uyumlu mu, agent ne yapmaya çalışıyor?</p>
</header>

<section class="doc-section">
  <div class="dashboard-map">
    <div class="screen-card ready" data-reveal><span>Home</span><h3>Başlangıç</h3><p>Readiness, SafetyGate, follower/leader durumu ve önerilen güvenli aksiyon.</p></div>
    <div class="screen-card" data-reveal><span>Devices</span><h3>Cihazlar</h3><p>Port adayları, kamera adayları, calibration presence ve no-motion inventory.</p></div>
    <div class="screen-card warning" data-reveal><span>Calibration</span><h3>Kalibrasyon</h3><p>Dosya varlığı, role eşleşmesi, backup ve overwrite kilidi.</p></div>
    <div class="screen-card danger" data-reveal><span>Live</span><h3>Canlı Kontrol</h3><p>Motor lock, speed scale, session timer, emergency stop ve manual unlock.</p></div>
    <div class="screen-card" data-reveal><span>Recording</span><h3>Kayıt</h3><p>Task, dataset path/repo, FPS, episode planı ve camera key mapping.</p></div>
    <div class="screen-card" data-reveal><span>Policies</span><h3>Policyler</h3><p>Hugging Face training setup, expected features ve rollout blocker listesi.</p></div>
    <div class="screen-card" data-reveal><span>Agent</span><h3>Agent</h3><p>Tool-call stream, permission scope ve SafetyGate sonucu.</p></div>
    <div class="screen-card" data-reveal><span>Settings</span><h3>Ayarlar</h3><p>API key vault, language, gateway config ve support export.</p></div>
  </div>
</section>

<section class="doc-section">
  <div class="split">
    <pre class="terminal" data-reveal><code>GET /health
GET /inventory
GET /settings/api-keys
POST /settings/api-keys/{provider}
POST /operations
POST /operations/{id}/stop</code></pre>
    <div class="panel">
      <h2>UI doğrudan LeRobot veya Strands çağırmaz.</h2>
      <p>Dashboard stable local gateway kontratlarıyla konuşur. SDK değişirse UI kırılmamalı; adapter ve gateway katmanı değişikliği absorbe eder.</p>
    </div>
  </div>
</section>

<nav class="next-prev" aria-label="Bölüm gezinme">
  <a href="{{ '/tutorials/so101-studio/hardware/' | relative_url }}">Önceki: Robot ve Parçalar</a>
  <a href="{{ '/tutorials/so101-studio/safety/' | relative_url }}">Sonraki: SafetyGate</a>
</nav>
