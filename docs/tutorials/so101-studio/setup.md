---
layout: default
book: so101
guide_section: setup
title: "SO-101 Kurulum Akışı"
description: "SO-101 robot kolunu Hashtag Robotic Studio ile güvenli kurma akışı."
permalink: /tutorials/so101-studio/setup/
lang: tr
---

<header class="page-head">
  <p class="eyebrow">Chapter 01</p>
  <h1>Kurulum önce gözlem, sonra güvenli bağlantı.</h1>
  <p class="lead">Studio ilk çalıştığında robotu hareket ettirmez. Önce profil seçer, cihazları okur, calibration dosyalarını doğrular ve kullanıcıya güvenli bir readiness haritası verir.</p>
</header>

<section class="doc-section">
  <div class="timeline">
    <div class="timeline-row" data-reveal><span>01</span><div><h3>Dil ve robot profili</h3><p>Türkçe varsayılan gelir. Kullanıcı follower-only, leader + follower veya simulation-only profilini seçer.</p></div></div>
    <div class="timeline-row" data-reveal><span>02</span><div><h3>Device discovery</h3><p>Follower port adayları, leader port adayları, kamera adayları ve OS izinleri salt okunur şekilde listelenir.</p></div></div>
    <div class="timeline-row" data-reveal><span>03</span><div><h3>Calibration check</h3><p>Calibration dosyası varlığı, robot role eşleşmesi, backup durumu ve calibration yaşı kontrol edilir. Dosya yazılmaz.</p></div></div>
    <div class="timeline-row" data-reveal><span>04</span><div><h3>Camera preview</h3><p>Front ve opsiyonel wrist camera için FPS, latency ve frame health gösterilir.</p></div></div>
    <div class="timeline-row" data-reveal><span>05</span><div><h3>Observation-only connect</h3><p>Seri port davranışı ve package import durumu incelenir. Motor komutu gönderilmez.</p></div></div>
    <div class="timeline-row" data-reveal><span>06</span><div><h3>Bounded motion test</h3><p>Sadece kullanıcı unlock verirse kısa süreli, düşük hız limitli ve görünür stop path olan test açılır.</p></div></div>
  </div>
</section>

<section class="doc-section">
  <div class="callout warning">
    <h2>Kurulum ekranı robotu hazır gösterse bile hareket otomatik başlamaz.</h2>
    <p>Teleop, kayıt, motor testi ve real policy rollout fiziksel hareket sınıfındadır. Her biri explicit operation contract, SafetyGate sonucu ve kullanıcı unlock ister.</p>
  </div>
</section>

<nav class="next-prev" aria-label="Bölüm gezinme">
  <a href="{{ '/tutorials/so101-studio/' | relative_url }}">Önceki: Başlangıç</a>
  <a href="{{ '/tutorials/so101-studio/hardware/' | relative_url }}">Sonraki: Robot ve Parçalar</a>
</nav>
