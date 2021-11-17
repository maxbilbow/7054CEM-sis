from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class InsuranceType(Enum):
    Home = "Home"
    Motor = "Motor"


@dataclass(frozen=True, eq=True)
class InsurancePackage:
    user_id: int = field(metadata={"Key": True})
    type: InsuranceType
    start_date: date
    end_date: date


