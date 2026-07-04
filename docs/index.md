---
layout: default
title: "Hashtag Robotic Studio Kılavuzları"
description: "SO-101 robot kolu ve Hashtag Robotic Studio için görsel GitHub Pages dokümantasyon merkezi."
permalink: /
lang: tr
---

<section class="hero">
  <div data-reveal>
    <p class="eyebrow">SO-101 customer docs</p>
    <h1>Hashtag Robotic Studio kılavuz merkezi.</h1>
    <p class="lead">Robot kolu bağlama, SafetyGate preflight, dataset kayıt, Hugging Face training ve agent operasyonları için görsel dokümantasyon.</p>
    <div class="hero-actions">
      <a class="button primary" href="{{ '/tutorials/so101-studio/' | relative_url }}">SO-101 kılavuzunu aç</a>
      <a class="button" href="https://github.com/mertozbas/hashtag-robotic-studio">GitHub reposu</a>
    </div>
  </div>
  <div data-reveal>
    <div class="hero-visual">
      <img src="{{ '/assets/media/leader-follower.jpg' | relative_url }}" alt="SO-101 leader ve follower robot kolları">
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <p class="eyebrow">Published guides</p>
      <h2>Yayındaki kılavuzlar</h2>
    </div>
    <p>Bu alan website entegrasyonundan bağımsızdır; GitHub Pages üzerinde doğrudan çalışır.</p>
  </div>
  <div class="card-grid">
    <div class="panel" data-reveal>
      <h3>SO-101 + Studio Kullanım Kılavuzu</h3>
      <p>Kurulum, dashboard, SafetyGate, API key vault, dataset, training ve agent operasyon akışı.</p>
      <a class="button primary" href="{{ '/tutorials/so101-studio/' | relative_url }}">Kılavuza git</a>
    </div>
    <div class="panel" data-reveal>
      <h3>Local-first dashboard</h3>
      <p>Core robot workflows yerel gateway üzerinden çalışır; cloud backend zorunlu değildir.</p>
    </div>
    <div class="panel warning" data-reveal>
      <h3>SafetyGate</h3>
      <p>Fiziksel hareket, kullanıcı unlock ve operation contract olmadan başlamaz.</p>
    </div>
  </div>
</section>
