# In-app guide and GitHub Pages publish prep

Status: active

Date: 2026-07-04

The desktop cockpit now includes a Turkish `Kılavuz` screen. It summarizes the SO101 + Studio user guide inside the app, links to the expected GitHub Pages tutorial URL, and keeps physical motion rules visible: user unlock, duration limit, emergency stop, workspace_clear, and SafetyGate are required before teleop, recording, motor test, or real rollout.

The repository now includes a GitHub Pages shell under `docs/`:

- `docs/_config.yml`
- `docs/_layouts/default.html`
- `docs/assets/tutorial.css`
- `docs/index.md`
- `docs/tutorials/so101-studio-github-pages-guide.md`

The workflow `.github/workflows/pages.yml` builds `docs/` with Jekyll and deploys with GitHub Pages Actions. Publishing is not complete until the repo has a GitHub remote and Pages is enabled for GitHub Actions.

No physical robot operation, calibration write, dataset deletion, Hub push, model download, or training job was run.
