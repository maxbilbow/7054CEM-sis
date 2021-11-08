from enum import IntEnum
from typing import Optional

from .membership import Membership
from .roles import Role

SILVER_POINTS_THRESHOLD = 2
GOLD_POINTS_THRESHOLD = 5


class MembershipStatus(IntEnum):
    Bronze = 0
    Silver = 1
    Gold = 2


class MembershipStatusFactory:

    @staticmethod
    def get_membership_status(role: Role, points: int, membership: Optional[Membership]) -> MembershipStatus:
        if role is Role.Advisor:
            return MembershipStatus.Gold
        if not membership:
            return MembershipStatus.Bronze
        if points >= GOLD_POINTS_THRESHOLD:
            return MembershipStatus.Gold
        elif points >= SILVER_POINTS_THRESHOLD:
            return MembershipStatus.Silver
        else:
            return MembershipStatus.Bronze
