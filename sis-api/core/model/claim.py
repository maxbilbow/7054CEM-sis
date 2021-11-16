from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from core.model.claim_event import ClaimEvent
from core.model.claim_status import ClaimStatus


@dataclass
class Claim:
    id: int = field(metadata={"Key": True})
    package_id: int = field(metadata={"ForeignKey": True})
    claim_date: int
    summary: str
    resolution_date: Optional[int] = field(default=None)
    claim_status: ClaimStatus = field(default=ClaimStatus.Submitted)

    # Entities
    claim_history: List[ClaimEvent] = field(default_factory=list)

