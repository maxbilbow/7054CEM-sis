from dataclasses import dataclass
from datetime import date
from typing import Optional
from dateutil.relativedelta import relativedelta


@dataclass(frozen=True, eq=True)
class Membership:
    # user_id: int = field(metadata={"Key": True})
    # plan_id: int
    name: str
    start_date: Optional[date] = None
    term_months: int = 0

    @property
    def renewal_date(self) -> Optional[date]:
        if not self.start_date:
            return None

        return self.start_date + relativedelta(months=self.term_months)
