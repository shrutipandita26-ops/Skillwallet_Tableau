import os
from flask import Flask, render_template

app = Flask(__name__)

# Edit these once; every page picks them up.
SITE = {
    "name": "Your Name",
    "tagline": "Data analyst in the making",
    "college": "Your College, City",
    "email": "you@example.com",
    "github": "https://github.com/your-username",
    "linkedin": "https://www.linkedin.com/in/your-username",
}

LINKS = {
    "dashboard": "https://public.tableau.com/views/Book1_Shruti_Agricultural_Dashboard/IndiaAgriculturalCropAnalysisDashboard",
    "story": "https://public.tableau.com/views/Shruti_Agricultural_story/AgriculturalOverview",
}


@app.context_processor
def inject_globals():
    return {"site": SITE, "links": LINKS}


@app.route("/")
def home():
    return render_template("index.html", page="home")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", page="dashboard")


@app.route("/story")
def story():
    return render_template("story.html", page="story")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", page="portfolio")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
