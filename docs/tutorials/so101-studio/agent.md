---
layout: default
book: so101
guide_section: agent
title: "Agent Modu"
description: "Strands agent tool izinleri ve SO-101 operation contract modeli."
permalink: /tutorials/so101-studio/agent/
lang: tr
---

<header class="page-head">
  <p class="eyebrow">Chapter 08</p>
  <h1>Agent sohbet kutusu değil, kontratlı robot operatörü.</h1>
  <p class="lead">Agent robotu serbest sürmez. Diagnose ve simulation güvenli tool’lardır; physical request/control tool’ları SafetyGate, passkey unlock ve session scope olmadan kapalıdır.</p>
</header>

<section class="doc-section">
  <div class="card-grid">
    <div class="panel" data-reveal><h3>diagnose_setup</h3><p>Kurulum blokajlarını okur. Fiziksel hareket yok.</p></div>
    <div class="panel" data-reveal><h3>simulate_policy</h3><p>Sim/dry-run planı üretir. Donanım opt-in değildir.</p></div>
    <div class="panel warning" data-reveal><h3>request_teleop_session</h3><p>Fiziksel hareket ister; kullanıcı unlock ve operation contract gerekir.</p></div>
    <div class="panel danger" data-reveal><h3>run_real_policy</h3><p>Real rollout. Mapping, calibration, duration ve stop path eksikse bloklu kalır.</p></div>
    <div class="panel" data-reveal><h3>support_bundle</h3><p>Tanılama export eder; secret değerleri dahil edilmez.</p></div>
    <div class="panel" data-reveal><h3>tool stream</h3><p>Kullanıcı agent’in hangi tool’u neden çağırdığını görür.</p></div>
  </div>
</section>

<section class="doc-section">
  <div class="timeline">
    <div class="timeline-row" data-reveal><span>01</span><div><h3>Kullanıcı hedef verir</h3><p>Örnek: “Bu objeyi kavrama task’ı için kayıt planı hazırla.” Agent önce plan ve blocker listesi üretir.</p></div></div>
    <div class="timeline-row" data-reveal><span>02</span><div><h3>Agent tool çağırır</h3><p>`diagnose_setup`, `create_recording_plan` veya `simulate_policy` gibi no-motion tool’lar serbesttir.</p></div></div>
    <div class="timeline-row" data-reveal><span>03</span><div><h3>Fiziksel işlem isterse request oluşturur</h3><p>`request_teleop_session` veya `run_real_policy` doğrudan hareket ettirmez; operation request oluşturur.</p></div></div>
    <div class="timeline-row" data-reveal><span>04</span><div><h3>Kullanıcı unlock verir</h3><p>Passkey unlock ve SafetyGate geçerse sadece o session için bounded physical control tool’ları açılır.</p></div></div>
    <div class="timeline-row" data-reveal><span>05</span><div><h3>Tool stream izlenir</h3><p>Kullanıcı hangi tool’un neden çağrıldığını, hangi blocker’ın kaldığını ve STOP event’lerini görür.</p></div></div>
  </div>
</section>

<section class="doc-section">
  <div class="diagram-frame" data-reveal>
    <img src="{{ '/assets/so101-loop.svg' | relative_url }}" alt="Agent, gateway, SafetyGate ve robot runtime diyagramı">
  </div>
</section>

<nav class="next-prev" aria-label="Bölüm gezinme">
  <a href="{{ '/tutorials/so101-studio/training/' | relative_url }}">Önceki: Hugging Face Eğitim</a>
  <a href="{{ '/tutorials/so101-studio/sources/' | relative_url }}">Sonraki: Kaynaklar</a>
</nav>
