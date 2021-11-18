from mysql import connector

import config

_db: connector.connection.MySQLConnection = None


def init() -> connector.connection.MySQLConnection:
    global _db
    if _db:
        return _db
    _db = connector.connect(
        host=config.get("db.host"),
        user=config.get("db.user"),
        password=config.get("db.password"),
        port=config.get("db.port"),
        database=config.get("db.name")
    )
    return _db


def connect() -> connector.connection.MySQLConnection:
    init().connect()
    return _db
