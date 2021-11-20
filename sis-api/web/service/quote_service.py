from typing import List

from injector import inject

from core.model.insurance_policy import InsuranceType
from web.repository.api import Api
from web.service.auth_service import AuthService


class QuoteService:
    __api: Api

    @inject
    def __init__(self, api: Api = Api()):
        self.__api = api

    def get_all(self) -> List[dict]:
        user_id = AuthService.get_user_id()
        return self.__api.get(f"/user/{user_id}/quote")

    def get(self, quote_id: int):
        return self.__api.get(f"/quote/{quote_id}")

    def new_quote(self, insurance_type: str):
        user_id = AuthService.get_user_id()
        return self.__api.post(f"/user/{user_id}/quote", json={
            "type": insurance_type
        })

    def update_quote(self, quote: dict):
        return self.__api.put(f"/quote/{quote['id']}", quote)

    def delete_quote(self, quote_id: int):
        return self.__api.delete(f"/quote/{quote_id}")
