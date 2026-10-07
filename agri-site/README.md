# India Agricultural Crop Analysis: static site + Tableau Public

Build: `pip install -r requirements.txt && python build.py` (output goes to dist/)
Preview: `python -m http.server -d dist 8000`

Deploy on Render: push to GitHub, New > Static Site, pick the repo.
Build command: `pip install -r requirements.txt && python build.py`
Publish directory: `dist`  (render.yaml already has these.)
Edit config.py for your name and links, then rebuild.
