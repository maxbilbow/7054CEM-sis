import dataclasses
from typing import Optional, List

from core.model.driver_details import DriverDetails
from core.model.driver_history import DriverHistory
from core.model.home_details import HomeDetails
from core.model.home_quote_sections import HomeQuoteSections
from core.model.insurance_policy import InsuranceType
from core.model.profile import Profile
from core.model.quote import Quote
from core.model.quote_sections import QuoteSections
from core.model.vehicle_details import VehicleDetails
from core.model.vehicle_quote_sections import VehicleQuoteSections
from core.model.vehicle_usage import VehicleUsage
from core.repository import mysql
from core.repository.mysql import _Session
from core.repository.user_profile import UserProfileRepository
from core.utils.deserialization import deserialize


class QuoteRepository:

    @staticmethod
    def new_motor_quote(user_id: int, profile: Profile):
        quote = Quote(id=None, user_id=user_id, type=InsuranceType.Motor, sections=QuoteSections())
        with mysql.session() as s:
            quote_id = s.on_table("quote").insert(quote)
            driver_history = DriverHistory()
            driver_history.id = s.on_table("driver_history").insert(driver_history)
            driver_details = DriverDetails(quote_id, personal_details=profile.personal_details,
                                           driver_history=driver_history)

            sections = VehicleQuoteSections(
                quote_id=quote_id, driver_details=driver_details, vehicle_details=VehicleDetails(quote_id),
                vehicle_usage=VehicleUsage(quote_id)
            )
            quote = dataclasses.replace(quote, sections=sections, id=quote_id)
            s.on_table("quote_sections").insert(sections)
            s.on_table("driver_details").insert(driver_details)
            s.on_table("vehicle_details").insert(sections.vehicle_details)
            s.on_table("vehicle_usage").insert(sections.vehicle_usage)
            s.commit()
        return QuoteRepository.find_by_id(quote.id)

    @staticmethod
    def new_home_quote(user_id: int, profile: Profile):
        quote = Quote(id=None, user_id=user_id, type=InsuranceType.Home, sections=QuoteSections())
        with mysql.session() as s:
            quote_id = s.on_table("quote").insert(quote)
            sections = HomeQuoteSections(
                quote_id=quote_id, personal_details=profile.personal_details,
                home_details=HomeDetails(quote_id, address=profile.personal_details.address)
            )
            quote = dataclasses.replace(quote, sections=sections, id=quote_id)
            s.on_table("home_details").insert(sections.home_details)
            s.on_table("quote_sections").insert(sections)
            s.commit()
            return quote  # QuoteRepository.find_by_id(quote_id)

    @staticmethod
    def find_by_id(id: int) -> Optional[Quote]:
        with mysql.session() as s:
            quote_matcher = "quote_id", id
            quote = s.on_table("quote").find_by(id).fetchone()
            if quote is None:
                return None

            sections = s.on_table("quote_sections").find_by(quote_matcher).fetchone()
            if quote["type"] == InsuranceType.Motor.name:
                sections["driver_details"] = s.on_table("driver_details").find_by(quote_matcher).fetchone()
                personal_details_id = sections["driver_details"]["personal_details_id"]
                driver_history_id = sections["driver_details"]["driver_history_id"]
                sections["driver_details"]["personal_details"] = UserProfileRepository.find_personal_details(s,
                                                                                                             personal_details_id)
                sections["driver_details"]["driver_history"] = \
                    s.on_table("driver_history").find_by(driver_history_id).fetchone()
                sections["vehicle_details"] = s.on_table("vehicle_details").find_by(quote_matcher).fetchone()
                sections["vehicle_usage"] = s.on_table("vehicle_usage").find_by(quote_matcher).fetchone()
            else:
                sections["personal_details"] = UserProfileRepository.find_personal_details(s, sections[
                    "personal_details_id"])

            quote["sections"] = sections
            return deserialize(quote, Quote)

    @staticmethod
    def find_by_userid(user_id: int) -> List[Quote]:
        rows = mysql.find_all_by(table_name="quote", key="user_id", key_value=user_id)
        return [deserialize(row, Quote) for row in rows]

    @staticmethod
    def update(quote: Quote) -> Quote:
        with mysql.session() as s:
            s.on_table("quote").update(quote)
            if quote.type is InsuranceType.Motor:
                sections: VehicleQuoteSections = quote.sections
                s.on_table("driver_history").update(sections.driver_details.driver_history)
                s.on_table("personal_details").update(sections.driver_details.personal_details)
                s.on_table("driver_details").update(sections.driver_details)
                s.on_table("vehicle_details").update(sections.vehicle_details)
                s.on_table("vehicle_usage").update(sections.vehicle_usage)
            else:
                sections: HomeQuoteSections = quote.sections
                s.on_table("home_details").update(sections.home_details)
                s.on_table("personal_details").update(sections.personal_details)
            s.on_table("quote_sections").update(quote.sections)
            s.commit()
        return QuoteRepository.find_by_id(quote.id)

    @staticmethod
    def delete(id: int):
        with mysql.session() as s:
            s.on_table("quote").delete(id)
            s.commit()

    @staticmethod
    def get_personal_details(s: _Session, personal_details_id: int) -> Optional[dict]:
        personal_details = s.on_table("personal_details").find_by(personal_details_id).fetchone()
        if personal_details is None:
            return None
