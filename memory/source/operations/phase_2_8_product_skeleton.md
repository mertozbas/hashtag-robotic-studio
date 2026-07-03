# Phase 2-8 Product Skeleton

Status: active

Roadmap phases 2 through 8 are complete as no-motion product skeletons.

Durable facts:

- Static cockpit files live under `apps/desktop/`.
- Turkish is the default UI language and English is selectable through
  dictionaries in `apps/desktop/app.js`.
- The cockpit reads gateway health, capabilities, inventory, datasets, policy
  compatibility, agent tools, and SSE events.
- Read-only inventory endpoint: `GET /inventory`.
- Operation contract endpoints: `GET /operations/templates`,
  `POST /operations/request`, and `POST /operations/real-rollout/preflight`.
- Dataset endpoint: `GET /datasets`.
- Policy compatibility endpoint: `GET /policies/compatibility`.
- Agent tool taxonomy endpoint: `GET /agent/tools`.
- Packaging plan endpoint: `GET /packaging/plan`.
- Support bundle skeleton endpoint: `POST /support-bundle/export`, with secrets
  excluded by default.
- Stop event endpoint: `POST /stop`; no hardware disconnect is attempted in fake
  mode.
- Physical observation, physical motion, calibration write, destructive data,
  and real rollout remain blocked unless future current-turn hardware permission
  and full SafetyGate requirements are satisfied.

No physical robot movement, teleoperation, calibration write, dataset or
checkpoint deletion, model download, training job, Docker pull, external login,
or public publishing was performed for these skeleton phases.
