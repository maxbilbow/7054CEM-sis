from dataclasses import dataclass, field
from typing import List

from core.model.driver_details import DriverDetails
from core.model.insurance_policy import InsuranceType
from core.model.meta import PK, FK
from core.model.quote_sections import QuoteSections
from core.model.vehicle_details import VehicleDetails
from core.model.vehicle_usage import VehicleUsage


@dataclass(frozen=True, eq=True)
class VehicleQuoteSections(QuoteSections):
    quote_id: int = field(metadata={PK: True, FK: True})
    driver_details: DriverDetails
    vehicle_details: VehicleDetails
    vehicle_usage: VehicleUsage
    quote_type: InsuranceType = field(default=InsuranceType.Motor)
    additional_drivers: List[DriverDetails] = field(default_factory=list)
