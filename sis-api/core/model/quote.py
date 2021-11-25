import logging
import time
from typing import Optional

from core.model.home_quote_sections import HomeQuoteSections
from core.model.meta import *
from core.model.quote_sections import *
from core.model.vehicle_quote_sections import VehicleQuoteSections
from core.utils.deserialization import deserialize

from dataclasses import dataclass, field


def quote_sections_factory(data: dict) -> QuoteSections:
    if data is not None:
        if data["quote_type"] == InsuranceType.Motor.name:
            return deserialize(data, VehicleQuoteSections)
        elif data["quote_type"] == InsuranceType.Home.name:
            return deserialize(data, HomeQuoteSections)
    logging.warning(f"Unable to determine sections type for {data}")


@dataclass(frozen=True, eq=True)
class Quote(BaseModel):
    id: Optional[int] = field(metadata={PK: True, GENERATED: True})
    user_id: int = field(metadata={FK: True})
    type: InsuranceType
    sections: Optional[QuoteSections] = field(metadata={DESERIALIZER: quote_sections_factory, SQL_COLUMN: False})
    created: int = field(default_factory=lambda: int(time.time() * 1000), metadata={SQL_UPDATE: False})
    updated: int = field(default_factory=lambda: int(time.time() * 1000))
    is_complete: bool = field(default=False)
    price: Optional[float] = field(default=None)
