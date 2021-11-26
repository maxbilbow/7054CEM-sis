import logging
import typing
from abc import abstractmethod, ABC
from dataclasses import asdict, is_dataclass
from datetime import date
from enum import Enum
from typing import List, Optional

import six

from core.model.meta import *
from swagger_server.models.base_model_ import Model as SwaggerModel


class Serializer:
    """
    Object serialization interface
    Returned bu serialize method
    """

    @abstractmethod
    def for_sql_insert(self) -> dict:
        """
        :return: A dictionary stripped of any properties
                 that cannot be inserted into an SQL table
                 Foreign keys are mapped according to dataclass annotations
                 if present
        """
        pass

    @abstractmethod
    def for_sql_update(self) -> dict:
        """
        :return: A dictionary stripped of any properties
                 that cannot be updated on an SQL table
                 Foreign keys are mapped according to dataclass annotations
                 if present
        """
        pass

    @abstractmethod
    def for_api(self, include_nulls: Optional[bool]) -> dict:
        """
        :param include_nulls: if False, null properties will not be included in the resulting dict
        :return: A dictionary ready to be converted to JSON and sent to the consuming client
        """
        pass


_T = typing.TypeVar("_T")


class _AbstractSerializer(Serializer, typing.Generic[_T], ABC):
    _model: _T

    def __init__(self, t: _T):
        self._model = t


class _DataclassSerializer(_AbstractSerializer[dataclass]):
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

    def for_api(self, include_nulls=True):
        return _to_json_api_dict(self._model, include_nulls)


class _SwaggerModelSerializer(_AbstractSerializer[SwaggerModel]):
    def for_sql_insert(self):
        logging.warning(f"SQL serialization may not work correctly for {type(self._model)}")
        return self.for_api()

    def for_sql_update(self):
        logging.warning(f"SQL serialization may not work correctly for {type(self._model)}")
        return self.for_api()

    def for_api(self, include_nulls=True):
        o = self._model
        dikt: dict = {}
        for attr, _ in six.iteritems(o.swagger_types):
            value = getattr(o, attr)
            if value is None and not include_nulls:
                continue
            attr = o.attribute_map[attr]
            dikt[attr] = value
        return dikt


class _Dict(_AbstractSerializer[dict]):
    def for_sql_insert(self):
        return self.for_api(True)

    def for_sql_update(self):
        return self.for_api(True)

    def for_api(self, include_nulls=True):
        return self._model


Serializable = typing.Union[dataclass, SwaggerModel, dict]


def serialize(o: Serializable) -> Serializer:
    if is_dataclass(o):
        logging.info("Serialization strategy: dataclass")
        return _DataclassSerializer(o)
    if isinstance(o, dict):
        logging.info("Serialization strategy: dict")
        return _Dict(o)
    if isinstance(o, SwaggerModel):
        logging.info("Serialization strategy: swagger-model")
        return _SwaggerModelSerializer(o)
    raise Exception(f"Unable to serialize object of type: {type(o)}")


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
    if issubclass(t, SwaggerModel):
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
    return f"{f.name}_{sub_field.name}", lambda v: v[f.name][sub_field.name]


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
    result = asdict(model, dict_factory=_get_asdict_factory(True))
    return {key: get(result) for key, get in keys}


def _to_json_api_dict(model: dataclass, include_nulls: bool) -> dict:
    return asdict(model, dict_factory=_get_asdict_factory(include_nulls))


def _get_asdict_factory(include_nulls: bool):
    def factory(data):
        def convert_value(obj):
            if obj is None:
                return obj
            if is_dataclass(obj):
                return serialize(obj).for_api(include_nulls)
            if isinstance(obj, Enum):
                return obj.name
            if isinstance(obj, date):
                return obj.isoformat()
            if isinstance(obj, SwaggerModel):
                return serialize(obj).for_api(include_nulls)
            return obj

        res = dict()
        for k, v in data:
            v = convert_value(v)
            if v is None and not include_nulls:
                continue
            res[k] = convert_value(v)

        return res

    return factory
