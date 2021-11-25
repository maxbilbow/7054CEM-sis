from dataclasses import dataclass, field

from core.model.base_model import BaseModel
from core.model.driver_history import DriverHistory
from core.model.meta import PK, FK, SQL_COLUMN
from core.model.personal_details import PersonalDetails
from core.model.quote_sections import QuoteSection


@dataclass(frozen=True, eq=True)
class DriverDetails(QuoteSection):
    quote_id: int = field(metadata={PK: True, FK: True})
    personal_details: PersonalDetails = field(metadata={FK: True})
    driver_history: DriverHistory = field(default_factory=lambda: DriverHistory(None), metadata={FK: True})

    @property
    def personal_details_id(self) -> int:
        return self.personal_details.id

    @property
    def driver_history_id(self) -> int:
        return self.driver_history.id
