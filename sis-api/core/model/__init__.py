from dataclasses import dataclass, asdict
from datetime import date
from enum import Enum
from typing import Optional, Union


def to_dict(o: dataclass, use_enum_values=False) -> dict:
    return asdict(o, dict_factory=_dict_with_enum_names)


def _dict_with_enum_names(data):
    def convert_value(obj):
        if isinstance(obj, Enum):
            return obj.name
        if isinstance(obj, date):
            return f"{obj.year}-{obj.month}-{obj.day}"
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
        y, m, d = value.split("-")
        return date(int(y), int(m), int(d.split('T')[0]))
    else:
        raise TypeError(f"Unable to parse date string: {value}")

