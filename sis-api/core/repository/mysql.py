import dataclasses
from typing import Any, Optional, List

from mysql import connector

from core import config
from core.model import to_dict


# _db: connector.connection.MySQLConnection = None


def _init() -> connector.connection.MySQLConnection:
    # global _db
    # if _db:
    #     return _db
    return connector.connect(
        host=config.get("db.host"),
        user=config.get("db.user"),
        password=config.get("db.password"),
        port=config.get("db.port"),
        database=config.get("db.name")
    )


def connect() -> connector.connection.MySQLConnection:
    con = _init()
    con.connect()
    return con


def insert(table_name: str,
           entity: dataclasses.dataclass,
           exclude_keys: Optional[List[str]] = None):
    if exclude_keys is None:
        exclude_keys = list()

    con = connect()
    cur = con.cursor(dictionary=True)

    try:
        o = to_dict(entity, use_enum_values=True)
        for ex in exclude_keys:
            if ex in o:
                del o[ex]

        placeholder = ", ".join(["%s"] * len(o))
        qry = "INSERT INTO {table_name} ({columns}) VALUES ({values})" \
            .format(table_name=table_name, columns=",".join(o.keys()), values=placeholder)
        print(qry)
        cur.execute(qry, list(o.values()))
        con.commit()
        return cur.lastrowid
    finally:
        cur.close()
        con.close()


def update_by_pk(table_name: str,
                 entity: dataclasses.dataclass,
                 pk: Any,
                 pk_name: str = "id",
                 exclude_keys: Optional[List[str]] = None):
    if exclude_keys is None:
        exclude_keys = list()

    con = connect()
    cur = con.cursor()

    def update_value(name: str) -> str:
        return '{name}=%s'.format(name=name)

    try:
        data = to_dict(entity, use_enum_values=True)
        del data[pk_name]
        for ex in exclude_keys:
            if ex in data:
                del data[ex]

        update_values = map(update_value, data.keys())
        qry = "UPDATE {table_name} SET {update_values} WHERE {pk_name}={pk_value}" \
            .format(table_name=table_name, update_values=",".join(update_values), pk_name=pk_name, pk_value=pk)
        print(qry)
        values = list(data.values())
        cur.execute(qry, values)
        con.commit()
        return
    finally:
        cur.close()
        con.close()


def find_by(table_name: str, key_value: Any, key: str = "id"):
    con = connect()
    cur = con.cursor(dictionary=True)

    try:
        cur.execute(f"SELECT * FROM `{table_name}` WHERE {key} = '{key_value}'")
        entry = cur.fetchone()
        con.commit()
        return entry
    finally:
        cur.close()
        con.close()


def find_all_by(table_name: str, key_value: Any, key: str = "id"):
    con = connect()
    cur = con.cursor(dictionary=True)
    try:
        cur.execute(f"SELECT * FROM `{table_name}` WHERE {key} = '{key_value}'")
        rows = cur.fetchall()
        con.commit()
        return rows
    finally:
        cur.close()
        con.close()


def delete_by(table_name: str, key_value: Any, key: str = "id"):
    con = connect()
    cur = con.cursor()
    try:
        cur.execute(f"DELETE FROM `{table_name}` WHERE {key} = '{key_value}'")
        con.commit()
    finally:
        cur.close()
        con.close()
