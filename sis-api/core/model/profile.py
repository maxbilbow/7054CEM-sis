from dataclasses import dataclass, field
from typing import Optional, List

from .roles import Role
from .membership import Membership
from .membership_status import MembershipStatus, GOLD_POINTS_THRESHOLD, SILVER_POINTS_THRESHOLD
from .benefit import Benefit


@dataclass(frozen=True, eq=True)
class Profile:
    # user_id: int = field(metadata={"Key": True})
    # membership_id: Optional[int]
    points: int
    membership: Optional[Membership]
    membership_status: MembershipStatus
    benefits: List[Benefit]
    role: Role


