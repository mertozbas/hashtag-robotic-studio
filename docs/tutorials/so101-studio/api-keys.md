---
layout: default
book: so101
guide_section: api-keys
title: "API Key Vault"
description: "Hashtag Robotic Studio API key ayarları ve secret masking modeli."
permalink: /tutorials/so101-studio/api-keys/
lang: tr
---

<header class="page-head">
  <p class="eyebrow">Chapter 05</p>
  <h1>Model eğitimi ve agent sağlayıcıları için tek key vault.</h1>
  <p class="lead">Hugging Face eğitim akışının merkezinde olacak. OpenAI, Anthropic, Gemini, GitHub, W&B, AWS ve Custom MCP keyleri aynı ayar yüzeyinde maskeli tutulur.</p>
</header>

<section class="doc-section">
  <table>
    <thead><tr><th>Provider</th><th>Kullanım</th><th>UI davranışı</th></tr></thead>
    <tbody>
      <tr><td>Hugging Face</td><td>Dataset upload, remote training, model download</td><td>Training hazırlığı için required provider.</td></tr>
      <tr><td>OpenAI / Anthropic / Gemini</td><td>Agent LLM sağlayıcıları</td><td>Connected state ve masked suffix dışında secret render edilmez.</td></tr>
      <tr><td>GitHub</td><td>Issue sync, release notes, repo workflow</td><td>Publish ve support iş akışları için ayrı scope düşünülür.</td></tr>
      <tr><td>Weights & Biases / AWS / Custom MCP</td><td>Tracking, artifact storage, tool connectors</td><td>Opsiyonel entegrasyon; production’da OS keychain’e taşınmalı.</td></tr>
    </tbody>
  </table>
</section>

<section class="doc-section">
  <div class="callout">
    <h2>Secret değeri geri dönmez.</h2>
    <p>Gateway `POST /settings/api-keys/{provider}` ile değer kabul eder, ama `GET /settings/api-keys` response içinde gerçek token dönmez. Support bundle ve log çıktıları da secret içermemelidir.</p>
  </div>
</section>

<section class="doc-section">
  <div class="timeline">
    <div class="timeline-row" data-reveal><span>01</span><div><h3>Hugging Face key ekle</h3><p>Ayarlar → API Key Vault → Hugging Face alanına write-access token gir. Dataset upload, remote training ve policy download için bu provider gerekir.</p></div></div>
    <div class="timeline-row" data-reveal><span>02</span><div><h3>Agent model provider seç</h3><p>OpenAI, Anthropic veya Gemini keylerinden biri agent modu için bağlanır. Bu key robot hareketini tek başına açmaz; sadece agent reasoning sağlar.</p></div></div>
    <div class="timeline-row" data-reveal><span>03</span><div><h3>Tracking opsiyonel</h3><p>W&B veya AWS gibi provider’lar experiment tracking/artifact storage için opsiyoneldir. Müşteri ilk kullanımda zorunlu değildir.</p></div></div>
  </div>
</section>

<nav class="next-prev" aria-label="Bölüm gezinme">
  <a href="{{ '/tutorials/so101-studio/safety/' | relative_url }}">Önceki: SafetyGate</a>
  <a href="{{ '/tutorials/so101-studio/dataset/' | relative_url }}">Sonraki: Dataset Kaydı</a>
</nav>
