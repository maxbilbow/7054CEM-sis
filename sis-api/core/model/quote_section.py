from dataclasses import field, dataclass
from typing import List

from core.model.base_model import BaseModel
from core.model.meta import PK, FK
from swagger_server.models import DriverDetails, VehicleDetails, VehicleUsage, PersonalDetails, HomeDetails


class QuoteSection(BaseModel):
    quote_id: int = field(metadata={PK: True, FK: True})


@dataclass(frozen=True, eq=True)
class VehicleQuoteSections(QuoteSection):
    personal_details_id: int
    driver_history_id: int

    driver_details: DriverDetails = field(default_factory=DriverDetails)
    vehicle_details: VehicleDetails = field(default_factory=VehicleDetails)
    vehicle_usage: VehicleUsage = field(default_factory=VehicleUsage)
    additional_drivers: List[DriverDetails] = field(default_factory=list)


class HomeQuoteSections:
    personal_details_id: int
    home_details_id: int

    personal_details: PersonalDetails
    home_details: HomeDetails
