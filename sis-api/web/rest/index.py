import flask
from flask import render_template, send_from_directory

from web.flask_app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/css/<path:path>')
def send_css(path):
    return flask.send_from_directory('../static/css', path)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
