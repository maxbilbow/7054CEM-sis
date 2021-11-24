from dataclasses import is_dataclass, dataclass
from datetime import date
from enum import Enum
from typing import Optional, Union, List
from deprecated import deprecated
from swagger_server.models.base_model_ import Model


def get_keys(o: Union[dict, dataclass, Model], exclude: Optional[List[str]] = None) -> List[str]:
    keys: List[str]
    if isinstance(o, Model):
        keys = [o.attribute_map[key] for key in list(o.swagger_types.keys())]
    else:
        keys = list(to_dict(o).keys())

    if exclude is not None:
        keys = list(filter(lambda x: x not in exclude, keys))
    return keys


@deprecated
def to_dict(o) -> Optional[Union[list, dict]]:
    if o is None:
        return None
    if is_dataclass(o):
        return to_dict(o)
    if isinstance(o, list):
        return [to_dict(each) for each in o]
    if isinstance(o, Model):
        return o.to_dict()
    raise TypeError("{} is not a dict".format(type(o)))


def _serializable_dict(data):
    def convert_value(obj):
        if obj is None:
            return obj
        if isinstance(obj, Enum):
            return obj.name
        if isinstance(obj, date):
            return obj.isoformat()  # f"{obj.year}-{obj.month}-{obj.day}"
        if isinstance(obj, Model):
            return to_dict(obj)
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
