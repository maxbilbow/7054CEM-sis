import dataclasses
from typing import Optional

from core.repository import mysql
from core.model.user import User


class UserRepository:

    @staticmethod
    def insert_user(email: str, password_hash: str):
        id = mysql.insert(table_name="user",
                          exclude_keys=["id"],
                          entity=User(id=-1, email=email, password_hash=password_hash))
        return User(id=id, email=email, password_hash=password_hash)

    @staticmethod
    def find_by_id(user_id: int):
        result = mysql.find_by(table_name="user", key_value=user_id)
        if not result:
            return None
        return dataclasses.replace(User(**result), password_hash=None)

    @staticmethod
    def find_by_email(email: str):
        result = mysql.find_by(table_name="user", key="email", key_value=email)
        return None if result is None else User(**result)

    @staticmethod
    def update(user_id: int, email: Optional[str], password: Optional[str]) -> User:
        exclude = ["password_hash"] if password is None else list()
        if email is None:
            exclude.append("email")
        user = User(user_id, email, password)
        return mysql.update_by_pk(pk=user_id, table_name="user", entity=user, exclude_keys=exclude)

    @staticmethod
    def delete(user_id: int):
        return mysql.delete_by(table_name="user", key="id", key_value=user_id)
