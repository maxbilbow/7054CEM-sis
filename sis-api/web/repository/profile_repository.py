import dataclasses
from typing import Optional

from injector import singleton, inject

from core.model import to_dict
from core.model.membership import Membership
from core.model.profile import Profile
from web.repository.api import Api


@singleton
class ProfileRepository:
    __api: Api

    @inject
    def __init__(self, api: Api):
        self.__api = api

    def get(self, user_id: int) -> Optional[Profile]:
        profile = self.__api.get(f"/user/{user_id}/profile")
        return None if not profile else Profile(**profile)

    def insert(self, user_id: int, profile: Profile):
        return self.__api.post(f"/user/{user_id}/profile", json=to_dict(profile))

    def update(self, user_id: int, profile: Profile):
        return self.__api.put(f"/user/{user_id}/profile", json=to_dict(profile))

