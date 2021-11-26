from flask import send_from_directory, current_app as app

import config
from rest.decorators import login_required


@app.route("/")
@app.route("/<path:filename>")
@login_required
def index_catch_all(filename: str = "index.html"):
    return send_from_directory(config.get("web_app.public"), filename)
