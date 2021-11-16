from dataclasses import field, dataclass
from typing import Optional, List

from core.model.Attachment import Attachment
from core.model.claim_status import ClaimStatus


@dataclass(frozen=True, eq=True)
class ClaimEvent:
    id: int = field(metadata={"Key": True})
    claim_id: int
    comment: str
    created: int
    claim_status: Optional[ClaimStatus] = field(default=None)
    attachments: List[Attachment] = field(default_factory=list)
