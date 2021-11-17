from dataclasses import dataclass, field
from datetime import date

from .membership_type import MembershipType


@dataclass(frozen=True, eq=True)
class Membership:
    id: int = field(metadata={"Key": True})
    user_id: int = field(metadata={"ForeignKey": True})
    start_date: date
    end_date: date
    type: MembershipType

