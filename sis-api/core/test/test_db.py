import atexit
import logging
from os.path import dirname

from mysql import connector

from core import config
from core.repository import mysql


def load_config():
    config.load_config(r"%s/config.yml" % dirname(__file__))


def _get_db():
    return connector.connect(
        host=config.get("db.host"),
        user=config.get("db.user"),
        password=config.get("db.password"),
        port=config.get("db.port")
    )


def tear_down():
    atexit.unregister(tear_down)
    con = _get_db()
    try:
        res = con.cmd_query(f'DROP DATABASE IF EXISTS {config.get("db.name")}')
        logging.debug(f'Dropped database "{config.get("db.name")}"', res)
    finally:
        con.close()


def set_up():
    load_config()
    atexit.register(tear_down)
    tear_down()
    with open(r"%s/test_db.sql" % dirname(__file__)) as file:
        con = _get_db()
        try:
            con.cmd_query(
                f'CREATE DATABASE IF NOT EXISTS `{config.get("db.name")}` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;')
            con.close()
            con = mysql.connect()
            for sql in file.read().replace("\n", "").split(';'):
                if sql.strip(" ") == "":
                    continue
                res = con.cmd_query(sql)
                logging.debug(sql, res)

            logging.info(f'Created database "{config.get("db.name")}"')
        except Exception as e:
            logging.error("DB Setup Failed")
            logging.error(e)
            raise e
        finally:
            con.close()


if __name__ == '__main__':
    set_up()
