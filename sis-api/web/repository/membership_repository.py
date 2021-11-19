from typing import Optional

from injector import singleton, inject

from core.model import to_dict
from core.model.membership import Membership
from web.repository.api import Api


@singleton
class MembershipRepository:
    __api: Api

    @inject
    def __init__(self, api: Api):
        self.__api = api

    def find_by_userid(self, user_id: int) -> Optional[Membership]:
        membership = self.__api.get(f"/user/{user_id}/membership")
        return None if not membership else Membership.from_dict(membership)

    def update(self, user_id: int, membership: Membership) -> Optional[Membership]:
        self.__api.put(f"/user/{user_id}/membership", json=to_dict(membership))
        return self.find_by_userid(user_id)

    def create(self, user_id: int, membership: Membership) -> Optional[Membership]:
        self.__api.post(f"/user/{user_id}/membership", json=to_dict(membership))
        return self.find_by_userid(user_id)

    def cancel(self, user_id: int) -> Optional[Membership]:
        self.__api.delete(f"/user/{user_id}/membership")
        return self.find_by_userid(user_id)
