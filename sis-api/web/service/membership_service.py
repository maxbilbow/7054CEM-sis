from datetime import date
from typing import Optional

from injector import singleton, inject

from core.model.membership import Membership
from core.model.membership_type import MembershipType
from web.repository.api import Api
from web.service.auth_service import AuthService


@singleton
class MembershipService:
    __api: Api

    @inject
    def __init__(self, api: Api):
        self.__api = api

    def get(self, ) -> Optional[Membership]:
        user_id = AuthService.get_user_id()
        res = self.__api.get(f"/user/{user_id}/membership")
        return Membership.from_dict(res) if res else None

    def update_membership(self, start_date: date, end_date: date,
                          membership_type: MembershipType) -> Optional[Membership]:
        user_id = AuthService.get_user_id()
        res = self.__api.put(f"/user/{user_id}/membership", json={
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "type": membership_type.name
        })
        return Membership.from_dict(res)

    def new_membership(self, end_date: date, start_date: Optional[date],
                       membership_type: Optional[MembershipType]) -> Optional[Membership]:
        user_id = AuthService.get_user_id()
        res = self.__api.post(f"/user/{user_id}/membership", json={
            "start_date": start_date.isoformat() if start_date else date.today(),
            "end_date": end_date.isoformat(),
            "type": membership_type.name if membership_type else MembershipType.Smart.name
        })
        return Membership.from_dict(res)

    def cancel_membership(self) -> Optional[Membership]:
        user_id = AuthService.get_user_id()
        res = self.__api.delete(f"/user/{user_id}/membership")
        return None if not res else Membership.from_dict(res)
