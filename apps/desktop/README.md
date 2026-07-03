# Desktop Cockpit Prototype

Phase-2 desktop cockpit prototype is a static, dependency-light shell that can
be served by any local file server while the Tauri/Electron packaging spike is
pending.

Run with the gateway:

```bash
uvicorn services.local_gateway.app:app --reload
```

Open `http://127.0.0.1:8000/app/`.

Current surfaces:

- Home / `Başlangıç`
- Devices / `Cihazlar`
- Calibration / `Kalibrasyon`
- Agent
- Diagnostics / `Tanılama`

Gateway reads:

- `GET /health`
- `GET /capabilities`
- `GET /inventory`
- `GET /datasets`
- `GET /policies/compatibility`
- `GET /agent/tools`
- `GET /events` through SSE

Safety stance:

- STOP, motor lock, calibration write, and real rollout controls are visible,
  solid, high contrast, and blocked by default.
- No UI action talks directly to LeRobot, Strands Robots, serial ports, cameras,
  datasets, checkpoints, or hardware.
- The shell choice remains open; phase-8 records Tauri preferred with Electron
  fallback until the packaging spike is run.
