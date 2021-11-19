import dataclasses
from datetime import date
from typing import Optional

from injector import singleton, inject

from core.model.membership import Membership
from core.model.membership_type import MembershipType, get_membership_type
from web.exceptions import BadRequest
from web.repository.membership_repository import MembershipRepository
from web.repository.profile_repository import ProfileRepository
from web.service.auth_service import AuthService


@singleton
class MembershipService:
    __membership: MembershipRepository
    __profile: ProfileRepository

    @inject
    def __init__(self, membership_repository: MembershipRepository, profile_repository: ProfileRepository):
        self.__membership = membership_repository
        self.__profile = profile_repository

    def get(self) -> Membership:
        user_id = AuthService.get_user_id()
        return self.__membership.find_by_userid(user_id)

    def new_membership(self,
                       end_date: date) -> Membership:
        current_membership = self.get()
        if current_membership is not None:
            raise BadRequest("Cannot create new membership when current one is active")

        if end_date <= date.today():
            raise BadRequest("end_date must be in the future")

        user_id = AuthService.get_user_id()
        membership = Membership(id=-1, user_id=user_id, start_date=date.today(), end_date=end_date,
                                type=self.get_eligible_membership_type())
        self.__membership.create(user_id, membership)
        return self.get()

    def update_membership(self, end_date: Optional[date] = None, membership_type: Optional[MembershipType] = None):
        membership = self.get()
        if end_date is not None:
            if end_date < date.today() or end_date < membership.start_date:
                raise BadRequest("New end_date is invalid")
            membership = dataclasses.replace(membership, end_date=end_date)

        if membership_type is not None:
            eligible_type = self.get_eligible_membership_type()
            if membership_type < eligible_type:
                raise BadRequest(f"User is not eligible for {membership_type.name} membership")
            membership = dataclasses.replace(membership, type=membership_type)

        user_id = AuthService.get_user_id()
        return self.__membership.update(user_id, membership)

    def cancel_membership(self):
        user_id = AuthService.get_user_id()
        return self.__membership.cancel(user_id)

    def get_eligible_membership_type(self):
        user_id = AuthService.get_user_id()
        profile = self.__profile.get(user_id)
        return get_membership_type(role=profile.role, points=profile.points)
