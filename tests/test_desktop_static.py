from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_desktop_cockpit_static_files_include_required_screens_and_i18n() -> None:
    index = (ROOT / "apps/desktop/index.html").read_text(encoding="utf-8")
    script = (ROOT / "apps/desktop/app.js").read_text(encoding="utf-8")

    for screen in ["home", "devices", "calibration", "live", "recording", "datasets", "policies", "agent", "diagnostics", "settings"]:
        assert f'data-screen="{screen}"' in index

    assert "const dictionaries" in script
    assert "Başlangıç" in script
    assert "Diagnostics" in script
    assert "fetchJson('/health')" in script
    assert "fetchJson('/capabilities')" in script
    assert "fetchJson('/settings/api-keys')" in script
    assert "new EventSource('/events')" in script
    assert "Hugging Face egitim ayari" in index
    assert "API key vault" in index


def test_desktop_cockpit_uses_high_contrast_critical_controls() -> None:
    css = (ROOT / "apps/desktop/styles.css").read_text(encoding="utf-8")
    index = (ROOT / "apps/desktop/index.html").read_text(encoding="utf-8")

    assert "stop-button" in index
    assert "motor-lock" in index
    assert "calibration-write" in index
    assert "real-rollout" in index
    assert ".critical.stop" in css
    assert "background: var(--red)" in css
    assert ".solid-panel" in css
    assert ".arm-visual" in css
