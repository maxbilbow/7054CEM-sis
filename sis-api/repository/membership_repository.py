from core.model.membership import Membership


class MembershipRepository:

    @staticmethod
    def get_membership(user_id: int) -> Membership:
        return Membership()
