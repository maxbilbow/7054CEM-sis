from dataclasses import dataclass, field
from core.model.meta import PK, FK


@dataclass(frozen=True, eq=True)
class VehicleDetails:
    quote_id: int = field(metadata={PK: True, FK: True})
