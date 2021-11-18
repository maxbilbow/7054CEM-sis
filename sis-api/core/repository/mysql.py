import dataclasses
from typing import Any, Optional, List

from swagger_server import db
from core.model import custom_asdict_factory


def insert(table_name: str,
           entity: dataclasses.dataclass,
           exclude_keys: Optional[List[str]] = None):
    if exclude_keys is None:
        exclude_keys = list()

    con = db.connect()
    cur = con.cursor()

    try:
        o = dataclasses.asdict(entity, dict_factory=custom_asdict_factory)
        for ex in exclude_keys:
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

    con = db.connect()
    cur = con.cursor()

    def update_value(name: str) -> str:
        return '{name}=%s'.format(name=name)

    try:
        data = dataclasses.asdict(entity, dict_factory=custom_asdict_factory)
        del data[pk_name]
        for ex in exclude_keys:
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
    con = db.connect()
    cur = con.cursor()
    try:
        cur.execute(f"SELECT * FROM `{table_name}` WHERE {key} = '{key_value}'")
        entry = cur.fetchone()
        con.commit()
        return entry
    finally:
        cur.close()
        con.close()


def delete_by(table_name: str, key_value: Any, key: str = "id"):
    con = db.connect()
    cur = con.cursor()
    try:
        cur.execute(f"DELETE FROM `{table_name}` WHERE {key} = '{key_value}'")
        con.commit()
    finally:
        cur.close()
        con.close()
