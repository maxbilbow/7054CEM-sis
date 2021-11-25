import dataclasses
import logging
import typing
from copy import copy
from dataclasses import dataclass, fields, is_dataclass, Field
# Meta Data:
from datetime import date, datetime
from enum import Enum
from typing import Any, Optional, Callable

from core.model.meta import DESERIALIZER
from core.utils.serialization import is_list_type, is_optional, get_type
from swagger_server.models.base_model_ import Model

Parser = Callable[[Any], Any]


def deserialize(data: dict, to_class: type(dataclass)):
    data = copy(data)
    parsed_data = dict()
    dc_fields = fields(to_class)
    for f in dc_fields:
        if f.name in data and data[f.name] is not None:
            parsed_data[f.name] = _parse_with_field(data[f.name], f)
        else:
            parsed_data[f.name] = _get_default(f)

    dc = to_class(**parsed_data)
    return dc


def _get_default(f: Field):
    if is_optional(f.type):
        return None
    if f.default is not dataclasses.MISSING:
        return f.default
    if f.default_factory is not dataclasses.MISSING:
        return f.default_factory()

    logging.warning(f"Unable to determine default value for required field: {f}")
    return None


def _get_parser_for_type(cls: type) -> Optional[Parser]:
    if is_dataclass(cls):
        return lambda value: deserialize(value, cls)
    else:
        return cls


def _parse_with_field(value: Any, f: Field):
    if DESERIALIZER in f.metadata:
        return f.metadata[DESERIALIZER](value)
    if is_list_type(f.type):
        list_item_type = typing.get_args(f.type)[0]
        parse_item = _get_parser_for_type(list_item_type)
        return [parse_item(item) for item in value] if value is not None else list()
    t = get_type(f)

    if not isinstance(t, type):
        raise TypeError(f"Unable to determine type for {f}")
    if is_dataclass(t):
        return deserialize(value, t)
    if issubclass(t, Model):
        logging.warning(f"Need to stop using swagger models: {t}")
        return t.from_dict(value)
    if isinstance(value, int):
        return value == 1 if t is bool else value
    if not isinstance(value, str):
        logging.info(f"Already deserialized: {value}")
        return value
    if t == datetime:
        return datetime.fromisoformat(value)
    if t == date:
        return datetime.fromisoformat(value) if "T" in value else date.fromisoformat(value)
    if issubclass(t, Enum):
        return t[value]

    return value
