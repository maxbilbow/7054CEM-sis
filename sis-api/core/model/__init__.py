from dataclasses import dataclass, asdict
from enum import Enum


def to_dict(o: dataclass) -> dict:
    return asdict(o, dict_factory=custom_asdict_factory)


def custom_asdict_factory(data):
    def convert_value(obj):
        if isinstance(obj, Enum):
            return obj.name
        return obj

    return dict((k, convert_value(v)) for k, v in data)
