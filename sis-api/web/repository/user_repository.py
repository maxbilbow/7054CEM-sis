import requests

import config
from core.model.user import User

URL = config.get("api.origin")


class UserRepository:

    @staticmethod
    def find_by_id(id: int) -> User:
        response = requests.get(f"{URL}/user/{id}")
        user_dict = response.json()
        return User(user_dict)

    @staticmethod
    def find_user_by_email(email: str) -> User:
        response = requests.get(f"{URL}/user-id/{email}")
        user_id = response.json()
        return user_id

    @staticmethod
    def create_user(email: str, password_hash: str) -> User:
        response = requests.post(url=f"{URL}/user", json={
            "email": email,
            "password_hash": password_hash
        })
        user_id = response.json()["user_id"]
        return UserRepository.find_by_id(user_id)
