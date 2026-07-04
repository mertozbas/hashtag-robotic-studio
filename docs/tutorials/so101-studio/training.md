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
  <h1>Dataset hazırsa Studio training planı üretir.</h1>
  <p class="lead">Eğitim maliyetli ve uzun sürebilir. Studio dataset kalite kontrolü, Hugging Face token, output repo ve feature mapping tamamlanınca çalıştırılabilir plan üretir; kullanıcı onayı olmadan Hub upload veya training başlatmaz.</p>
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
  <div class="section-head">
    <div>
      <p class="eyebrow">After training</p>
      <h2>Eğitilen policy nasıl kullanılır?</h2>
    </div>
    <p>Policy kullanmak training kadar güvenlik ister. Studio önce checkpoint’i indirir veya lokal path’ten okur, sonra kamera/state/action mapping’i dataset ile karşılaştırır.</p>
  </div>
  <div class="timeline">
    <div class="timeline-row" data-reveal><span>01</span><div><h3>Checkpoint seç</h3><p>Hugging Face model repo veya lokal `outputs/train/.../pretrained_model` path’i seçilir.</p></div></div>
    <div class="timeline-row" data-reveal><span>02</span><div><h3>Compatibility report al</h3><p>Policy’nin beklediği image key, state feature order ve action dimension mevcut robot config’i ile eşleşmelidir.</p></div></div>
    <div class="timeline-row" data-reveal><span>03</span><div><h3>Sim/dry-run çalıştır</h3><p>Gerçek robot öncesi simülasyon veya no-motion dry-run yapılır. Mapping unknown ise real rollout kapalı kalır.</p></div></div>
    <div class="timeline-row" data-reveal><span>04</span><div><h3>Real rollout için unlock al</h3><p>Passkey session, workspace_clear, emergency stop, duration limit ve SafetyGate sonucu olmadan policy gerçek robotta çalışmaz.</p></div></div>
    <div class="timeline-row" data-reveal><span>05</span><div><h3>Evaluation dataset kaydet</h3><p>Policy çalışırken ayrı `eval_*` dataset kaydedilir. Başarı/başarısızlık oranı Dataset Studio’da incelenir.</p></div></div>
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
