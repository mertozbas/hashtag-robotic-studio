from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs/tutorials/so101-studio-github-pages-guide.md"
PAGES_CONFIG = ROOT / "docs/_config.yml"
PAGES_INDEX = ROOT / "docs/index.md"
PAGES_LAYOUT = ROOT / "docs/_layouts/default.html"
PAGES_CSS = ROOT / "docs/assets/tutorial.css"
PAGES_WORKFLOW = ROOT / ".github/workflows/pages.yml"


def test_github_pages_tutorial_has_frontmatter_and_core_sections() -> None:
    guide = GUIDE.read_text(encoding="utf-8")

    assert guide.startswith("---\n")
    for field in [
        "layout: default",
        "permalink: /tutorials/so101-studio/",
        "lang: tr",
    ]:
        assert field in guide

    for heading in [
        "## 1. Bu kılavuz neyi kapsıyor?",
        "## 3. İlk açılış: dashboard mantığı",
        "## 5. API key vault ve model eğitimi",
        "## 7. Veri kaydı",
        "## 8. Hugging Face üzerinde eğitim",
        "## 10. Agent operasyon modu",
        "## 12. GitHub Pages medya planı",
        "## 14. Kaynaklar",
    ]:
        assert heading in guide


def test_tutorial_keeps_physical_motion_behind_safety_gate() -> None:
    guide = GUIDE.read_text(encoding="utf-8")

    for phrase in [
        "Fiziksel hareket başlatma",
        "SafetyGate",
        "kullanıcı unlock",
        "süre limiti",
        "acil stop",
        "workspace_clear",
        "Kalibrasyon dosyasını yazma veya üzerine yazma",
    ]:
        assert phrase in guide


def test_tutorial_links_official_sources_and_reuses_site_media_paths() -> None:
    guide = GUIDE.read_text(encoding="utf-8")

    for url in [
        "https://labs.hashtagworldcompany.com/product",
        "https://huggingface.co/docs/lerobot/en/so101",
        "https://huggingface.co/docs/lerobot/en/il_robots",
        "https://huggingface.co/docs/lerobot/en/act",
        "https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3",
        "https://github.com/huggingface/lerobot",
        "https://github.com/TheRobotStudio/SO-ARM100",
    ]:
        assert url in guide

    for asset_path in [
        "/assets/hero-follower.webp",
        "/assets/leader-follower.jpg",
        "/assets/anatomy/Joint1.mp4",
        "/assets/anatomy/Gripper.mp4",
    ]:
        assert asset_path in guide


def test_repository_contains_github_pages_site_shell() -> None:
    config = PAGES_CONFIG.read_text(encoding="utf-8")
    index = PAGES_INDEX.read_text(encoding="utf-8")
    layout = PAGES_LAYOUT.read_text(encoding="utf-8")
    css = PAGES_CSS.read_text(encoding="utf-8")
    workflow = PAGES_WORKFLOW.read_text(encoding="utf-8")

    assert 'baseurl: "/hashtag-robotic-studio"' in config
    assert "permalink: /" in index
    assert "/tutorials/so101-studio/" in index
    assert "{{ content }}" in layout
    assert "Hashtag Robotic Studio" in layout
    assert "color-scheme: dark" in css
    assert "actions/jekyll-build-pages@v1" in workflow
    assert "actions/deploy-pages@v4" in workflow
