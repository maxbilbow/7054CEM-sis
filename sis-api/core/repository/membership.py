from datetime import date
from typing import Optional

import core.repository.mysql
from core.model.membership import Membership
from core.model.membership_type import MembershipType
from core.repository import mysql


class MembershipRepository:

    @staticmethod
    def find_by_id(id: int) -> Membership:
        res = mysql.find_by(table_name="membership", key="id", key_value=id)
        return Membership.from_dict(res)

    @staticmethod
    def create(user_id: int, membership_type: MembershipType, start_date: date,
               end_date: Optional[date] = None) -> Membership:
        membership = Membership(id=-1, user_id=user_id, type=membership_type, start_date=start_date,
                                end_date=end_date)
        id = mysql.insert(table_name="membership", entity=membership, exclude_keys=["id"])
        return MembershipRepository.find_by_id(id)

    @staticmethod
    def find_by_user_id(user_id: int) -> Membership:
        con = core.repository.mysql.connect()
        cur = con.cursor(dictionary=True)
        try:
            cur.execute(f"SELECT * FROM `membership` WHERE user_id = {user_id}"
                        f" AND start_date <= CURRENT_DATE()"
                        f" AND end_date >= CURRENT_DATE()")
            entry = cur.fetchone()
            con.commit()
            return None if not entry else Membership.from_dict(entry)
        finally:
            cur.close()
            con.close()

    @staticmethod
    def update_current(user_id: int, membership: Membership):
        pk = MembershipRepository.find_by_user_id(user_id).id
        mysql.update_by_pk(table_name="membership", pk=pk, entity=membership, exclude_keys=["id", "user_id"])
        return MembershipRepository.find_by_id(pk)

    @staticmethod
    def delete(membership: Membership):
        mysql.delete_by(table_name="membership", key_value=membership.id)
