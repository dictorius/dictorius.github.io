from flask import render_template
from dictorius.app import app
from dictorius.models import Index, SEO, Footer, Config, Support
import json


def content_loader(lang: str) -> dict:
    file_path = f"dictorius/content/{lang}/content.json"
    with open(file_path, "r") as f:
        return json.load(f)


@app.route("/")
def index():
    content = content_loader("en")
    page = Index(content["index"])
    config = Config(content["config"])
    footer = Footer(content["footer"])
    seo = SEO(content["seo"])

    return render_template(
        "index.html", page=page, seo=seo, config=config, footer=footer
    )


@app.route("/support.html")
def support():
    content = content_loader("en")
    page = Support(content["support"])
    config = Config(content["config"])
    footer = Footer(content["footer"])
    seo = SEO(content["seo"])

    return render_template(
        "support.html", page=page, seo=seo, config=config, footer=footer
    )


@app.route("/privacy.html")
def privacy():
    return render_template("privacy.html")
