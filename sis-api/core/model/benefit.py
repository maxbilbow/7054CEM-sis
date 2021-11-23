from dataclasses import dataclass, field
from typing import Optional

from .meta import PK
from .membership_type import MembershipType


@dataclass(frozen=True, eq=True)
class Benefit:
    name: str = field(metadata={PK: True})
    min_membership: MembershipType
    max_membership: Optional[MembershipType] = None

