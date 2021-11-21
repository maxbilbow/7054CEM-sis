import atexit
from os.path import dirname

from mysql import connector

import config
from core.repository import mysql

config.load_config(r"%s/../config.yml" % dirname(__file__))


def _get_db():
    return connector.connect(
        host=config.get("db.host"),
        user=config.get("db.user"),
        password=config.get("db.password"),
        port=config.get("db.port")
    )


def _on_exit():
    con = _get_db()
    con.cursor().execute(f'DROP DATABASE {config.get("db.name")}')
    con.commit()


atexit.register(_on_exit)

with open(r"%s/../../../../sql/create_db.sql" % dirname(__file__)) as file:
    print("HELLO!")
    sql = file.read()
    # print(sql)
    try:
        con = _get_db()
        con.cursor().execute(f'CREATE DATABASE {config.get("db.name")}')
        con.cursor().execute(sql, multi=True)
        con.commit()
    except Exception as e:
        print(e)
