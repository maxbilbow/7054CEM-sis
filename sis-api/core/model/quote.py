from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from core.model.insurance_policy import InsuranceType


@dataclass(frozen=True, eq=True)
class Quote:
    id: int = field(metadata={"Key": True})
    user_id: int
    type: InsuranceType
    created: int = field(default=-1)
    updated: int = field(default=-1)
    is_complete: bool = field(default=False)
    price: Optional[float] = field(default=None)
