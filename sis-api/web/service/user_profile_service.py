import dataclasses

from injector import singleton, inject

from core.model.profile import Profile
from web.repository.profile_repository import ProfileRepository
from web.service.auth_service import AuthService
from web.service.membership_service import MembershipService


@singleton
class UserProfileService:
    __profile: ProfileRepository
    __membership: MembershipService

    @inject
    def __init__(self, profile_repository: ProfileRepository, membership_repository: MembershipService):
        self.__profile = profile_repository
        self.__membership = membership_repository

    def get_profile(self) -> Profile:
        user_id = AuthService.get_user_id()
        profile = self.__profile.get(user_id)
        if not profile:
            return Profile()

        membership = self.__membership.get()
        return dataclasses.replace(profile, membership=membership)

    def update_profile(self, profile: Profile) -> Profile:
        user_id = AuthService.get_user_id()
        if self.__profile.get(user_id) is None:
            self.__profile.insert(user_id, profile)
        else:
            self.__profile.update(user_id, profile)
        return self.get_profile()
