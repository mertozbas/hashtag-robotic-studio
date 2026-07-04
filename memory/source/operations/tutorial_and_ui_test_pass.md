# GitHub Pages tutorial and UI contract test pass

Status: active

Date: 2026-07-04

Hashtag Robotic Studio now has a GitHub Pages compatible Turkish SO-101 tutorial at `docs/tutorials/so101-studio-github-pages-guide.md`. The guide covers the desktop cockpit, SO-101 leader/follower usage, safety gates, API key vault, Hugging Face dataset/training flow, policy compatibility, agent operations, diagnostics, and support bundle behavior.

The guide intentionally references website-ready media paths instead of copying large files into this repo. The current local sources are:

- Product assets: `/Users/macmert/hashtag-robotic/labs-redesign/assets/`
- Assembly videos: `/Users/macmert/hashtag-robotic/hashtag-robotics-montaj-animasyon/web/`

UI coverage was expanded with `tests/test_ui_contracts.py` and `tests/test_tutorial_content.py`. These tests assert screen/panel mapping, gateway endpoint usage, secret masking, API provider coverage, responsive cockpit CSS, critical controls, Turkish training/safety surfaces, tutorial frontmatter, safety language, source links, and expected media paths.

No physical robot operation, calibration write, dataset deletion, Hub push, model download, or long training job was run during this pass.
