from typing import Optional

from core.model.driver_history import DriverHistory
from core.model.profile import Profile
from core.repository import mysql
from core.repository.mysql import _Session
from core.utils.deserialization import deserialize


class UserProfileRepository:

    @staticmethod
    def insert(profile: Profile):
        with mysql.session() as s:
            profile.personal_details.address.id = s.on_table("address").insert(profile.personal_details.address)

            profile.personal_details.id = s.on_table("personal_details").insert(profile.personal_details)

            profile.driver_history.id = s.on_table("driver_history").insert(profile.driver_history)

            UserProfileRepository._update_claims(s, profile.driver_history)

            s.on_table("user_profile").insert(profile, replace=True)
            s.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> Optional[Profile]:
        with mysql.session() as s:
            profile = s.on_table("user_profile").find_by(["user_id", user_id]).fetchone()
            if profile is None:
                return None

            profile["personal_details"] = UserProfileRepository.find_personal_details(s, profile["personal_details_id"])

            profile["driver_history"] = UserProfileRepository._find_driver_history(s, profile)

            return deserialize(profile, to_class=Profile)

    @staticmethod
    def _update_claims(s: _Session, driver_history: DriverHistory):
        s.on_table("previous_claim").delete(["driver_history_id", driver_history.id])
        for claim in driver_history.previous_claims:
            claim.driver_history_id = driver_history.id
            claim.id = s.on_table("previous_claim").insert(claim)

    @staticmethod
    def update(profile: Profile):
        with mysql.session() as s:
            if profile.personal_details.address.id is None:
                profile.personal_details.address.id = s.on_table("address").insert(profile.personal_details.address)
            else:
                s.on_table("address").update(profile.personal_details.address)

            if profile.personal_details.id is None:
                profile.personal_details.id = s.on_table("personal_details").insert(profile.personal_details)
            else:
                s.on_table("personal_details").update(profile.personal_details)

            if profile.driver_history.id is None:
                profile.driver_history.id = s.on_table("driver_history").insert(profile.driver_history)
            else:
                s.on_table("driver_history").update(profile.driver_history)

            UserProfileRepository._update_claims(s, profile.driver_history)

            s.on_table("user_profile").update(profile)
            s.commit()

    @staticmethod
    def delete(user_id: int):
        profile = UserProfileRepository.find_by_user_id(user_id)
        pd_id = profile.personal_details.id
        dh_id = profile.driver_history.id
        address = profile.personal_details.address
        with mysql.session() as s:
            s.on_table("user_profile").delete(["user_id", user_id])
            if pd_id is not None:
                s.on_table("personal_details").delete(pd_id)
            if address.id is not None:
                s.on_table("address").delete(address.id)
            if dh_id is not None:
                s.on_table("driver_history").delete(dh_id)
            s.commit()

    @staticmethod
    def find_personal_details(s: _Session, personal_details_id: Optional[int]) -> Optional[dict]:
        if personal_details_id is None:
            return None

        personal_details = s.on_table("personal_details").find_by(["id", personal_details_id]).fetchone()
        if personal_details is None:
            return None

        address_id = personal_details["address_id"]
        if address_id is not None:
            personal_details["address"] = s.on_table("address").find_by(["id", address_id]).fetchone()

        return personal_details

    @staticmethod
    def _find_driver_history(s: _Session, profile: dict) -> Optional[dict]:
        if profile["driver_history_id"] is None:
            return None

        driver_history = s.on_table("driver_history").find_by(["id", profile["driver_history_id"]]).fetchone()

        if driver_history is not None:
            driver_history["previous_claims"] = s.on_table("previous_claim") \
                .find_by(["driver_history_id", profile["driver_history_id"]]) \
                .fetchall()

        return driver_history
