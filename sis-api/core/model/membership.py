import dataclasses
from copy import copy
from dataclasses import dataclass, field
from datetime import date
from typing import Optional

from core.model import to_date
from core.model.base_model import BaseModel
from core.model.meta import PK, GENERATED, FK
from core.model.membership_type import MembershipType


@dataclass(frozen=True, eq=True)
class Membership(BaseModel):
    id: Optional[int] = field(metadata={PK: True, GENERATED: True})
    user_id: int = field(metadata={FK: True})
    start_date: date
    end_date: date
    type: MembershipType

    def __post_init__(self):
        if isinstance(self.start_date, str):
            raise TypeError("start_date initialized as string!")
        if isinstance(self.end_date, str):
            raise TypeError("end_date initialized as string!")
        if isinstance(self.type, str):
            raise TypeError("membership type is not an enum")

    @classmethod
    def from_dict(cls, args: dict):
        args = copy(args)
        args["start_date"] = to_date(args["start_date"])
        args["end_date"] = to_date(args["end_date"])
        args["type"] = MembershipType[args["type"]]
        return cls(**args)


if __name__ == '__main__':
    m = Membership(1, 2, date.today(), date.today(), MembershipType.Smart)
    d = dataclasses.asdict(m)
    print(d)
