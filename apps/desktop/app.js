const dictionaries = {
  tr: {
    "gateway.waiting": "Gateway bekleniyor",
    "gateway.ok": "Gateway bağlı",
    "nav.home": "Başlangıç",
    "nav.devices": "Cihazlar",
    "nav.calibration": "Kalibrasyon",
    "nav.agent": "Agent",
    "nav.diagnostics": "Tanılama",
    "home.title": "Operasyon durumu",
    "devices.title": "Cihazlar",
    "calibration.title": "Kalibrasyon",
    "agent.title": "Agent cockpit",
    "diagnostics.title": "Tanılama",
    "events.title": "Olaylar",
    "operation.blocked": "İşlem engellendi",
  },
  en: {
    "gateway.waiting": "Waiting for gateway",
    "gateway.ok": "Gateway connected",
    "nav.home": "Home",
    "nav.devices": "Devices",
    "nav.calibration": "Calibration",
    "nav.agent": "Agent",
    "nav.diagnostics": "Diagnostics",
    "home.title": "Operational status",
    "devices.title": "Devices",
    "calibration.title": "Calibration",
    "agent.title": "Agent cockpit",
    "diagnostics.title": "Diagnostics",
    "events.title": "Events",
    "operation.blocked": "Operation blocked",
  },
};

let language = "tr";

function t(key) {
  return dictionaries[language][key] || key;
}

async function fetchJson(path) {
  const response = await fetch(path);
  if (!response.ok) throw new Error(`${path}: ${response.status}`);
  return response.json();
}

function setText(id, value) {
  const node = document.getElementById(id);
  if (node) node.textContent = value;
}

function renderRows(id, rows) {
  const node = document.getElementById(id);
  node.innerHTML = rows
    .map((row) => `<div class="row"><span>${row.label}</span><strong>${row.value}</strong></div>`)
    .join("");
}

function applyLanguage() {
  setText("gateway-status", t("gateway.waiting"));
  setText("home-title", t("home.title"));
  setText("devices-title", t("devices.title"));
  setText("calibration-title", t("calibration.title"));
  setText("agent-title", t("agent.title"));
  setText("diagnostics-title", t("diagnostics.title"));
  setText("events-title", t("events.title"));
  document.querySelectorAll(".nav").forEach((button) => {
    button.textContent = t(`nav.${button.dataset.screen}`);
  });
  document.getElementById("language-toggle").textContent = language.toUpperCase();
}

async function refreshGateway() {
  const [health, capabilities, inventory, datasets, policy, agent] = await Promise.all([
    fetchJson('/health'),
    fetchJson('/capabilities'),
    fetchJson('/inventory'),
    fetchJson('/datasets'),
    fetchJson('/policies/compatibility'),
    fetchJson('/agent/tools'),
  ]);

  setText("gateway-status", `${t("gateway.ok")} · ${health.version}`);
  setText("readiness", `${health.mode} · physical_motion=${health.physical_motion_enabled}`);
  renderRows("device-list", [
    { label: "Packages", value: inventory.packages.filter((item) => item.installed).length },
    { label: "Ports", value: inventory.ports.length },
    { label: "Cameras", value: inventory.cameras.length },
    { label: "Capabilities", value: capabilities.capabilities.length },
  ]);
  renderRows(
    "calibration-list",
    inventory.calibrations.map((item) => ({ label: item.robot_id, value: item.present ? "present" : "missing" })),
  );
  renderRows(
    "agent-tools",
    agent.tools.map((tool) => ({ label: tool.name, value: tool.enabled ? "enabled" : "blocked" })),
  );
  setText("rollout-summary", policy.real_rollout_allowed ? "ready" : t("operation.blocked"));
  setText("diagnostics-log", JSON.stringify({ health, datasets, policy }, null, 2));
  document.getElementById("blockers").innerHTML = policy.blockers.map((item) => `<li>${item}</li>`).join("");
}

function connectEvents() {
  const feed = document.getElementById("event-feed");
  const source = new EventSource('/events');
  source.onmessage = (event) => {
    const row = document.createElement("div");
    row.textContent = event.data;
    feed.prepend(row);
  };
  source.addEventListener("operation_completed", (event) => {
    const row = document.createElement("div");
    row.textContent = event.data;
    feed.prepend(row);
  });
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

document.getElementById("language-toggle").addEventListener("click", () => {
  language = language === "tr" ? "en" : "tr";
  applyLanguage();
});

applyLanguage();
refreshGateway().catch((error) => setText("gateway-status", error.message));
connectEvents();
