from dataclasses import dataclass, field

from core.model.meta import PK, FK


@dataclass(frozen=True, eq=True)
class VehicleUsage:
    quote_id: int = field(metadata={PK: True, FK: True})
