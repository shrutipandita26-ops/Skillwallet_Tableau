"""Render templates/ into static HTML in dist/. Run: python build.py"""
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from config import SITE, LINKS

ROOT = Path(__file__).parent
DIST = ROOT / "dist"

# endpoint -> (template, output file)
PAGES = {
    "home": ("index.html", "index.html"),
    "dashboard": ("dashboard.html", "dashboard.html"),
    "story": ("story.html", "story.html"),
    "portfolio": ("portfolio.html", "portfolio.html"),
}


def url_for(endpoint, **kw):
    if endpoint == "static":
        return "static/" + kw["filename"]
    return PAGES[endpoint][1]


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(ROOT / "static", DIST / "static")
    env = Environment(loader=FileSystemLoader(ROOT / "templates"))
    for page, (template, out) in PAGES.items():
        html = env.get_template(template).render(
            site=SITE, links=LINKS, page=page, url_for=url_for
        )
        (DIST / out).write_text(html, encoding="utf-8")
        print("built", out)


if __name__ == "__main__":
    main()
