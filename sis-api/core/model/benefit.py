from dataclasses import dataclass, field
from typing import Optional

from .membership_type import MembershipType


@dataclass(frozen=True, eq=True)
class Benefit:
    name: str = field(metadata={"Key": True})
    min_status: MembershipType
    max_status: Optional[MembershipType] = None

