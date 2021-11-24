import dataclasses
import time
from typing import Optional, List

from core.model.driver_details import DriverDetails
from core.model.driver_history import DriverHistory
from core.model.insurance_policy import InsuranceType
from core.model.profile import Profile
from core.model.quote import Quote
from core.model.quote_sections import VehicleQuoteSections, HomeQuoteSections, QuoteSections
from core.model.vehicle_details import VehicleDetails
from core.model.vehicle_usage import VehicleUsage
from core.repository import mysql
from core.utils.deserialization import deserialize


class QuoteRepository:

    @staticmethod
    def new_motor_quote(user_id: int, profile: Profile):
        quote = Quote(id=None, user_id=user_id, type=InsuranceType.Motor, sections=QuoteSections())
        with mysql.session() as s:
            quote_id = s.on_table("quote").insert(quote)
            driver_history = DriverHistory()
            driver_history_id = s.on_table("driver_history").insert(driver_history)
            driver_history = dataclasses.replace(driver_history, id=driver_history_id)
            driver_details = DriverDetails(quote_id, personal_details=profile.personal_details,
                                           driver_history=driver_history)

            sections = VehicleQuoteSections(
                quote_id=quote_id, driver_details=driver_details, vehicle_details=VehicleDetails(quote_id),
                vehicle_usage=VehicleUsage(quote_id)
            )

            s.on_table("quote_sections").insert(sections)
            s.on_table("driver_details").insert(driver_details)
            s.on_table("vehicle_details").insert(sections.vehicle_details)
            s.on_table("vehicle_usage").insert(sections.vehicle_usage)
            s.on_table("vehicle_usage").insert(sections.vehicle_usage)
            s.commit()
            return quote  # QuoteRepository.find_by_id(quote_id)

    @staticmethod
    def new_home_quote(user_id: int, profile: Profile):
        pass

    @staticmethod
    def find_by_id(id: int) -> Optional[Quote]:
        with mysql.session() as s:
            quote_matcher = ["quote_id", id]
            quote = s.on_table("quote").find_by(quote_matcher)
            if quote is None:
                return None

            quote["quote_sections"] = s.on_table("quote_sections").find_by(quote_matcher)
            quote["quote_sections"]["driver_details"] = s.on_table("driver_details").find_by(quote_matcher)
            personal_details_id = quote["quote_sections"]["driver_details"]["personal_details_id"]
            driver_history_id = quote["quote_sections"]["driver_details"]["driver_history_id"]
            quote["quote_sections"]["driver_details"]["personal_details"] = s.on_table("personal_details").find_by(
                ["personal_details_id", personal_details_id]
            )
            quote["quote_sections"]["driver_details"]["driver_history"] = s.on_table("driver_history").find_by(
                ["driver_history_id", driver_history_id]
            )
            quote["quote_sections"]["vehicle_details"] = s.on_table("vehicle_details").find_by(quote_matcher)
            quote["quote_sections"]["vehicle_usage"] = s.on_table("vehicle_usage").find_by(quote_matcher)

            return deserialize(quote, Quote)

    @staticmethod
    def find_by_userid(user_id: int) -> List[Quote]:
        rows = mysql.find_all_by(table_name="quote", key="user_id", key_value=user_id)
        return [Quote.from_dict(row) for row in rows]

    @staticmethod
    def update(quote: Quote):
        quote = dataclasses.replace(quote, updated=int(time.time() * 1000))
        return mysql.update_by_pk(pk_name="id",
                                  pk=quote.id,
                                  table_name="quote",
                                  entity=quote,
                                  exclude_keys=["created"])

    @staticmethod
    def delete(id: int):
        return mysql.delete_by(table_name="quote", key="id", key_value=id)
