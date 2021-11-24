from dataclasses import Field, dataclass, fields
from typing import Any, Tuple

PK = "sql_pk"
FK = "sql_foreign_key"
GENERATED = "sql_auto_increment"
NO_UPDATE = "sql_no_update"
SQL_COLUMN = "sql_is_column"
SQL_INSERT = "sql_insert"
SQL_UPDATE = "sql_update"
DESERIALIZER = "deserializer_function"


class DCMetaDataError(Exception):
    pass


def is_pk(f: Field) -> bool:
    return PK in f.metadata and f.metadata[PK]


def get_pk_name(dc_type: type(dataclass)) -> str:
    pk_list = list(filter(is_pk, fields(dc_type)))
    if len(pk_list) == 0:
        raise DCMetaDataError(f"object does not appear to have a primary key defined: {dc_type}")
    return pk_list[0].name


def get_pk(dc: dataclass) -> Tuple[str, Any]:
    pk = get_pk_name(dc)
    return pk, getattr(dc, pk)
