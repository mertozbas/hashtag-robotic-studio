from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs/tutorials/so101-studio-github-pages-guide.md"
GUIDE_DIR = ROOT / "docs/tutorials/so101-studio"
PAGES_CONFIG = ROOT / "docs/_config.yml"
PAGES_INDEX = ROOT / "docs/index.md"
PAGES_LAYOUT = ROOT / "docs/_layouts/default.html"
PAGES_CSS = ROOT / "docs/assets/tutorial.css"
PAGES_JS = ROOT / "docs/assets/tutorial.js"
ANIMATED_SVG = ROOT / "docs/assets/so101-loop.svg"
PAGES_WORKFLOW = ROOT / ".github/workflows/pages.yml"


def test_github_pages_tutorial_has_frontmatter_and_core_sections() -> None:
    guide = GUIDE.read_text(encoding="utf-8")

    assert guide.startswith("---\n")
    for field in [
        "layout: default",
        "book: so101",
        "guide_section: overview",
        "permalink: /tutorials/so101-studio/",
        "lang: tr",
    ]:
        assert field in guide

    for permalink in [
        "/tutorials/so101-studio/setup/",
        "/tutorials/so101-studio/hardware/",
        "/tutorials/so101-studio/dashboard/",
        "/tutorials/so101-studio/safety/",
        "/tutorials/so101-studio/api-keys/",
        "/tutorials/so101-studio/dataset/",
        "/tutorials/so101-studio/training/",
        "/tutorials/so101-studio/agent/",
        "/tutorials/so101-studio/sources/",
    ]:
        assert permalink in guide


def test_tutorial_is_a_multi_page_book_not_single_scroll_page() -> None:
    expected_pages = {
        "setup.md": "guide_section: setup",
        "hardware.md": "guide_section: hardware",
        "dashboard.md": "guide_section: dashboard",
        "safety.md": "guide_section: safety",
        "api-keys.md": "guide_section: api-keys",
        "dataset.md": "guide_section: dataset",
        "training.md": "guide_section: training",
        "agent.md": "guide_section: agent",
        "sources.md": "guide_section: sources",
    }

    for filename, section in expected_pages.items():
        page = (GUIDE_DIR / filename).read_text(encoding="utf-8")
        assert "book: so101" in page
        assert section in page
        assert "permalink: /tutorials/so101-studio/" in page
        assert "next-prev" in page

    layout = PAGES_LAYOUT.read_text(encoding="utf-8")
    assert 'page.book == "so101"' in layout
    assert "book-sidebar" in layout
    assert "book-nav" in layout
    assert "page.guide_section" in layout


def test_tutorial_keeps_physical_motion_behind_safety_gate() -> None:
    guide = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [GUIDE, *(sorted(GUIDE_DIR.glob("*.md")))]
    )

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
    guide = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [GUIDE, *(sorted(GUIDE_DIR.glob("*.md")))]
    )

    for url in [
        "https://labs.hashtagworldcompany.com/product",
        "https://strands-labs.github.io/robots/",
        "https://huggingface.co/docs/lerobot/en/so101",
        "https://huggingface.co/docs/lerobot/en/il_robots",
        "https://huggingface.co/docs/lerobot/en/act",
        "https://huggingface.co/docs/lerobot/en/lerobot-dataset-v3",
        "https://github.com/huggingface/lerobot",
        "https://github.com/TheRobotStudio/SO-ARM100",
    ]:
        assert url in guide

    for asset_path in [
        "/assets/media/hero-follower.webp",
        "/assets/media/leader-follower.jpg",
        "/assets/anatomy/Joint1.mp4",
        "/assets/anatomy/Joint2.mp4",
        "/assets/anatomy/Joint3.mp4",
        "/assets/anatomy/Gripper.mp4",
        "/assets/so101-loop.svg",
    ]:
        assert asset_path in guide


def test_repository_contains_github_pages_site_shell() -> None:
    config = PAGES_CONFIG.read_text(encoding="utf-8")
    index = PAGES_INDEX.read_text(encoding="utf-8")
    layout = PAGES_LAYOUT.read_text(encoding="utf-8")
    css = PAGES_CSS.read_text(encoding="utf-8")
    script = PAGES_JS.read_text(encoding="utf-8")
    workflow = PAGES_WORKFLOW.read_text(encoding="utf-8")

    assert 'baseurl: "/hashtag-robotic-studio"' in config
    assert "permalink: /" in index
    assert "/tutorials/so101-studio/" in index
    assert "{{ content }}" in layout
    assert "/assets/tutorial.js" in layout
    assert "og:image" in layout
    assert "Hashtag Robotic Studio" in layout
    assert "color-scheme: dark" in css
    assert ".book-shell" in css
    assert ".book-sidebar" in css
    assert ".pipeline" in css
    assert "IntersectionObserver" in script
    assert "ambientVideos" in script
    assert "actions/jekyll-build-pages@v1" in workflow
    assert "actions/deploy-pages@v4" in workflow


def test_tutorial_visual_assets_are_present_and_active() -> None:
    guide = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [GUIDE, *(sorted(GUIDE_DIR.glob("*.md")))]
    )
    svg = ANIMATED_SVG.read_text(encoding="utf-8")
    tracked_files = set(
        subprocess.check_output(["git", "ls-files", "docs/assets"], cwd=ROOT, text=True).splitlines()
    )

    for relative_path in [
        "docs/assets/media/leader-follower.jpg",
        "docs/assets/media/hero-follower.webp",
        "docs/assets/media/leader.webp",
        "docs/assets/media/part-servo.jpg",
        "docs/assets/media/part-board.png",
        "docs/assets/media/part-gripper.png",
        "docs/assets/media/part-lerobot.png",
        "docs/assets/media/so101-ar.glb",
        "docs/assets/anatomy/Joint1.mp4",
        "docs/assets/anatomy/Joint2.mp4",
        "docs/assets/anatomy/Joint3.mp4",
        "docs/assets/anatomy/Gripper.mp4",
        "docs/assets/so101-loop.svg",
    ]:
        path = ROOT / relative_path
        assert path.exists(), relative_path
        assert path.stat().st_size > 1024, relative_path
        assert relative_path in tracked_files, relative_path

    assert "<video controls" not in guide
    assert "class=\"ambient-video\"" in guide
    assert "autoplay loop muted playsinline" in guide
    assert "preload=\"auto\"" in guide
    assert "<animateMotion" in svg
    assert "LeRobot Runtime" in svg
    assert "SafetyGate" in svg
    assert "Hugging Face" in svg
    assert "data-reveal" in guide
