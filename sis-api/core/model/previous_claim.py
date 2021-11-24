from dataclasses import dataclass, field
from datetime import date as Date
from typing import Optional

from core.model.meta import PK, GENERATED, FK


@dataclass(frozen=False, eq=True)
class PreviousClaim:
    id: Optional[int] = field(metadata={PK: True, GENERATED: True})
    driver_history_id: int = field(metadata={PK: True, FK: True})
    date: Optional[Date] = field(default=None)
    fault: Optional[str] = field(default=None)
    claim_type: Optional[str] = field(default=None)
