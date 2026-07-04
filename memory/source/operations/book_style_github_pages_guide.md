# Book-style GitHub Pages guide

Status: active

Date: 2026-07-04

The SO-101 guide has been converted from a single long scrolling page into a
book-style GitHub Pages documentation surface. The layout now uses `book: so101`
frontmatter, a shared left sidebar, active chapter links, and separate permalinks
under `/tutorials/so101-studio/` for setup, hardware, dashboard, SafetyGate, API
keys, dataset, training, agent mode, and sources.

Important behavior:

- Clicking sidebar chapters opens a real page/URL instead of scrolling to an
  anchor on one document.
- Hardware videos use `autoplay loop muted playsinline`, remove visible controls,
  and are backed by JavaScript that forces `controls = false`.
- The old robot-arm SVG was replaced by a cleaner animated system diagram for
  Studio UI, Local Gateway, SafetyGate, LeRobot Runtime, Strands Agent, and
  Hugging Face.
- Mobile uses a compact horizontal chapter bar so the first viewport does not
  become only navigation.
- Tests now enforce the multi-page book structure and ambient video behavior.

No physical robot operation, calibration write, dataset deletion, model download,
training job, or Hub push was run.
