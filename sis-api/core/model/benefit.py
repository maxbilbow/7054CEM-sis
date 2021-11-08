from dataclasses import dataclass, field
from membership_status import MembershipStatus


@dataclass
class Benefit:
    id: str = field(metadata={"Key": True})
    name: str
    description: str
    min_status: MembershipStatus
