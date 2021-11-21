from enum import Enum, IntEnum

from core.model.roles import Role

SILVER_POINTS_THRESHOLD = 2
GOLD_POINTS_THRESHOLD = 5


class MembershipType(IntEnum):
    Smart = 0
    Silver = 1
    Gold = 2

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value


def get_membership_type(points: int) -> MembershipType:
    if points >= GOLD_POINTS_THRESHOLD:
        return MembershipType.Gold
    elif points >= SILVER_POINTS_THRESHOLD:
        return MembershipType.Silver
    else:
        return MembershipType.Smart
