from flask import render_template

from web.flask_app import app
from web.rest.decorators import login_required


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<ignored>")
@login_required
def index_catch_all(ignored):
    return index()
