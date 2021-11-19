from dataclasses import dataclass, field
from datetime import date

from . import to_date
from .membership_type import MembershipType


@dataclass(frozen=True, eq=True)
class Membership:
    id: int = field(metadata={"Key": True})
    user_id: int = field(metadata={"ForeignKey": True})
    start_date: date
    end_date: date
    type: MembershipType

    @classmethod
    def from_dict(cls, args: dict):
        args["start_date"] = to_date(args["start_date"])
        args["end_date"] = to_date(args["end_date"])
        return cls(**args)
