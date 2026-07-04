# Rich GitHub Pages guide redesign

Date: 2026-07-04

## Scope

- Rebuilt the SO-101 + Studio GitHub Pages guide from a plain Markdown page into a richer product documentation page.
- Added active local media assets under `docs/assets/media/` and `docs/assets/anatomy/`.
- Added an animated SVG control-loop visual at `docs/assets/so101-loop.svg`.
- Added a small progressive enhancement script for scroll progress and reveal states.
- Updated the guide and docs home page to use hero, sticky TOC, pipeline cards, video cards, safety panels, source cards, and responsive layout.
- Expanded tests so the guide now requires real visual assets, active videos, animated SVG, layout shell, and JS hooks.

## Validation

- `python3 -m pytest`
- `python3 tools/verify_phase.py --phase phase-0`
- `python3 tools/verify_phase.py --phase phase-2`
- `python3 tools/verify_phase.py --phase phase-8`
- Secret pattern scan only found the existing fake Hugging Face test fixture.

## Reference Direction

- The redesign was influenced by the documentation ergonomics of `https://strands-labs.github.io/robots/`: visible navigation, code + diagram balance, animated/visual technical explanation, and sim-first/hardware opt-in framing.

## Notes

- No physical robot operation was run.
- Local Jekyll is not installed, so final Pages build verification must happen through GitHub Actions.
