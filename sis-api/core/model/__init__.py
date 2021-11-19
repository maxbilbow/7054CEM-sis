from dataclasses import dataclass, asdict
from datetime import date
from enum import Enum
from typing import Optional, Union


def to_dict(o: dataclass, use_enum_values=False) -> dict:
    return asdict(o, dict_factory=_serializable_dict)


def _serializable_dict(data):
    def convert_value(obj):
        if obj is None:
            return obj
        if isinstance(obj, Enum):
            return obj.name
        if isinstance(obj, date):
            return obj.isoformat() #f"{obj.year}-{obj.month}-{obj.day}"
        return obj

    return dict((k, convert_value(v)) for k, v in data)


def to_date(value: Optional[Union[str, date]]) -> Optional[date]:
    if not value:
        return None
    if isinstance(value, date):
        return value
    if not isinstance(value, str):
        raise TypeError(f"Expected string or date but found {type(value)}")

    ymd = value.split("-")
    if len(ymd) == 3:
        return date.fromisoformat(value)
    else:
        return date.fromisoformat(value)

