# India Agricultural Crop Analysis: Flask + Tableau Public

Run locally: `pip install -r requirements.txt && python app.py`

Deploy on Render: push to GitHub, New > Web Service, pick the repo.
Build: `pip install -r requirements.txt`  Start: `gunicorn app:app`
(render.yaml already has these.) Edit the SITE dict in app.py for your name and links.
