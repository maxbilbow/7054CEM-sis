from datetime import date
from typing import List

from injector import singleton, inject

from repository.api import Api
from service.auth_service import AuthService


@singleton
class InsurancePolicyService:
    __api: Api

    @inject
    def __init__(self, api: Api):
        self.__api = api

    def get_all(self) -> List[dict]:
        user_id = AuthService.get_user_id()
        return self.__api.get(f"/user/{user_id}/insurance_policy")

    def create(self, package_id: int, start_date: date) -> dict:
        pass
