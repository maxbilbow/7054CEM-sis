import urllib.parse
from typing import Optional

from injector import singleton, inject

import config
from core.model.user import User
from web.exceptions import NotFoundError
from web.repository import api
from web.repository.api import Api


@singleton
class UserRepository:
    __api: Api

    @inject
    def __init__(self, api: Api):
        self.__api = api

    def find_by_id(self, id: int) -> User:
        user_dict = self.__api.get(f"/user/{id}")
        return User(**user_dict)

    def find_user_by_email(self, email: str) -> Optional[User]:
        user_id = self.__api.get(f"/user-id/{email}")
        if user_id is not None:
            return self.find_by_id(user_id)
        else:
            raise NotFoundError(email)

    def create_user(self, email: str, password_hash: str) -> User:
        response = self.__api.post(f"/user", json={
            "email": email,
            "password_hash": password_hash
        })
        user_id = response["user_id"]
        return self.find_by_id(user_id)
