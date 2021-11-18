from injector import singleton, inject

from core.model.profile import Profile
from web.repository.profile_repository import ProfileRepository
from web.service.auth_service import AuthService


@singleton
class UserProfileService:
    __repository: ProfileRepository

    @inject
    def __init__(self, repository: ProfileRepository):
        self.__repository = repository

    def get_profile(self) -> Profile:
        user_id = AuthService.get_user_id()
        return self.__repository.get_profile(user_id)
