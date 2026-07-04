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
- Guide / `Kılavuz`
- Devices / `Cihazlar`
- Calibration / `Kalibrasyon`
- Live Control / `Canlı Kontrol`
- Recording / `Kayıt`
- Datasets / `Datasetler`
- Policies / `Policyler`
- Agent
- Diagnostics / `Tanılama`
- Settings / `Ayarlar`

Gateway reads:

- `GET /health`
- `GET /capabilities`
- `GET /inventory`
- `GET /datasets`
- `GET /policies/compatibility`
- `GET /agent/tools`
- `GET /settings/api-keys`
- `POST /settings/api-keys/{provider}`
- `GET /events` through SSE

Safety stance:

- STOP, motor lock, calibration write, and real rollout controls are visible,
  solid, high contrast, and blocked by default.
- No UI action talks directly to LeRobot, Strands Robots, serial ports, cameras,
  datasets, checkpoints, or hardware.
- API key values are submitted to the local gateway but not rendered back,
  included in diagnostics, or included in support bundle payloads.
- The in-app `Kılavuz` screen mirrors the customer guide and links to the
  GitHub Pages tutorial path prepared under `docs/tutorials/`.
- The shell choice remains open; phase-8 records Tauri preferred with Electron
  fallback until the packaging spike is run.
