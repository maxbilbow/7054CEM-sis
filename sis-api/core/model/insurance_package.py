from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import List

from core.model.claim import Claim


class InsuranceType(Enum):
    Home = "Home"
    Motor = "Motor"


@dataclass(frozen=True, eq=True)
class InsurancePackage:
    user_id: int = field(metadata={"Key": True})
    type: InsuranceType
    start_date: date
    end_date: date
    claims: List[Claim]


