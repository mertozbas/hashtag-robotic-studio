---
layout: default
book: so101
guide_section: training
title: "Hugging Face Eğitim"
description: "SO-101 datasetlerinden Hugging Face üzerinde policy eğitim hazırlığı."
permalink: /tutorials/so101-studio/training/
lang: tr
---

<header class="page-head">
  <p class="eyebrow">Chapter 07</p>
  <h1>Training otomatik başlatılmaz; önce plan ve uyumluluk hazırlanır.</h1>
  <p class="lead">Eğitim maliyetli ve uzun sürebilir. Studio dataset kalite kontrolü, Hugging Face token, output repo ve feature mapping tamamlanınca çalıştırılabilir plan üretir.</p>
</header>

<section class="doc-section">
  <div class="split">
    <div class="panel" data-reveal>
      <h2>Minimum hazırlık</h2>
      <ul>
        <li>Hugging Face API key bağlı.</li>
        <li>Dataset repo/path ve episode kalite durumu doğrulanmış.</li>
        <li>Policy family seçilmiş: ACT, Diffusion Policy veya SmolVLA.</li>
        <li>Output model repo belirlenmiş.</li>
        <li>Expected image/state/action feature eşleşmesi tamamlanmış.</li>
      </ul>
    </div>
    <pre class="terminal" data-reveal><code># Studio bunu doğrudan çalıştırmaz; güvenli plan olarak üretir.
hf auth login
lerobot-record --dataset.repo_id=&lt;user&gt;/&lt;dataset&gt;
lerobot-train --policy.type=act --dataset.repo_id=&lt;user&gt;/&lt;dataset&gt;</code></pre>
  </div>
</section>

<section class="doc-section">
  <div class="dashboard-map compact">
    <div class="screen-card" data-reveal><span>ACT</span><h3>Imitation learning baseline</h3><p>SO-101 için başlangıç policy ailesi olarak UI’da görünür.</p></div>
    <div class="screen-card" data-reveal><span>Diffusion</span><h3>Trajectory quality</h3><p>Dataset kalitesi iyi değilse rollout öncesi risk artar.</p></div>
    <div class="screen-card" data-reveal><span>SmolVLA</span><h3>Vision-language-action</h3><p>Feature mapping ve kamera isimleri daha kritik hale gelir.</p></div>
  </div>
</section>

<nav class="next-prev" aria-label="Bölüm gezinme">
  <a href="{{ '/tutorials/so101-studio/dataset/' | relative_url }}">Önceki: Dataset Kaydı</a>
  <a href="{{ '/tutorials/so101-studio/agent/' | relative_url }}">Sonraki: Agent Modu</a>
</nav>
