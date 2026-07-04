import re
from pathlib import Path

from services.local_gateway.studio import list_api_key_providers


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "apps/desktop/index.html"
SCRIPT = ROOT / "apps/desktop/app.js"
STYLES = ROOT / "apps/desktop/styles.css"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_navigation_screens_have_matching_panels_and_required_runtime_targets() -> None:
    index = _read(INDEX)
    screens = re.findall(r'data-screen="([^"]+)"', index)
    panels = re.findall(r'data-panel="([^"]+)"', index)

    assert screens == [
        "home",
        "devices",
        "calibration",
        "live",
        "recording",
        "datasets",
        "policies",
        "agent",
        "diagnostics",
        "settings",
    ]
    assert set(screens) == set(panels)

    for element_id in [
        "gateway-status",
        "readiness-score",
        "preflight-list",
        "port-list",
        "camera-list",
        "calibration-list",
        "operation-template-list",
        "dataset-list",
        "policy-report",
        "agent-tools",
        "api-key-grid",
        "diagnostics-log",
        "support-bundle-button",
        "stop-button",
    ]:
        assert f'id="{element_id}"' in index


def test_ui_uses_gateway_endpoint_contracts_without_secret_echoes() -> None:
    script = _read(SCRIPT)

    for endpoint in [
        "/health",
        "/capabilities",
        "/inventory",
        "/datasets",
        "/policies/compatibility",
        "/agent/tools",
        "/operations/templates",
        "/settings/api-keys",
        "/support-bundle/export",
        "/stop",
        "/events",
    ]:
        assert endpoint in script

    assert "method: \"POST\"" in script
    assert "input.value = \"\"" in script
    assert "last_four" in script
    assert "secret_values" not in script
    assert "secrets: { providers: state.secrets.providers.map" in script
    assert "value: input.value.trim()" in script


def test_api_key_provider_matrix_covers_training_agents_and_tool_connectors() -> None:
    providers = list_api_key_providers()
    provider_names = {provider.provider for provider in providers}

    assert provider_names == {
        "huggingface",
        "openai",
        "anthropic",
        "google",
        "github",
        "wandb",
        "aws",
        "custom_mcp",
    }
    huggingface = next(provider for provider in providers if provider.provider == "huggingface")
    assert {"dataset_upload", "remote_training", "model_download"} <= set(huggingface.required_for)
    assert all(provider.secret_returned is False for provider in providers)


def test_cockpit_css_preserves_operational_layout_and_critical_controls() -> None:
    css = _read(STYLES)

    assert "grid-template-columns: 210px minmax(0, 1fr) 310px" in css
    assert ".workspace { min-width: 0; padding: 16px; overflow: auto; }" in css
    assert ".table-list, #event-feed, #blockers, pre" in css
    assert ".critical.stop { background: var(--red); color: white; }" in css
    assert "@media (max-width: 1120px)" in css
    assert "@media (max-width: 760px)" in css
    assert "letter-spacing: 0;" in css


def test_turkish_first_cockpit_copy_exposes_training_and_safety_surfaces() -> None:
    index = _read(INDEX)

    for text in [
        "Robot kollarini baglamaya hazir cockpit",
        "Fiziksel hareket kilidi",
        "Hugging Face egitim ayari",
        "Policy compatibility",
        "Agent operasyon cockpit",
        "API key vault",
        "Secret politikasi",
    ]:
        assert text in index
