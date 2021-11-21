from typing import Optional

from injector import singleton, inject

from core.model.user import User
from web.exceptions import NotFoundError
from web.repository.api import Api


@singleton
class UserService:
    __api: Api

    @inject
    def __init__(self, api: Api):
        self.__api = api

    def find_by_id(self, id: int) -> User:
        user_dict = self.__api.get(f"/user/{id}")
        return User.from_dict(user_dict)

    def find_user_by_email(self, email: str) -> Optional[User]:
        user_id = self.__api.get(f"/user-id/{email}")
        if user_id is not None:
            return self.find_by_id(user_id)
        else:
            raise NotFoundError(email)

    def check_credentials(self, email: str, password: str) -> Optional[User]:
        response = self.__api.post(f"/user/verify", json={
            "email": email,
            "password": password
        })
        return self.find_by_id(response["user_id"])

    def create_user(self, email: str, password: str) -> User:
        response = self.__api.post(f"/user", json={
            "email": email,
            "password": password
        })
        user_id = response["user_id"]
        return self.find_by_id(user_id)
