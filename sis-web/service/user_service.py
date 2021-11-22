from typing import Optional

from injector import singleton, inject

from web_exceptions import NotFoundError
from repository.api import Api


@singleton
class UserService:
    __api: Api

    @inject
    def __init__(self, api: Api):
        self.__api = api

    def find_by_id(self, id: int) -> dict:
        return self.__api.get(f"/user/{id}")

    def find_user_by_email(self, email: str) -> Optional[dict]:
        user_id = self.__api.get(f"/user-id/{email}")
        if user_id is not None:
            return self.find_by_id(user_id)
        else:
            raise NotFoundError(email)

    def check_credentials(self, email: str, password: str) -> Optional[dict]:
        response = self.__api.post(f"/user/verify", json={
            "email": email,
            "password": password
        })
        return self.find_by_id(response["user_id"])

    def create_user(self, email: str, password: str) -> dict:
        response = self.__api.post(f"/user", json={
            "email": email,
            "password": password
        })
        user_id = response["user_id"]
        return self.find_by_id(user_id)
