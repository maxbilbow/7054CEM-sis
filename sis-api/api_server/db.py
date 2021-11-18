from mysql import connector

import config

db: connector.connection.MySQLConnection = None


def init() -> connector.connection.MySQLConnection:
    global db
    if db:
        return db
    db = connector.connect(
        host=config.get("db.host"),
        user=config.get("db.user"),
        password=config.get("db.password"),
        port=config.get("db.port"),
        database=config.get("db.name")
    )
    return db


def connect() -> connector.connection.MySQLConnection:
    init().connect()
    return db
