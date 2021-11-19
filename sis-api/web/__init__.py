import sys
from os.path import dirname, abspath, join

from flask_injector import FlaskInjector

path = abspath(join(dirname(__file__)))
sys.path.append(path)


def configure(binder):
    # binder.bind(MyService, to=MyService, scope=singleton)
    # binder.bind(Database, to=MongoDatabase, scope=singleton)
    print("Hello!")


def init(app):
    import web.rest
    # Setup Flask Injector, this has to happen AFTER routes are added
    FlaskInjector(app=app, modules=[configure])
