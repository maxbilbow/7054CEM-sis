import dataclasses
import re
import sys
import typing
from copy import copy
from dataclasses import dataclass, fields, is_dataclass, Field
# Meta Data:
from datetime import date, datetime
from enum import Enum
from typing import Any, Optional, Callable

from core.utils.serialization import is_list_type
from swagger_server.models.base_model_ import Model

Parser = Callable[[Any], Any]


def deserialize(data: dict, to_class: type(dataclass)):
    data = copy(data)
    dc_fields = fields(to_class)
    for f in dc_fields:
        if f.name in data and data[f.name] is not None:
            data[f.name] = _parse_with_field(data[f.name], f)
        else:
            data[f.name] = _get_default(f)

    dc = to_class(**data)
    return dc


def _is_optional(t: type) -> bool:
    return typing.get_origin(t) is typing.Union and type(None) in typing.get_args(t)


def _get_default(f: Field):
    if _is_optional(f.type):
        return None
    if f.default is not dataclasses.MISSING:
        return f.default
    if f.default_factory is not dataclasses.MISSING:
        return f.default_factory()
    return None


def _get_parser_for_type(cls: type) -> Optional[Parser]:
    if is_dataclass(cls):
        return lambda value: deserialize(value, cls)
    else:
        return cls


def _parse_with_field(value: Any, f: Field):
    if is_list_type(f.type):
        list_item_type = typing.get_args(f.type)[0]
        parse_item = _get_parser_for_type(list_item_type)
        return [parse_item(item) for item in value] if value is not None else list()
    if not isinstance(f.type, type):
        raise TypeError(f"Unable to determine type for {f}")
    if f.type is datetime:
        return datetime.fromisoformat(value)
    if f.type is date:
        return datetime.fromisoformat(value) if "T" in value else date.fromisoformat(value)
    if issubclass(f.type, Enum):
        return f.type[value]
    if is_dataclass(f.type):
        return deserialize(value, f.type)
    if issubclass(f.type, Model):
        return f.type.from_dict(value)

    return value
