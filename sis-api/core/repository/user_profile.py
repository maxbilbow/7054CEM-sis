from core.model.profile import Profile
from core.repository import mysql


class UserProfileRepository:

    @staticmethod
    def insert(profile: Profile):
        mysql.insert(table_name="user_profile", entity=profile,
                     exclude_keys=["membership", "benefits", "insurance_packages"])
        return profile

    @staticmethod
    def find_by_user_id(user_id: int):
        result = mysql.find_by(table_name="user_profile", key="user_id", key_value=user_id)
        return None if result is None else Profile(*result)

    @staticmethod
    def update(user_id: int, profile: Profile):
        return mysql.update_by_pk(pk_name="user_id",
                                  pk=user_id,
                                  table_name="user_profile",
                                  entity=profile,
                                  exclude_keys=["membership", "benefits", "insurance_packages"])

    @staticmethod
    def delete(user_id: int):
        return mysql.delete_by(table_name="user_profile", key="user_id", key_value=user_id)

