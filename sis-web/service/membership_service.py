from datetime import date
from typing import Optional

from injector import singleton, inject

from repository.api import Api
from service.auth_service import AuthService


@singleton
class MembershipService:
    __api: Api

    @inject
    def __init__(self, api: Api):
        self.__api = api

    def get(self, ) -> dict:
        user_id = AuthService.get_user_id()
        res = self.__api.get(f"/user/{user_id}/membership")
        return res if res else None

    def update_membership(self, start_date: str, end_date: str,
                          membership_type: str) -> Optional[dict]:
        user_id = AuthService.get_user_id()
        res = self.__api.put(f"/user/{user_id}/membership", json={
            "start_date": start_date,
            "end_date": end_date,
            "type": membership_type
        })
        return res

    def new_membership(self, end_date: date, start_date: Optional[date],
                       membership_type: str) -> Optional[dict]:
        user_id = AuthService.get_user_id()
        res = self.__api.post(f"/user/{user_id}/membership", json={
            "start_date": start_date.isoformat() if start_date else date.today(),
            "end_date": end_date.isoformat(),
            "type": membership_type if membership_type else "Smart"
        })
        return res

    def cancel_membership(self) -> Optional[dict]:
        user_id = AuthService.get_user_id()
        res = self.__api.delete(f"/user/{user_id}/membership")
        return None if not res else res
