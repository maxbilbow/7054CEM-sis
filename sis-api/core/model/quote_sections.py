from dataclasses import field, dataclass
from typing import List

from core.model.base_model import BaseModel
from core.model.driver_details import DriverDetails
from core.model.insurance_policy import InsuranceType
from core.model.meta import PK, FK
from core.model.personal_details import PersonalDetails
from core.model.vehicle_details import VehicleDetails
from core.model.vehicle_usage import VehicleUsage
from swagger_server.models import HomeDetails


class QuoteSections(BaseModel):
    quote_id: int
    quote_type: InsuranceType


@dataclass(frozen=True, eq=True)
class VehicleQuoteSections(QuoteSections):
    quote_id: int = field(metadata={PK: True, FK: True})
    driver_details: DriverDetails
    vehicle_details: VehicleDetails
    vehicle_usage: VehicleUsage
    quote_type: InsuranceType = field(default=InsuranceType.Motor)
    additional_drivers: List[DriverDetails] = field(default_factory=list)


@dataclass(frozen=True, eq=True)
class HomeQuoteSections(QuoteSections):
    quote_id: int = field(metadata={PK: True, FK: True}, default=-1)
    quote_type: InsuranceType = field(default=InsuranceType.Home)
    personal_details: PersonalDetails = field(default_factory=PersonalDetails)
    home_details: HomeDetails = field(default_factory=HomeDetails)

    @property
    def personal_details_id(self) -> int:
        return self.personal_details.id
