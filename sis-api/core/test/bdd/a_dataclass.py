import dataclasses
from datetime import date, datetime
from enum import Enum
from typing import List

import swagger_server
from core.model.meta import *
from swagger_server.models.base_model_ import Model

DATE_TODAY = date.today()
DATE_STRING_TODAY = DATE_TODAY.isoformat()
DATETIME_NOW = datetime.today()
DATETIME_STRING_NOW = DATETIME_NOW.isoformat()


class AnEnum(Enum):
    Name = "Value"


@dataclasses.dataclass
class ADataclass:
    p1: str = dataclasses.field(default="p1")


class ASwaggerModel(swagger_server.models.User):
    def __init__(self):
        super().__init__(id=1, email="", password="")


@dataclasses.dataclass
class MyDataclass:
    pk: str = dataclasses.field(metadata={PK: True}, default="pk")
    pk_auto: int = dataclasses.field(metadata={PK: True, GENERATED: True}, default=42)
    not_a_column: str = dataclasses.field(metadata={SQL_COLUMN: False}, default="not_a_column")
    a_dataclass: ADataclass = dataclasses.field(default_factory=ADataclass)
    a_swagger_model: ASwaggerModel = dataclasses.field(default_factory=ASwaggerModel)
    a_date: date = dataclasses.field(default=DATE_TODAY)
    a_datetime: date = dataclasses.field(default=DATETIME_NOW)
    an_enum: AnEnum = dataclasses.field(default=AnEnum.Name)
    a_list: List[str] = dataclasses.field(default_factory=lambda: ["a_list", "of_things"])
    a_dataclass_list: List[ADataclass] = dataclasses.field(default_factory=lambda: [ADataclass()])
