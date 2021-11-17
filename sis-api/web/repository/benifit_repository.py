from typing import List

from core.model.benefit import Benefit
from core.model.membership_type import MembershipType


class BenefitRepository:

    @staticmethod
    def get_benefits(membership_status: MembershipType) -> List[Benefit]:
        return list()
