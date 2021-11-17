from enum import Enum

from core.model.roles import Role

SILVER_POINTS_THRESHOLD = 2
GOLD_POINTS_THRESHOLD = 5


class MembershipType(Enum):
    Smart = "Smart"
    Silver = "Silver"
    Gold = "Gold"


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
