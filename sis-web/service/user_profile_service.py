from typing import Optional

from injector import inject

from repository.api import Api
from service.auth_service import AuthService


class UserProfileService:
    __api: Api

    @inject
    def __init__(self, api: Api):
        self.__api = api

    def get(self) -> Optional[dict]:
        user_id = AuthService.get_user_id()
        profile = self.__api.get(f"/user/{user_id}/profile")
        return profile

    def insert_or_update(self, profile: dict) -> dict:
        user_id = AuthService.get_user_id()
        if self.get() is None:
            return self.__api.post(f"/user/{user_id}/profile", json=profile)
        else:
            return self.__api.put(f"/user/{user_id}/profile", json=profile)
