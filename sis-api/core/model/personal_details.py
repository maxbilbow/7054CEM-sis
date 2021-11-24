from dataclasses import dataclass, field
from datetime import date
from typing import Optional

from core.model.address import Address
from core.model.meta import GENERATED, PK, FK


@dataclass(frozen=False, eq=True)
class PersonalDetails:
    id: Optional[int] = field(metadata={PK: True, GENERATED: True}, default=None)
    full_name: Optional[str] = field(default=None)
    address: Address = field(default_factory=Address, metadata={FK: True})
    dob: Optional[date] = field(default=None)
    relationship_status: Optional[str] = field(default=None)
    home_owner: Optional[bool] = field(default=None)
    dependents: Optional[int] = field(default=None)
    employment_status: Optional[str] = field(default=None)
