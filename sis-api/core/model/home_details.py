from dataclasses import dataclass, field

from core.model.address import Address
from core.model.meta import PK, FK
from core.model.quote_sections import QuoteSection


@dataclass
class HomeDetails(QuoteSection):
    quote_id: int = field(metadata={PK: True, FK: True})
    address: Address = field(default_factory=Address, metadata={FK: True})
