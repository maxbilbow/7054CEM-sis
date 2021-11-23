import dataclasses
from dataclasses import dataclass, Field, asdict, fields, is_dataclass
from datetime import date
from enum import Enum
from typing import List, Optional

from core.model import to_dict

# Meta Data:
from core.model.base_model import BaseModel
from core.model.meta import *
from swagger_server.models.base_model_ import Model


def _is_sql_column(f: Field) -> bool:
    if is_dataclass(f.type):
        return False
    if f.type is list:
        return False
    if SQL_COLUMN in f.metadata and f.metadata[SQL_COLUMN] is False:
        return False
    return True


def _should_insert(f: Field) -> bool:
    if GENERATED in f.metadata and f.metadata[GENERATED] is True:
        return False
    if SQL_INSERT in f.metadata and f.metadata[SQL_INSERT] is False:
        return False
    return True


def _should_update(f: Field) -> bool:
    if SQL_UPDATE in f.metadata and f.metadata[SQL_UPDATE] is False:
        return False
    return True


def _get_field(dataclass_fields: List[Field], key: str) -> Optional[Field]:
    field_list = list(filter(lambda f: f.name == key, dataclass_fields))
    return field_list[0] if len(field_list) == 1 else None


def _get_sql_fields(model: dataclass) -> List[Field]:
    dataclass_fields = fields(model)
    dataclass_fields = list(filter(_is_sql_column, dataclass_fields))
    return dataclass_fields


def _to_sql_dict(model: dataclass, dataclass_fields: List[Field]) -> dict:
    keys = list(map(lambda f: f.name, dataclass_fields))
    result = asdict(model, dict_factory=_get_sql_asdict_factory(dataclass_fields))
    return {key: result[key] for key in keys}


def _to_json_api_dict(model: dataclass) -> dict:
    return asdict(model, dict_factory=_get_sql_asdict_factory(list()))


def _get_sql_asdict_factory(dataclass_fields: List[Field]):
    def factory(data):
        def convert_value(obj, f: Optional[Field]):
            if obj is None:
                return obj
            if is_dataclass(obj):
                return serialize(obj).for_api()
            if isinstance(obj, Enum):
                return obj.name
            if isinstance(obj, date):
                return obj.isoformat()  # f"{obj.year}-{obj.month}-{obj.day}"
            if isinstance(obj, Model):
                return to_dict(obj)
            return obj

        return dict((k, convert_value(v, _get_field(dataclass_fields, k))) for k, v in data)

    return factory


class _Serializer:
    _model: dataclass

    def __init__(self, model: dataclass):
        self._model = model

    def for_sql_insert(self):
        sql_fields = _get_sql_fields(self._model)
        sql_fields = list(filter(_should_insert, sql_fields))
        sql_dict = _to_sql_dict(self._model, sql_fields)
        return sql_dict

    def for_sql_update(self):
        sql_fields = _get_sql_fields(self._model)
        sql_fields = list(filter(_should_update, sql_fields))
        sql_dict = _to_sql_dict(self._model, sql_fields)
        return sql_dict

    def for_api(self):
        return _to_json_api_dict(self._model)


def serialize(o: dataclass) -> _Serializer:
    return _Serializer(o)
