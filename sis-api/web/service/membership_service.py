from datetime import date
from typing import Optional

from dateutil.relativedelta import relativedelta

from core.model.membership import Membership
from core.model.membership_type import MembershipTypeFactory
from core.model.profile import Profile
from web.repository.membership_repository import MembershipRepository


class MembershipService:
    __repository: MembershipRepository

    def __init__(self, repository: MembershipRepository):
        self.__repository = repository

    def new_membership(self, profile: Profile, start_date: date, term_months: int) -> Membership:
        membership_type = MembershipTypeFactory.get_membership_type(profile.role, profile.points)
        end_date = MembershipService.__renewal_date(start_date, term_months)
        return self.__repository.create_membership(
            user_id=profile.user_id, start_date=start_date, end_date=end_date,
            membership_type=membership_type
        )

    @staticmethod
    def __renewal_date(start_date: date, term_months: int) -> Optional[date]:
        if not start_date:
            return None

        return start_date + relativedelta(months=term_months)
