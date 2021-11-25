import logging
import typing
from dataclasses import dataclass, Field, asdict, fields, is_dataclass
from datetime import date
from enum import Enum
from typing import List, Optional

from core.model import to_dict
# Meta Data:
from core.model.meta import *
from swagger_server.models.base_model_ import Model


def is_optional(t: type) -> bool:
    return typing.get_origin(t) is typing.Union and type(None) in typing.get_args(t)


def is_list_type(t: type) -> bool:
    return t is list or typing.get_origin(t) is list


def get_type(f: Field) -> type:
    if isinstance(f.type, type):
        return f.type
    if is_optional(f.type):
        return typing.get_args(f.type)[0]
    if is_list_type(f.type):
        return f.type
    logging.warning(f"Not sure what type this is: {f.type}")
    return f.type


def _is_sql_column(f: Field) -> bool:
    t = get_type(f)
    if is_dataclass(t):
        return FK in f.metadata and f.metadata[FK]
    if is_list_type(t):
        return False
    if SQL_COLUMN in f.metadata and f.metadata[SQL_COLUMN] is False:
        return False
    if issubclass(t, Model):
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


def _is_pk(f: Field) -> bool:
    return PK in f.metadata and f.metadata[PK]


def _get_sql_name(f: Field) -> typing.Tuple[str, typing.Callable]:
    t = get_type(f)
    if not is_dataclass(t):
        return f.name, lambda v: v[f.name]

    if FK not in f.metadata:
        raise Exception("Dataclass is not specified as a foreign key. Cannot determine SLQ column name")

    if isinstance(f.metadata[FK], str):
        return f.metadata[FK], lambda v: "TODO"

    sub_field: Field = list(filter(_is_pk, list(fields(t))))[0]
    return f"{f.name}_{sub_field.name}", lambda v:  v[f.name][sub_field.name]


def _get_sql_entry(value: typing.Any, f: Field) -> typing.Tuple[str, typing.Any]:
    t = get_type(f)
    if not is_dataclass(t):
        return f.name, value

    if FK not in f.metadata:
        raise Exception("Dataclass is not specified as a foreign key. Cannot determine SLQ column name")

    if isinstance(f.metadata[FK], str):
        return f.metadata[FK]

    sub_field: Field = list(filter(_is_pk, list(fields(t))))[0]
    key = f"{f.name}_{sub_field.name}"

    if value is None:
        return key, None

    return key, getattr(value, sub_field.name)


def _to_sql_dict(model: dataclass, dataclass_fields: List[Field]) -> dict:
    keys = list(map(_get_sql_name, dataclass_fields))
    result = asdict(model, dict_factory=_get_sql_asdict_factory(dataclass_fields))
    return {key: get(result) for key, get in keys}


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
                return obj.to_dict()
            return obj

        res = dict()
        for k, v in data:
            # this_field = _get_field(dataclass_fields, k)
            # k, v = _get_sql_entry(v, this_field)
            res[k] = convert_value(v, None)

        return res
        # return dict((k, convert_value(v, _get_field(dataclass_fields, k))) for k, v in data)

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


class _SwaggerModelSerializer(_Serializer):
    _model: Model

    def __init__(self, model: Model):
        super().__init__(model)

    def for_sql_insert(self):
        logging.warning(f"SQL serialization may not work for {type(self._model)}")
        return self.for_api()

    def for_sql_update(self):
        logging.warning(f"SQL serialization may not work for {type(self._model)}")
        return self.for_api()

    def for_api(self):
        logging.warning(f"SQL serialization may not work for {type(self._model)}")
        from swagger_server import encoder
        o = encoder.JSONEncoder().default(self._model)
        return o


class _Dict(_Serializer):
    _model: Model

    def __init__(self, model: Model):
        super().__init__(model)

    def for_sql_insert(self):
        return self.for_api()

    def for_sql_update(self):
        return self.for_api()

    def for_api(self):
        return self._model


def serialize(o: dataclass) -> _Serializer:
    if isinstance(o, dict):
        logging.warning("Serialize used for dict")
        return _Dict(o)
    if isinstance(o, Model):
        logging.warning("Serialize used for swagger model")
        return _SwaggerModelSerializer(o)
    return _Serializer(o)
