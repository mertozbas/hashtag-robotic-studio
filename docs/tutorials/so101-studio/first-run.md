---
layout: default
book: so101
guide_section: first-run
title: "SO-101 İlk Kullanım"
description: "SO-101 robotu kurduktan ve USB kablolarını bağladıktan sonra adım adım ilk kullanım."
permalink: /tutorials/so101-studio/first-run/
lang: tr
---

<header class="page-head">
  <p class="eyebrow">Chapter 02</p>
  <h1>Robotu aldın, yazılımı kurdun, USB’leri taktın. Şimdi ne olacak?</h1>
  <p class="lead">Bu bölüm müşteri akışıdır. Terminal veya SDK bilgisi varsaymaz. Ama arka planda ne kontrol edildiğini de açık söyler: port, kamera, calibration, passkey unlock, SafetyGate, duration limit ve stop path.</p>
</header>

<section class="doc-section">
  <div class="timeline">
    <div class="timeline-row" data-reveal><span>01</span><div><h3>Studio’yu aç</h3><p>Başlangıç ekranı lokal gateway health check yapar. `Gateway online`, `Robot motion locked`, `STOP ready` durumlarını görmelisin.</p></div></div>
    <div class="timeline-row" data-reveal><span>02</span><div><h3>Giriş ve güvenlik kilidi</h3><p>İlk kurulumda admin passkey oluştur. Sonraki oturumlarda fiziksel robot işlemleri için Face ID, Touch ID, Windows Hello veya güvenlik anahtarı ile kısa süreli unlock alınır.</p></div></div>
    <div class="timeline-row" data-reveal><span>03</span><div><h3>Robot profilini seç</h3><p>Follower-only kullanacaksan tek kol profili, dataset teleop yapacaksan leader + follower profili seç. Simülasyon denemesi için simulation-only seç.</p></div></div>
    <div class="timeline-row" data-reveal><span>04</span><div><h3>USB portlarını tara</h3><p>Studio port adaylarını listeler. Otomatik tanıma yapabilir, ama role atamasını kullanıcı doğrular: `Bu port follower mı? Bu port leader mı?` Yanlış eşleşme fiziksel hareketi bloklar.</p></div></div>
    <div class="timeline-row" data-reveal><span>05</span><div><h3>Kamera seç</h3><p>Front camera zorunlu olabilir; wrist camera opsiyoneldir. Kamera isimleri dataset ve policy keyleriyle eşleşmelidir.</p></div></div>
    <div class="timeline-row" data-reveal><span>06</span><div><h3>Calibration kontrolü</h3><p>Studio calibration dosyasını okur, robot id ve role ile eşleştirir. Dosya yoksa veya role yanlışsa motor testi açılmaz. Calibration yazma ayrı, daha güçlü onay ister.</p></div></div>
    <div class="timeline-row" data-reveal><span>07</span><div><h3>Observation-only bağlan</h3><p>İlk bağlantı motor hareketi değildir. App sadece cihaz durumunu, kamera preview’ını ve runtime paketlerini doğrular.</p></div></div>
    <div class="timeline-row" data-reveal><span>08</span><div><h3>Kısa motor testi</h3><p>Workspace clear, emergency stop, duration limit ve passkey unlock tamamlanırsa düşük hızda kısa test açılır. STOP her zaman görünür kalır.</p></div></div>
    <div class="timeline-row" data-reveal><span>09</span><div><h3>Teleop veya kayıt seç</h3><p>Leader + follower doğrulandıysa Canlı Kontrol ile alıştırma yap. Hazır olunca Kayıt ekranında task ve episode planı oluştur.</p></div></div>
  </div>
</section>

<section class="doc-section">
  <div class="split">
    <div class="panel danger" data-reveal>
      <h2>Otomatik tanıma ne kadar otomatik?</h2>
      <p>Studio bağlı portları ve kameraları tarar, ama fiziksel hareket için kritik role bilgisini körlemesine kabul etmez. Follower ve leader eşleşmesi, calibration id, camera key mapping ve workspace onayı kullanıcıya gösterilir.</p>
    </div>
    <pre class="terminal" data-reveal><code>Readiness checklist:
  gateway: online
  passkey_session: valid
  follower_port: selected + verified
  leader_port: selected when teleop/recording
  calibration_id: matched
  camera_config: mapped
  emergency_stop: armed
  workspace_clear: confirmed
  duration_limit: set
  motion_state: locked until unlock</code></pre>
  </div>
</section>

<section class="doc-section">
  <div class="callout warning">
    <h2>İlk gün hedefi policy çalıştırmak değil, güvenli veri toplamaya hazırlanmak.</h2>
    <p>Önce portları doğru tanıt, kısa teleop ile leader/follower yönlerini doğrula, kamera açısını sabitle, 5-10 deneme episode’u kaydet ve Dataset Studio’da kalite kontrol yap. Policy rollout en son adımdır.</p>
  </div>
</section>

<nav class="next-prev" aria-label="Bölüm gezinme">
  <a href="{{ '/tutorials/so101-studio/setup/' | relative_url }}">Önceki: Kurulum / Install</a>
  <a href="{{ '/tutorials/so101-studio/hardware/' | relative_url }}">Sonraki: Robot ve Parçalar</a>
</nav>
