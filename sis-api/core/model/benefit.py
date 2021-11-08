from dataclasses import dataclass, field
from typing import Optional

from membership_status import MembershipStatus


@dataclass(frozen=True, eq=True)
class Benefit:
    name: str = field(metadata={"Key": True})
    min_status: MembershipStatus
    max_status: Optional[MembershipStatus] = None

