from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class InsuranceType(Enum):
    Home = "Home"
    Motor = "Motor"


@dataclass(frozen=True, eq=True)
class InsurancePolicy:
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
