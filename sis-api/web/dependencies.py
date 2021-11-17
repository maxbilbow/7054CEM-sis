from injector import singleton

# Import rest endpoints
import web.rest.index


def configure(binder):
    # binder.bind(MyService, to=MyService, scope=singleton)
    # binder.bind(Database, to=MongoDatabase, scope=singleton)
    print("Hello!")
