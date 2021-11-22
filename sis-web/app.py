#!/usr/bin/env python3
# Import the Flask class. An instance of this class will be our WSGI application.
from os.path import dirname

from flask import Flask
from flask_injector import FlaskInjector

import config
import rest


def configure(binder):
    # binder.bind(MyService, to=MyService, scope=singleton)
    # binder.bind(Database, to=MongoDatabase, scope=singleton)
    print("Hello!")


def init(app):
    rest.init()
    # Setup Flask Injector, this has to happen AFTER routes are added
    FlaskInjector(app=app, modules=[configure])


def run():
    config.load_config(r"%s/config.yml" % dirname(__file__))
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

    with app.app_context():
        init(app)

    app.run(port=8888)

    # if (os.environ.get('FLASK_ENV') == 'development'):
    #     logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


if __name__ == '__main__':
    run()
