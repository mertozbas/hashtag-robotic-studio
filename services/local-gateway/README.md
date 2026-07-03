# Local Gateway

The phase-1 local gateway is a non-actuating FastAPI prototype. It exposes
stable contracts for the future desktop app without probing serial ports,
opening cameras, importing LeRobot, or moving hardware.

Run locally:

```bash
uvicorn services.local_gateway.app:app --reload
```

Current endpoints:

- `GET /health`: app, version, status, local fake mode, and physical motion flag.
- `GET /capabilities`: deterministic fake/local capability inventory.
- `GET /inventory`: read-only packages, ports, cameras, calibration, and optional
  sim smoke status.
- `GET /operations/templates`: operation contract templates for observe, teleop,
  and recording workflows.
- `GET /events`: SSE replay stream for operation events.
- `POST /operations/fake`: runs a fake operation through SafetyGate and the
  operation state machine.
- `POST /operations/request`: evaluates an operation request through SafetyGate
  without running hardware.
- `POST /operations/real-rollout/preflight`: returns the default real-rollout
  blockers.
- `GET /datasets`: dataset inventory skeleton.
- `GET /policies/compatibility`: policy feature mapping and rollout blockers.
- `GET /agent/tools`: diagnostic, simulation, request, and physical tool scopes.
- `GET /packaging/plan`: desktop shell and gateway packaging plan.
- `GET /settings/api-keys`: API key provider status without secret values.
- `POST /settings/api-keys/{provider}`: accepts a secret value and returns only
  masked provider status.
- `POST /support-bundle/export`: support bundle skeleton with secrets excluded.
- `POST /stop`: stop event endpoint; no hardware disconnect is attempted in fake
  mode.

Implementation package:

- `../local_gateway/app.py`
- `../local_gateway/capabilities.py`
- `../local_gateway/events.py`
- `../local_gateway/operations.py`
- `../local_gateway/safety.py`

Phase-1 constraints:

- no physical robot movement
- no serial or camera probing
- physical observation and physical motion are blocked by default
- calibration write and destructive data paths are blocked by default
- future real operations must stay behind the safety contract in
  `../../docs/SAFETY_MODEL.md`
