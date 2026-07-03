---
title: "Advanced Dashboard And API Key Vault"
type: worklog
status: active
area: "frontend"
tags: ["dashboard", "api-keys", "huggingface", "so101", "safety"]
created: 2026-07-04
updated: 2026-07-04
---

# Advanced Dashboard And API Key Vault

## Summary

The desktop cockpit was upgraded from a simple static shell into a more complete
product dashboard for connecting SO101 arms and preparing Hugging Face training.

## Context

Mert opened the dashboard and found the current skeleton too basic. He asked for
a more designed, product-like final dashboard that is ready for connecting robot
arms and includes settings for API keys, especially because model training will
use Hugging Face.

## Decision Or Finding

- Home is now a robot-readiness cockpit with an SO101 arm visual, readiness
  score, metric strip, and preflight checklist.
- Added product screens for devices, calibration, live control, recording,
  datasets, policies, agent, diagnostics, and settings.
- Policy screen includes Hugging Face training setup fields.
- Settings includes API key providers for Hugging Face, OpenAI, Anthropic,
  Google Gemini, GitHub, Weights & Biases, AWS, and custom MCP.
- Gateway accepts API key submissions but only returns masked provider status.
- Secret values are excluded from diagnostics and support bundle responses.

## Consequences

The UI is now closer to a customer-facing robot studio. Before a customer build,
the runtime-memory secret handling should be replaced with OS keychain storage
through the chosen desktop shell.

## Related

- `../../apps/desktop/index.html`
- `../../apps/desktop/app.js`
- `../../apps/desktop/styles.css`
- `../../services/local_gateway/app.py`
- `../../packages/contracts/models.py`
