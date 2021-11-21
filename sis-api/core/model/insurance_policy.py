from copy import copy
from dataclasses import dataclass, field
from datetime import date
from enum import Enum

from core.model.base_model import BaseModel


class InsuranceType(Enum):
    Home = "Home"
    Motor = "Motor"


@dataclass(frozen=True, eq=True)
class InsurancePolicy(BaseModel):
    id: int = field(metadata={"Key": True})
    user_id: int
    type: InsuranceType
    start_date: date
    end_date: date

    @property
    def status(self):
        if self.start_date > date.today():
            return "Pending"
        if self.end_date < date.today():
            return "Expired"
        return "Active"

    def __post_init__(self):
        if isinstance(self.type, str):
            raise TypeError("membership type is not an enum")

    def from_dict(cls, data: dict):
        data = copy(data)
        data["type"] = InsuranceType[data["type"]]
        return cls(**data)
