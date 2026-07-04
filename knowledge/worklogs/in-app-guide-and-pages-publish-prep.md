# In-app guide and Pages publish prep

Date: 2026-07-04

## Scope

- Added an in-app `Kılavuz` screen to the desktop cockpit.
- Added a GitHub Pages site shell under `docs/` with Jekyll layout, tutorial CSS, and an index page.
- Added `.github/workflows/pages.yml` to build `docs/` with Jekyll and deploy through GitHub Pages Actions.
- Updated static/UI tests to cover the new guide screen and Pages shell.

## Validation

- `python3 -m pytest`
- `python3 tools/verify_phase.py --phase phase-0`
- `python3 tools/verify_phase.py --phase phase-2`
- `python3 tools/verify_phase.py --phase phase-8`
- FastAPI TestClient served `/app/`, `/app/app.js`, and `/app/styles.css`; the guide screen marker was present.

## Notes

- No physical robot command was run.
- The local git repository has no remote configured yet, so GitHub push/Pages publication still needs a remote repository target.
