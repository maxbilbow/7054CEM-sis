from flask import send_from_directory, current_app as app

import config
from rest.decorators import login_required


@app.route("/")
def index():
    return send_from_directory(config.get("web_app.public"), "index.html")


@app.route("/<path:filename>")
@login_required
def index_catch_all(filename: str):
    return send_from_directory(config.get("web_app.public"), filename)
