from typing import Optional

from injector import inject

from core.model import to_dict
from core.model.profile import Profile
from web.repository.api import Api
from web.service.auth_service import AuthService


class UserProfileService:
    __api: Api

    @inject
    def __init__(self, api: Api):
        self.__api = api

    def get(self) -> Optional[dict]:
        user_id = AuthService.get_user_id()
        profile = self.__api.get(f"/user/{user_id}/profile")
        return profile

    def insert_or_update(self, profile: Profile) -> dict:
        user_id = AuthService.get_user_id()
        if self.get() is None:
            return self.__api.post(f"/user/{user_id}/profile", json=to_dict(profile))
        else:
            return self.__api.put(f"/user/{user_id}/profile", json=to_dict(profile))
