import dataclasses
from dataclasses import dataclass, field
from datetime import date

from core.model import to_date
from core.model.membership_type import MembershipType


@dataclass(frozen=True, eq=True)
class Membership:
    id: int = field(metadata={"Key": True})
    user_id: int = field(metadata={"ForeignKey": True})
    start_date: date
    end_date: date
    type: MembershipType

    def __post_init__(self):
        if isinstance(self.start_date, str):
            raise TypeError("start_date initialized as string!")
        if isinstance(self.end_date, str):
            raise TypeError("end_date initialized as string!")

    @classmethod
    def from_dict(cls, args: dict):
        args["start_date"] = to_date(args["start_date"])
        args["end_date"] = to_date(args["end_date"])
        return cls(**args)


if __name__ == '__main__':
    m = Membership(1, 2, date.today(), date.today(), MembershipType.Smart)
    d = dataclasses.asdict(m)
    print(d)
