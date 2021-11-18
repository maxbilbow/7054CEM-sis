from typing import List

import core.repository.mysql
from swagger_server import db
from core.model.benefit import Benefit
from core.model.profile import Profile
from core.repository import mysql


class BenefitRepository:

    @staticmethod
    def find_for_profile(profile: Profile) -> List[Benefit]:
        con = core.repository.mysql.connect()
        cur = con.cursor()
        try:
            cur.execute(f"SELECT * FROM `benefit` WHERE min_status <= {profile}")
            entry = cur.fetchone()
            con.commit()
            return entry
        finally:
            cur.close()
            con.close()

