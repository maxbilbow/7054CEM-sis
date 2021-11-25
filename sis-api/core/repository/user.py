import dataclasses
from typing import Optional

from core.repository import mysql
from core.model.user import User
from core.utils.deserialization import deserialize


class UserRepository:

    @staticmethod
    def insert_user(email: str, password_hash: str):
        with mysql.session() as s:
            user = User(None, email, password_hash)
            id = s.on_table("user").insert(user)
            s.commit()
            return dataclasses.replace(user, id=id)

    @staticmethod
    def find_by_id(user_id: int) -> Optional[User]:
        with mysql.session() as s:
            data = s.on_table("user").find_by(user_id).fetchone()
            if data is None:
                return None
            del data["password_hash"]
            return deserialize(data, User)

    @staticmethod
    def find_by_email(email: str):
        with mysql.session() as s:
            data = s.on_table("user").find_by(["email", email]).fetchone()
            if data is None:
                return None
            del data["password_hash"]
            return deserialize(data, User)

    @staticmethod
    def update(user_id: int, email: Optional[str], password: Optional[str]) -> User:
        keys = list()
        if password is not None:
            keys.append("password_hash")
        if email is not None:
            keys.append("email")
        user = User(user_id, email, password)

        with mysql.session() as s:
            s.on_table("user").update(user, keys=keys)
            s.commit()

        return UserRepository.find_by_id(user_id)

    @staticmethod
    def delete(user_id: int):
        with mysql.session() as s:
            s.on_table("user").delete(user_id)
            s.commit()
