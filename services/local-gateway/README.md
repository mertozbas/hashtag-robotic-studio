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
- `GET /events`: SSE replay stream for operation events.
- `POST /operations/fake`: runs a fake operation through SafetyGate and the
  operation state machine.

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
- future real operations must stay behind the safety contract in
  `../../docs/SAFETY_MODEL.md`
