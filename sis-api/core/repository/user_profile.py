from core.model import get_keys, to_dict
from core.model.profile import Profile
from core.repository import mysql
from swagger_server.models import PersonalDetails, DriverHistory, Address


class UserProfileRepository:

    @staticmethod
    def insert(profile: Profile):
        with mysql.session() as con:
            pd_table = con.on_table("personal_details")
            address_table = con.on_table("address")
            dh_table = con.on_table("driver_history")
            profile_table = con.on_table("user_profile")
            claim_table = con.on_table("previous_claim")

            address_keys = get_keys(profile.personal_details.address, exclude=["id"])
            profile.personal_details.address.id = address_table.insert(profile.personal_details.address, address_keys)

            pd_keys = get_keys(profile.personal_details, exclude=["id", "address"])
            profile.personal_details.id = pd_table.insert(profile.personal_details, pd_keys)

            dh_keys = get_keys(profile.driver_history, exclude=["id", "previous_claims"])

            profile.driver_history.id = dh_table.insert(profile.driver_history, dh_keys)

            for claim in profile.driver_history.previous_claims:
                claim.driver_history_id = profile.driver_history.id
                claim_keys = get_keys(claim, exclude=["id"])
                claim_table.insert(claim, claim_keys)

            profile_table.insert(profile, keys=["user_id", "personal_details_id", "driver_history_id"])
            con.commit()

    @staticmethod
    def find_by_user_id(user_id: int):
        with mysql.session() as s:
            profile = s.on_table("user_profile").find_by(["user_id", user_id]).fetchone()
            if profile is None:
                return None

            if profile["personal_details_id"] is None:
                profile["personal_details"] = to_dict(PersonalDetails(relationship_status="", employment_status=""))
            else:
                profile["personal_details"] = s.on_table("personal_details").find_by(
                    ["id", profile["personal_details_id"]]
                ).fetchone()
                address_id = profile["personal_details"]["address_id"]
                address = to_dict(Address()) if address_id is None else s.on_table("address").find_by(
                    ["id", address_id]
                )
                profile["personal_details"]["address"] = address

            if profile["driver_history_id"] is not None:
                profile["driver_history"] = s.on_table("driver_history").find_by(
                    ["id", profile["driver_history_id"]]).fetchone()
                profile["driver_history"]["previous_claims"] = s.on_table("previous_claim").find_by(
                    ["driver_history_id", profile["driver_history_id"]]
                ).fetchall()
            else:
                profile["driver_history"] = DriverHistory(licence_type="").to_dict()

            return Profile.from_dict(profile)

    @staticmethod
    def update(profile: Profile):
        with mysql.session() as s:
            if profile.personal_details.address.id is None:
                keys = get_keys(profile.personal_details.address, exclude=["id"])
                s.on_table("address").insert(profile.personal_details.address, keys=keys)
            else:
                s.on_table("address").update(profile.personal_details.address)
            pd_keys = get_keys(profile.personal_details, exclude=["address"])
            s.on_table("personal_details").update(profile.personal_details, pd_keys)
            keys = get_keys(profile.driver_history, exclude=["previous_claims"])
            s.on_table("driver_history").update(profile.driver_history, keys)
            s.commit()

    @staticmethod
    def delete(user_id: int):
        profile = UserProfileRepository.find_by_user_id(user_id)
        address_id = profile.personal_details.address.id
        pd_id = profile.personal_details_id
        dh_id = profile.driver_history_id
        with mysql.session() as s:
            s.on_table("user_profile").delete(["user_id", user_id])
            s.on_table("personal_details").delete(pd_id)
            s.on_table("address").delete(address_id)
            s.on_table("driver_history").delete(dh_id)
            s.commit()
