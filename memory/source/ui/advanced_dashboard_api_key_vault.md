# Advanced Dashboard And API Key Vault

Status: active

The cockpit UI has been upgraded into a product-style SO101 readiness dashboard.

Durable facts:

- Static cockpit files remain under `apps/desktop/`.
- The home screen now centers on SO101 arm connection readiness, preflight,
  SafetyGate blockers, and next safe actions.
- Navigation now includes Home, Devices, Calibration, Live Control, Recording,
  Datasets, Policies, Agent, Diagnostics, and Settings.
- Policy screen includes Hugging Face training setup fields.
- Settings includes API key providers for Hugging Face, OpenAI, Anthropic,
  Google Gemini, GitHub, Weights & Biases, AWS, and custom MCP.
- Gateway endpoints:
  - `GET /settings/api-keys`
  - `POST /settings/api-keys/{provider}`
- API key values are accepted by the gateway but never returned in API
  responses; only masked status is returned.
- Current storage is runtime memory. Customer packaging should replace this with
  OS keychain storage before production.
- Physical motion remains blocked by SafetyGate and no hardware movement is
  triggered by the dashboard.
