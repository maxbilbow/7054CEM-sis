import dataclasses
from datetime import date
from typing import Optional

from core.model.membership import Membership
from core.model.membership_type import MembershipType, get_membership_type
from core.repository.membership import MembershipRepository
from core.repository.user_profile import UserProfileRepository
from web.exceptions import BadRequest


class MembershipService:
    __membership: MembershipRepository
    __profile: UserProfileRepository

    def __init__(self,
                 membership_repository=MembershipRepository(),
                 profile_repository=UserProfileRepository()):
        self.__membership = membership_repository
        self.__profile = profile_repository

    def get_for_user(self, user_id: int) -> Membership:
        return self.__membership.find_by_user_id(user_id)

    def new_membership(self,
                       user_id: int,
                       end_date: date) -> Membership:
        current_membership = self.get_for_user(user_id)
        if current_membership is not None:
            raise BadRequest("Cannot create new membership when current one is active")

        if end_date <= date.today():
            raise BadRequest("end_date must be in the future")

        membership = Membership(id=-1, user_id=user_id, start_date=date.today(), end_date=end_date,
                                type=self.get_eligible_membership_type(user_id))
        self.__membership.create(user_id, membership_type=membership.type,
                                 start_date=membership.start_date, end_date=membership.end_date)
        return self.get_for_user(user_id)

    def update_membership(self, user_id: int, end_date: Optional[date] = None,
                          membership_type: Optional[MembershipType] = None):
        membership = self.get_for_user(user_id)
        if end_date is not None:
            if end_date < date.today() or end_date < membership.start_date:
                raise BadRequest("New end_date is invalid")
            membership = dataclasses.replace(membership, end_date=end_date)

        if membership_type is not None:
            eligible_type = self.get_eligible_membership_type(user_id)
            if membership_type < eligible_type:
                raise BadRequest(f"User is not eligible for {membership_type.name} membership")
            membership = dataclasses.replace(membership, type=membership_type)

        return self.__membership.update_current(user_id, membership)

    def cancel_membership(self, user_id: int):
        membership = self.get_for_user(user_id)
        if membership is None:
            return None

        membership = dataclasses.replace(membership, end_date=date.today())
        if membership.start_date == membership.end_date:
            self.__membership.delete(membership)
            return None
        else:
            return self.__membership.update_current(user_id, membership)

    def get_eligible_membership_type(self, user_id: int) -> MembershipType:
        profile = self.__profile.find_by_user_id(user_id)
        return get_membership_type(role=profile.role, points=profile.points)
