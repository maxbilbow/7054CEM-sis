from copy import copy
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional

from core.model.base_model import BaseModel
from core.model.meta import PK, GENERATED


class InsuranceType(Enum):
    Home = "Home"
    Motor = "Motor"


@dataclass(frozen=True, eq=True)
class InsurancePolicy(BaseModel):
    id: Optional[int] = field(metadata={PK: True, GENERATED: True})
    package_id: int
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
