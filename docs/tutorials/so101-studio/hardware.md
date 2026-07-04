---
layout: default
book: so101
guide_section: hardware
title: "SO-101 Robot ve Parçalar"
description: "SO-101 follower, leader, servo, kart, gripper ve montaj hareketleri."
permalink: /tutorials/so101-studio/hardware/
lang: tr
---

<header class="page-head">
  <p class="eyebrow">Chapter 02</p>
  <h1>Robot anatomisi ürün deneyiminin parçası olmalı.</h1>
  <p class="lead">Kullanıcı sadece dashboard görmez; hangi parçanın hangi operasyon riskini etkilediğini de görür. Videolar kontrol çubuğu olmadan otomatik döner, böylece bu bölüm kitapçık içinde canlı ürün görseli gibi davranır.</p>
</header>

<section class="doc-section">
  <div class="media-grid">
    <div class="media-card" data-reveal><img src="{{ '/assets/media/hero-follower.webp' | relative_url }}" alt="SO-101 follower robot kol"><div><h3>Follower</h3><p>Görevi yapan fiziksel kol. Teleop, kayıt ve policy rollout bu tarafta hareket üretir.</p></div></div>
    <div class="media-card" data-reveal><img src="{{ '/assets/media/leader.webp' | relative_url }}" alt="SO-101 leader robot kol"><div><h3>Leader</h3><p>Operatörün elle yönlendirdiği kontrol kolu. Dataset kalitesi için mapping doğrulanır.</p></div></div>
    <div class="media-card" data-reveal><img src="{{ '/assets/media/part-servo.jpg' | relative_url }}" alt="Feetech STS3215 servo"><div><h3>STS3215 servo</h3><p>Serial bus servo katmanı. Motor komutu sadece approved runner üzerinden geçmelidir.</p></div></div>
    <div class="media-card" data-reveal><img src="{{ '/assets/media/part-board.png' | relative_url }}" alt="SO-101 kontrol kartı"><div><h3>Bus kartı</h3><p>Port adı varsayılmaz; Studio adayları ve doğrulama durumunu gösterir.</p></div></div>
    <div class="media-card" data-reveal><img src="{{ '/assets/media/part-gripper.png' | relative_url }}" alt="SO-101 gripper"><div><h3>Gripper</h3><p>Action dimension, gripper range ve yön bilgisi policy compatibility içinde doğrulanır.</p></div></div>
    <div class="media-card" data-reveal><img src="{{ '/assets/media/part-lerobot.png' | relative_url }}" alt="LeRobot uyumluluğu"><div><h3>LeRobot uyumu</h3><p>Dataset schema, calibration semantics ve record/train/eval akışı LeRobot ile hizalı tutulur.</p></div></div>
  </div>
</section>

<section class="doc-section">
  <div class="section-head">
    <div>
      <p class="eyebrow">Looping assembly motion</p>
      <h2>Montaj hareketleri otomatik oynar.</h2>
    </div>
    <p>Bu videolar kullanıcıdan play/pause beklemez. GitHub Pages üzerinde muted autoplay + loop + playsinline ile ürün kitapçığı içinde sürekli yaşayan görseller olarak çalışır.</p>
  </div>
  <div class="media-grid">
    <div class="media-card" data-reveal>
      <video class="ambient-video" autoplay loop muted playsinline preload="auto" poster="{{ '/assets/anatomy/Joint1.jpg' | relative_url }}" aria-label="Taban ekseni montaj animasyonu">
        <source src="{{ '/assets/anatomy/Joint1.mp4' | relative_url }}" type="video/mp4">
      </video>
      <div><h3>Taban ekseni</h3><p>Shoulder pan hareketinin mekanik mantığı.</p></div>
    </div>
    <div class="media-card" data-reveal>
      <video class="ambient-video" autoplay loop muted playsinline preload="auto" poster="{{ '/assets/anatomy/Joint2.jpg' | relative_url }}" aria-label="Omuz ekseni montaj animasyonu">
        <source src="{{ '/assets/anatomy/Joint2.mp4' | relative_url }}" type="video/mp4">
      </video>
      <div><h3>Omuz ekseni</h3><p>Leader/follower mapping sırasında kritik eklem çiftlerinden biri.</p></div>
    </div>
    <div class="media-card" data-reveal>
      <video class="ambient-video" autoplay loop muted playsinline preload="auto" poster="{{ '/assets/anatomy/Joint3.jpg' | relative_url }}" aria-label="Dirsek ekseni montaj animasyonu">
        <source src="{{ '/assets/anatomy/Joint3.mp4' | relative_url }}" type="video/mp4">
      </video>
      <div><h3>Dirsek ekseni</h3><p>Policy rollout öncesi joint limit ve direction kontrolü ister.</p></div>
    </div>
    <div class="media-card" data-reveal>
      <video class="ambient-video" autoplay loop muted playsinline preload="auto" poster="{{ '/assets/anatomy/Gripper.jpg' | relative_url }}" aria-label="Gripper montaj animasyonu">
        <source src="{{ '/assets/anatomy/Gripper.mp4' | relative_url }}" type="video/mp4">
      </video>
      <div><h3>Gripper</h3><p>Pick/place tasklarında veri kalitesini en çok etkileyen hareket.</p></div>
    </div>
  </div>
</section>

<nav class="next-prev" aria-label="Bölüm gezinme">
  <a href="{{ '/tutorials/so101-studio/first-run/' | relative_url }}">Önceki: İlk Kullanım</a>
  <a href="{{ '/tutorials/so101-studio/dashboard/' | relative_url }}">Sonraki: Dashboard</a>
</nav>
