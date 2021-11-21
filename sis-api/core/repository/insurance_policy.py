import dataclasses
from typing import List

from core.model.insurance_policy import InsurancePolicy
from core.model.profile import Profile
from core.repository import mysql


class InsurancePolicyRepository:

    @staticmethod
    def insert(policy: InsurancePolicy) -> InsurancePolicy:
        id = mysql.insert(table_name="insurance_policy", entity=policy, exclude_keys=["type", "id"])
        return dataclasses.replace(policy, id=id)

    @staticmethod
    def find_by_user_id(user_id: int) -> List[InsurancePolicy]:
        rows = mysql.find_all_by(table_name="insurance_policy", key="user_id", key_value=user_id)
        return [InsurancePolicy.from_dict(row) for row in rows]

    @staticmethod
    def update(user_id: int, profile: Profile):
        return mysql.update_by_pk(pk_name="user_id",
                                  pk=user_id,
                                  table_name="insurance_policy",
                                  entity=profile,
                                  exclude_keys=["membership", "benefits", "insurance_packages"])

    @staticmethod
    def delete(user_id: int):
        return mysql.delete_by(table_name="insurance_policy", key="user_id", key_value=user_id)
