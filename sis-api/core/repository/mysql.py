import dataclasses
from typing import Any, Optional, List, Union, Tuple

from mysql import connector
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from core import config
from core.model import to_dict

# _db: connector.connection.MySQLConnection = None
from swagger_server.models.base_model_ import Model


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


Entity = Union[dict, Model, dataclasses.dataclass]
Matcher = Tuple[str, Any]
Matchers = Union[List[Matcher], Matcher]


def _get_matchers(matchers: Matchers) -> Tuple[List[Matcher], str]:
    if not isinstance(matchers[0], list):
        matchers = [matchers]
    return matchers, " AND ".join([f"{key}={value}" for key, value in matchers])


class _Table:
    _table_name: str
    _cur: MySQLCursor

    def __init__(self, cur, table_name: str):
        self._cur = cur
        self._table_name = table_name

    def find_by(self, matchers: Matchers) -> MySQLCursor:
        matchers, where_clause = _get_matchers(matchers)
        self._cur.execute(f"SELECT * FROM `{self._table_name}` WHERE {where_clause}")
        return self._cur

    def insert(self, o: Entity, keys: Optional[List[str]] = None) -> int:
        o = to_dict(o)
        if keys is None:
            keys = list(o.keys())
        elif isinstance(keys, dict):
            keys = list(keys.keys())

        values = [o[key] if key in o else None for key in keys]
        placeholder = ", ".join(["%s"] * len(keys))
        table_name = self._table_name
        qry = "INSERT INTO {table_name} ({columns}) VALUES ({values})" \
            .format(table_name=table_name, columns=",".join(keys), values=placeholder)
        print(qry)
        self._cur.execute(qry, values)
        return self._cur.lastrowid

    def update(self, o: Entity, keys: Optional[List[str]] = None,
               matchers: Optional[Matchers] = None):
        def update_value(name: str) -> str:
            return '{name}=%s'.format(name=name)

        o = to_dict(o)
        if keys is None:
            keys = list(o.keys())
        if isinstance(keys, dict):
            keys = list(keys.keys())

        if matchers is None:
            matchers = list([list(o.keys())[0], list(o.values())[0]])

        matchers, where_clause = _get_matchers(matchers)

        table_name = self._table_name
        values = [o[key] for key in keys]

        update_values = map(update_value, keys)
        qry = "UPDATE {table_name} SET {update_values} WHERE {where_clause}" \
            .format(table_name=table_name, update_values=",".join(update_values), where_clause=where_clause)
        print(qry)
        return self._cur.execute(qry, values)

    def delete(self, matchers: Union[Matchers, int]):
        if isinstance(matchers, int):
            where_clause = f"id={matchers}"
        elif isinstance(matchers[0], list):
            where_clause = " AND ".join([f"{key}='{value}'" for [key, value] in matchers])
        else:
            key, value = matchers
            where_clause = f"{key}={value}"

        sql = f"DELETE FROM `{self._table_name}` WHERE {where_clause}"
        print(sql)
        return self._cur.execute(sql)


class _Session:
    connection: MySQLConnection
    cursor: MySQLCursor

    def __enter__(self):
        self.connection = connect()
        self.cursor = self.connection.cursor(dictionary=True, buffered=True)
        return self

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def on_table(self, table_name):
        return _Table(self.cursor, table_name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def session():
    return _Session()


def table(table_name):
    return session().on_table(table_name)


def insert(table_name: str,
           entity: dataclasses.dataclass,
           exclude_keys: Optional[List[str]] = None):
    if exclude_keys is None:
        exclude_keys = list()

    con = connect()
    cur = con.cursor(dictionary=True)

    try:
        o = to_dict(entity)
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
        data = to_dict(entity)
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
