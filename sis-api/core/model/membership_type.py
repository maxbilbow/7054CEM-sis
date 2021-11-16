from enum import IntEnum

from core.model.roles import Role

SILVER_POINTS_THRESHOLD = 2
GOLD_POINTS_THRESHOLD = 5


class MembershipType(IntEnum):
    Smart = 0
    Silver = 1
    Gold = 2


class MembershipTypeFactory:

    @staticmethod
    def get_membership_type(role: Role, points: int) -> MembershipType:
        if role is Role.Advisor:
            return MembershipType.Gold
        if points >= GOLD_POINTS_THRESHOLD:
            return MembershipType.Gold
        elif points >= SILVER_POINTS_THRESHOLD:
            return MembershipType.Silver
        else:
            return MembershipType.Smart
