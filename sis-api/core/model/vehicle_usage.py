from dataclasses import dataclass, field

from core.model.meta import PK, FK
from core.model.quote_sections import QuoteSection


@dataclass(frozen=True, eq=True)
class VehicleUsage(QuoteSection):
    quote_id: int = field(metadata={PK: True, FK: True})
