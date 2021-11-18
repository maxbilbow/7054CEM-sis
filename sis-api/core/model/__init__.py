from dataclasses import dataclass, asdict
from enum import Enum


def to_dict(o: dataclass, use_enum_values=False) -> dict:
    return asdict(o, dict_factory=_dict_with_enum_names)


def _dict_with_enum_names(data):
    def convert_value(obj):
        if isinstance(obj, Enum):
            return obj.name
        return obj

    return dict((k, convert_value(v)) for k, v in data)
