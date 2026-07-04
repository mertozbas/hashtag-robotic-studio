# Customer first-run SO-101 guide

Status: active

Date: 2026-07-04

The GitHub Pages SO-101 guide has been expanded from architecture-oriented docs
into a customer first-run manual.

Durable decisions:

- Customer distribution should be an installer/app bundle, not a pip/git-clone
  workflow.
- GitHub remains a developer preview path: clone the repo, create a venv,
  install `.[dev]`, run the local gateway, and open `/app/`.
- The current public preview must disclose that the gateway is `local_fake` and
  `physical_motion_enabled=false`.
- SO-101 setup docs now answer: install path, USB connection, automatic discovery
  limits, follower/leader assignment, camera mapping, calibration check,
  observation-only connect, bounded motor test, teleop, dataset recording,
  training, policy compatibility, and real rollout.
- The safety model now references Scout the Rover's WebAuthn/passkey pattern as
  inspiration for Hashtag Studio's passkey unlock layer: Face ID, Touch ID,
  Windows Hello, or security key for short-lived physical-motion sessions.
- Dataset, training, and agent pages now describe customer actions instead of
  only SDK concepts.

No physical robot operation, calibration write, dataset deletion, model download,
training job, or Hub push was run.
