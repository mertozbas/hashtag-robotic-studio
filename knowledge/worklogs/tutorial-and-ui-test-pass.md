# Tutorial and UI test pass

Date: 2026-07-04

## Scope

- Added a GitHub Pages compatible Turkish tutorial for SO-101 and Hashtag Robotic Studio.
- Kept the guide operational rather than marketing-only: dashboard screens, safety gates, API key vault, dataset recording, Hugging Face training, policy compatibility, agent tools, diagnostics, and support bundle behavior.
- Reused the public product page direction and local website media paths without copying large media into this repo.
- Added UI contract tests for desktop cockpit navigation, endpoint usage, secret masking, provider matrix, responsive layout, critical controls, and tutorial source coverage.

## Important paths

- Tutorial: `docs/tutorials/so101-studio-github-pages-guide.md`
- UI contract tests: `tests/test_ui_contracts.py`
- Tutorial content tests: `tests/test_tutorial_content.py`
- Website source assets: `/Users/macmert/hashtag-robotic/labs-redesign/assets/`
- Assembly videos: `/Users/macmert/hashtag-robotic/hashtag-robotics-montaj-animasyon/web/`

## Notes

- No physical robot command was run.
- No calibration file was read, written, or overwritten.
- No large video or image asset was copied into the product repo.
