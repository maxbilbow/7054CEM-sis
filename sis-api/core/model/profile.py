from dataclasses import dataclass, field

from .base_model import BaseModel
from .driver_history import DriverHistory
from .meta import PK, FK
from .personal_details import PersonalDetails


@dataclass(frozen=False, eq=True)
class Profile(BaseModel):
    user_id: int = field(metadata={PK: True, FK: True})

    # Entities
    personal_details: PersonalDetails = field(default_factory=PersonalDetails, metadata={FK: True})
    driver_history: DriverHistory = field(default_factory=DriverHistory, metadata={FK: True})
