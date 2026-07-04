---
layout: default
book: so101
guide_section: overview
title: "SO-101 + Hashtag Robotic Studio Kitabı"
description: "SO-101 robot kolu ve Hashtag Robotic Studio için GitHub Pages uyumlu ürün kitabı."
permalink: /tutorials/so101-studio/
lang: tr
---

<section class="book-hero">
  <div>
    <p class="eyebrow">Hashtag Robotics · SO-101 customer cockpit</p>
    <h1>SO-101’i terminalden değil, ürün cockpit’inden yönet.</h1>
    <p class="lead">Bu kitapçık, SO-101 leader + follower setini Hashtag Robotic Studio ile kurmak, güvenli şekilde bağlamak, dataset kaydetmek, Hugging Face üzerinde eğitim hazırlamak ve agent operasyonlarını SafetyGate arkasında yönetmek için tasarlandı.</p>
    <div class="hero-actions">
      <a class="button primary" href="{{ '/tutorials/so101-studio/setup/' | relative_url }}">Kurulum akışına başla</a>
      <a class="button" href="{{ '/tutorials/so101-studio/dashboard/' | relative_url }}">Dashboard yapısını gör</a>
    </div>
  </div>
  <div class="hero-visual" data-reveal>
    <img src="{{ '/assets/media/leader-follower.jpg' | relative_url }}" alt="SO-101 leader ve follower robot kolları" loading="eager">
  </div>
</section>

<section class="doc-section">
  <div class="section-head">
    <div>
      <p class="eyebrow">Book structure</p>
      <h2>Tek uzun sayfa değil, bölüm bölüm ürün kitabı.</h2>
    </div>
    <p>Sol menüdeki her başlık ayrı URL açar. Kullanıcı okuduğu yeri paylaşabilir, GitHub Pages deploy’u her bölümü bağımsız route olarak sunar ve app içindeki kılavuz linkleri doğrudan ilgili bölüme gidebilir.</p>
  </div>
  <div class="chapter-grid">
    <a class="chapter-card" href="{{ '/tutorials/so101-studio/setup/' | relative_url }}" data-reveal>
      <span>01</span><h3>Kurulum Akışı</h3><p>Profile seçimi, device discovery, calibration check ve observation-only bağlantı.</p>
    </a>
    <a class="chapter-card" href="{{ '/tutorials/so101-studio/hardware/' | relative_url }}" data-reveal>
      <span>02</span><h3>Robot ve Parçalar</h3><p>Follower, leader, servo, bus kartı, gripper ve autoplay montaj videoları.</p>
    </a>
    <a class="chapter-card" href="{{ '/tutorials/so101-studio/dashboard/' | relative_url }}" data-reveal>
      <span>03</span><h3>Dashboard</h3><p>Cockpit ekranları, readiness modeli ve local gateway bağlantısı.</p>
    </a>
    <a class="chapter-card" href="{{ '/tutorials/so101-studio/safety/' | relative_url }}" data-reveal>
      <span>04</span><h3>SafetyGate</h3><p>Fiziksel hareketin hangi kontratlarla engellendiği ve ne zaman açıldığı.</p>
    </a>
    <a class="chapter-card" href="{{ '/tutorials/so101-studio/api-keys/' | relative_url }}" data-reveal>
      <span>05</span><h3>API Key Vault</h3><p>Hugging Face ve agent sağlayıcı keyleri için maskeli ayar yüzeyi.</p>
    </a>
    <a class="chapter-card" href="{{ '/tutorials/so101-studio/dataset/' | relative_url }}" data-reveal>
      <span>06</span><h3>Dataset Kaydı</h3><p>LeRobot uyumlu episode, camera key ve kalite kontrol akışı.</p>
    </a>
    <a class="chapter-card" href="{{ '/tutorials/so101-studio/training/' | relative_url }}" data-reveal>
      <span>07</span><h3>Hugging Face Eğitim</h3><p>Training planı, model ailesi, output repo ve rollout öncesi uyumluluk.</p>
    </a>
    <a class="chapter-card" href="{{ '/tutorials/so101-studio/agent/' | relative_url }}" data-reveal>
      <span>08</span><h3>Agent Modu</h3><p>Strands agent tool izinleri, tool stream ve fiziksel session scope.</p>
    </a>
    <a class="chapter-card" href="{{ '/tutorials/so101-studio/sources/' | relative_url }}" data-reveal>
      <span>09</span><h3>Kaynaklar</h3><p>Hashtag Robotics, Strands Robots, LeRobot ve SO-101 referansları.</p>
    </a>
  </div>
</section>

<section class="doc-section">
  <div class="split">
    <div class="panel">
      <p class="eyebrow">System diagram</p>
      <h2>Ürün modeli</h2>
      <p>Diagram artık robot kolu çizmeye çalışmıyor. Bunun yerine gerçek ürün mimarisini gösteriyor: Studio UI, local gateway, SafetyGate, LeRobot runtime, Strands agent ve Hugging Face eğitim hattı.</p>
    </div>
    <div class="diagram-frame" data-reveal>
      <img src="{{ '/assets/so101-loop.svg' | relative_url }}" alt="Hashtag Robotic Studio sistem akışı">
    </div>
  </div>
</section>

<nav class="next-prev" aria-label="Sonraki bölüm">
  <span></span>
  <a href="{{ '/tutorials/so101-studio/setup/' | relative_url }}">Sonraki: Kurulum Akışı</a>
</nav>
