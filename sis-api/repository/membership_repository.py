from datetime import date

from core.model.membership import Membership
from core.model.membership_type import MembershipType


class MembershipRepository:

    def get_membership(self, user_id: int) -> Membership:
        pass

    @staticmethod
    def create_membership(user_id: int, start_date: date, end_date: date,
                          membership_type: MembershipType) -> Membership:
        return Membership(id=0,
                          user_id=user_id,
                          start_date=start_date,
                          end_date=end_date,
                          type=membership_type)
