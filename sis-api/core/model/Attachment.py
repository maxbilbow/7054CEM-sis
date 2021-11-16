from dataclasses import field, dataclass
from typing import Optional


@dataclass(frozen=True, eq=True)
class Attachment:
    claim_event_id: int
    name: Optional[str] = field(default=None)
    mime_type: Optional[str] = field(default=None)
    data: Optional[bytes] = field(default=None)
