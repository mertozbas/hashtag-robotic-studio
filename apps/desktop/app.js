const dictionaries = {
  tr: {
    "gateway.waiting": "Gateway bekleniyor",
    "gateway.ok": "Gateway bagli",
    "nav.home": "Başlangıç",
    "nav.devices": "Cihazlar",
    "nav.calibration": "Kalibrasyon",
    "nav.live": "Canlı Kontrol",
    "nav.recording": "Kayıt",
    "nav.datasets": "Datasetler",
    "nav.policies": "Policyler",
    "nav.agent": "Agent",
    "nav.diagnostics": "Tanılama",
    "nav.settings": "Ayarlar",
    "operation.blocked": "İşlem engellendi",
  },
  en: {
    "gateway.waiting": "Waiting for gateway",
    "gateway.ok": "Gateway connected",
    "nav.home": "Home",
    "nav.devices": "Devices",
    "nav.calibration": "Calibration",
    "nav.live": "Live Control",
    "nav.recording": "Recording",
    "nav.datasets": "Datasets",
    "nav.policies": "Policies",
    "nav.agent": "Agent",
    "nav.diagnostics": "Diagnostics",
    "nav.settings": "Settings",
    "operation.blocked": "Operation blocked",
  },
};

let language = "tr";
let state = {};

function t(key) {
  return dictionaries[language][key] || key;
}

async function fetchJson(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });
  if (!response.ok) throw new Error(`${path}: ${response.status}`);
  return response.json();
}

function setText(id, value) {
  const node = document.getElementById(id);
  if (node) node.textContent = value;
}

function row(label, value, detail = "") {
  return `<div class="row"><span>${label}${detail ? `<small>${detail}</small>` : ""}</span><strong>${value}</strong></div>`;
}

function renderRows(id, rows) {
  document.getElementById(id).innerHTML = rows.map((item) => row(item.label, item.value, item.detail)).join("");
}

function providerCard(provider) {
  const status = provider.connected ? `Bagli ...${provider.last_four}` : "Bagli degil";
  return `
    <article class="key-card" data-provider="${provider.provider}">
      <strong>${provider.label}</strong>
      <span class="key-status">${status} · ${provider.required_for.join(", ")}</span>
      <form data-secret-form="${provider.provider}">
        <input type="password" autocomplete="off" placeholder="${provider.label} API key" />
        <button class="secondary" type="submit">Kaydet</button>
      </form>
    </article>`;
}

function readinessScore() {
  const inventory = state.inventory;
  const policy = state.policy;
  if (!inventory || !policy) return 0;
  let score = 20;
  if (state.health?.status === "ok") score += 15;
  if (inventory.ports.length > 0) score += 15;
  if (inventory.cameras.length > 0) score += 10;
  if (inventory.calibrations.some((item) => item.present)) score += 15;
  if (state.secrets?.providers?.some((item) => item.provider === "huggingface" && item.connected)) score += 10;
  if (policy.real_rollout_allowed) score += 15;
  return Math.min(score, 100);
}

function renderPreflight() {
  const inventory = state.inventory || { ports: [], cameras: [], calibrations: [] };
  const hfConnected = state.secrets?.providers?.some((item) => item.provider === "huggingface" && item.connected);
  const steps = [
    ["Gateway", state.health?.status === "ok", "Local gateway aktif"],
    ["Follower port", inventory.ports.length > 0, inventory.ports.length ? `${inventory.ports.length} aday` : "USB port secilecek"],
    ["Kamera", inventory.cameras.length > 0, "Front / wrist mapping bekliyor"],
    ["Kalibrasyon", inventory.calibrations.some((item) => item.present), "Follower calibration gerekli"],
    ["E-stop", false, "Fiziksel stop path test edilecek"],
    ["Hugging Face", hfConnected, "Model egitimi icin HF token"],
  ];
  document.getElementById("preflight-list").innerHTML = steps
    .map(([label, ready, detail]) => `<li class="${ready ? "ready" : "blocked"}"><span>${label}<small>${detail}</small></span><strong>${ready ? "Hazir" : "Eksik"}</strong></li>`)
    .join("");
}

function renderDashboard() {
  const score = readinessScore();
  setText("readiness-score", `${score}%`);
  setText("metric-gateway", state.health?.status === "ok" ? "Bagli" : "Yok");
  setText("metric-follower", state.inventory?.ports?.length ? "Aday var" : "Secilmedi");
  setText("metric-leader", "Opsiyonel");
  setText("metric-safety", state.policy?.real_rollout_allowed ? "Hazir" : "Bloklu");
  setText("recommended-action", score < 50 ? "Follower port, kamera ve kalibrasyon durumunu tamamla." : "HF token ve policy mapping kontrollerini tamamla.");
  renderPreflight();
}

function renderInventory() {
  const inventory = state.inventory;
  renderRows("port-list", (inventory.ports.length ? inventory.ports : [{ path: "Port adayi yok", confidence: "blocked" }]).map((item) => ({
    label: item.path,
    value: item.safe_to_use ? "Hazir" : "Secim gerekli",
    detail: item.confidence || item.role_hint,
  })));
  renderRows("camera-list", inventory.cameras.map((item) => ({
    label: item.label,
    value: item.available ? "Algilandi" : "Bekliyor",
    detail: item.safe_to_open ? "preview hazir" : "preview kapali",
  })));
  renderRows("calibration-list", inventory.calibrations.map((item) => ({
    label: `${item.role} · ${item.robot_id}`,
    value: item.present ? "Var" : "Eksik",
    detail: item.write_allowed ? "write enabled" : "write locked",
  })));
}

function renderOperations() {
  renderRows("operation-template-list", state.templates.templates.map((item) => ({
    label: item.type,
    value: item.physical_motion ? "Motion" : "Observe",
    detail: item.required_inputs.join(", "),
  })));
}

function renderDatasetsAndPolicy() {
  renderRows("dataset-list", state.datasets.datasets.map((item) => ({
    label: item.id,
    value: `${item.episodes} episode`,
    detail: item.blockers.join(", "),
  })));
  const policy = state.policy;
  renderRows("policy-report", [
    { label: "Policy", value: policy.policy_id, detail: policy.source },
    { label: "Action dimension", value: policy.expected_action_dimension || "unknown", detail: policy.mapping.unit_status },
    { label: "Remote code trust", value: policy.remote_code_trusted ? "Granted" : "Required", detail: policy.remote_code_trust_required ? "explicit" : "not required" },
    { label: "Real rollout", value: policy.real_rollout_allowed ? "Ready" : "Blocked", detail: policy.blockers.join(", ") },
  ]);
  setText("rollout-summary", policy.real_rollout_allowed ? "Ready" : t("operation.blocked"));
  document.getElementById("blockers").innerHTML = policy.blockers.map((item) => `<li>${item}</li>`).join("");
}

function renderAgentAndSettings() {
  renderRows("agent-tools", state.agent.tools.map((tool) => ({
    label: tool.name,
    value: tool.enabled ? "Enabled" : "Blocked",
    detail: `${tool.permission_scope} · ${tool.category}`,
  })));
  document.getElementById("api-key-grid").innerHTML = state.secrets.providers.map(providerCard).join("");
  document.querySelectorAll("[data-secret-form]").forEach((form) => {
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const provider = form.dataset.secretForm;
      const input = form.querySelector("input");
      if (!input.value.trim()) return;
      await fetchJson(`/settings/api-keys/${provider}`, {
        method: "POST",
        body: JSON.stringify({ value: input.value.trim() }),
      });
      input.value = "";
      await refreshGateway();
    });
  });
}

function renderDiagnostics() {
  setText("diagnostics-log", JSON.stringify({
    health: state.health,
    inventory: state.inventory,
    policy: state.policy,
    secrets: { providers: state.secrets.providers.map((item) => ({ provider: item.provider, connected: item.connected, last_four: item.last_four })) },
  }, null, 2));
}

async function refreshGateway() {
  const [health, capabilities, inventory, datasets, policy, agent, templates, secrets] = await Promise.all([
    fetchJson('/health'),
    fetchJson('/capabilities'),
    fetchJson('/inventory'),
    fetchJson('/datasets'),
    fetchJson('/policies/compatibility'),
    fetchJson('/agent/tools'),
    fetchJson('/operations/templates'),
    fetchJson('/settings/api-keys'),
  ]);
  state = { health, capabilities, inventory, datasets, policy, agent, templates, secrets };
  setText("gateway-status", `${t("gateway.ok")} · ${health.version}`);
  setText("robot-mode", `${health.mode} · motion=${health.physical_motion_enabled}`);
  setText("secret-storage", secrets.storage);
  renderDashboard();
  renderInventory();
  renderOperations();
  renderDatasetsAndPolicy();
  renderAgentAndSettings();
  renderDiagnostics();
}

function applyLanguage() {
  setText("gateway-status", t("gateway.waiting"));
  document.querySelectorAll(".nav").forEach((button) => {
    button.textContent = t(`nav.${button.dataset.screen}`);
  });
  document.getElementById("language-toggle").textContent = language.toUpperCase();
}

function connectEvents() {
  const feed = document.getElementById("event-feed");
  const source = new EventSource('/events');
  const append = (text) => {
    const rowNode = document.createElement("div");
    rowNode.className = "row";
    rowNode.innerHTML = `<span>${text}</span><strong>event</strong>`;
    feed.prepend(rowNode);
  };
  source.onmessage = (event) => append(event.data);
  source.addEventListener("operation_completed", (event) => append(event.data));
  source.addEventListener("api_key_updated", (event) => append(event.data));
  source.onerror = () => source.close();
}

document.querySelectorAll(".nav").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll(".nav").forEach((item) => item.classList.remove("active"));
    document.querySelectorAll(".screen").forEach((item) => item.classList.remove("active"));
    button.classList.add("active");
    document.querySelector(`[data-panel="${button.dataset.screen}"]`).classList.add("active");
  });
});

document.querySelectorAll("[data-jump]").forEach((button) => {
  button.addEventListener("click", () => document.querySelector(`[data-screen="${button.dataset.jump}"]`).click());
});

document.getElementById("language-toggle").addEventListener("click", () => {
  language = language === "tr" ? "en" : "tr";
  applyLanguage();
});

document.getElementById("refresh-button").addEventListener("click", () => refreshGateway());
document.getElementById("device-refresh").addEventListener("click", () => refreshGateway());
document.getElementById("support-bundle-button").addEventListener("click", async () => {
  await fetchJson('/support-bundle/export', { method: "POST" });
  await refreshGateway();
});
document.getElementById("stop-button").addEventListener("click", async () => {
  await fetchJson('/stop', { method: "POST" });
});

applyLanguage();
refreshGateway().catch((error) => setText("gateway-status", error.message));
connectEvents();
