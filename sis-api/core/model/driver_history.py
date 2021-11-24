from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List

from core.model.base_model import BaseModel
from core.model.meta import PK, GENERATED
from core.model.previous_claim import PreviousClaim


@dataclass(frozen=False, eq=True)
class DriverHistory(BaseModel):
    id: Optional[int] = field(metadata={PK: True, GENERATED: True}, default=None)
    licence_type: Optional[str] = field(default=None)
    license_since: Optional[date] = field(default=None)
    licence_no: Optional[str] = field(default=None)
    previous_claims: List[PreviousClaim] = field(default_factory=list)
