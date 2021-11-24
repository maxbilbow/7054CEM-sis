from injector import singleton, inject

from core.model.profile import Profile
from core.repository.user_profile import UserProfileRepository
from core.utils.deserialization import deserialize


@singleton
class ProfileService:
    __profile: UserProfileRepository

    @inject
    def __init__(self, profile_repository=UserProfileRepository()):
        self.__profile = profile_repository

    def get_profile(self, user_id) -> Profile:
        profile = self.__profile.find_by_user_id(user_id)
        return Profile(user_id) if not profile else profile

    def insert_profile(self, data: dict) -> Profile:
        profile = deserialize(data, Profile)
        self.__profile.insert(profile)
        return self.get_profile(data["user_id"])

    def update_profile(self, data: dict) -> Profile:
        profile = deserialize(data, Profile)
        self.__profile.update(profile)
        return self.get_profile(data["user_id"])

    def delete_profile(self, user_id: int):
        return self.__profile.delete(user_id)
