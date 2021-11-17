from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List, Optional

from core.model.claim_note import ClaimNote
from core.model.claim_status import ClaimStatus


@dataclass
class Claim:
    id: int = field(metadata={"Key": True})
    package_id: int = field(metadata={"ForeignKey": True})
    summary: str
    incident_date: date
    timestamp: int
    resolution_date: Optional[int] = field(default=None)
    claim_status: ClaimStatus = field(default=ClaimStatus.Submitted)

    # Entities
    claim_history: List[ClaimNote] = field(default_factory=list)

