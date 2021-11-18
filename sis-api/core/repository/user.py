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
        return User(*result)

    @staticmethod
    def find_by_email(email: str):
        result = mysql.find_by(table_name="user", key="email", key_value=email)
        return User(*result)

    @staticmethod
    def update(user_id: int, user: User):
        return mysql.update_by_pk(pk=user_id, table_name="user", entity=user)

    @staticmethod
    def delete(user_id: int):
        return mysql.delete_by(table_name="user", key="id", key_value=user_id)
