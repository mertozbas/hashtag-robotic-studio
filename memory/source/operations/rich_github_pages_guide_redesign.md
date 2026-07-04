# Rich GitHub Pages guide redesign

Status: active

Date: 2026-07-04

The SO-101 + Hashtag Robotic Studio guide has been redesigned from a plain Markdown document into a richer GitHub Pages product guide. The page now uses real local media assets, anatomy videos, an animated SVG control-loop visual, sticky table-of-contents navigation, pipeline cards, safety panels, provider tables, and source cards.

The redesign follows the documentation ergonomics observed in `https://strands-labs.github.io/robots/`: strong navigation, visual explanation, code/diagram balance, and clear sim-first or safety-gated hardware framing.

Important files:

- `docs/tutorials/so101-studio-github-pages-guide.md`
- `docs/assets/tutorial.css`
- `docs/assets/tutorial.js`
- `docs/assets/so101-loop.svg`
- `docs/assets/media/`
- `docs/assets/anatomy/`
- `tests/test_tutorial_content.py`

No physical robot operation, calibration write, dataset deletion, model download, Hub push, or training job was run.
