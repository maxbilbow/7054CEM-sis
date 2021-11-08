from typing import List

from core.model.benefit import Benefit
from core.model.membership_status import MembershipStatus


class BenefitRepository:

    @staticmethod
    def get_benefits(membership_status: MembershipStatus) -> List[Benefit]:
        return list()
