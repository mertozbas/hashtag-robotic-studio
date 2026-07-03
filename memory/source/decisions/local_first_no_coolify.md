# Local-first And No Coolify Decision

Status: active

Coolify and self-hosted PaaS infrastructure are out of scope for Hashtag Robotic Studio.

Reasoning:

- The robot customer experience must work locally without a cloud backend.
- Policy download, dataset upload, Hugging Face auth, support bundle export, and updates can be implemented directly inside the app when needed.
- Adding a self-hosted PaaS would increase operational surface before there is a concrete product need.

Decision:

- Keep robot runtime, UI, agent runtime, dataset recording, policy validation, and diagnostics local-first.
- Add cloud-facing integrations only as direct app connectors, not as a required hosted platform.

