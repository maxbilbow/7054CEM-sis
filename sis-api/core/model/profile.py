from copy import copy
from dataclasses import dataclass, field
from typing import Optional

from swagger_server.models import DriverHistory, PersonalDetails, Address
from .base_model import BaseModel


@dataclass(frozen=True, eq=True)
class Profile(BaseModel):
    user_id: int = field(metadata={"Key": True}, default=-1)
    personal_details_id: Optional[int] = field(init=False)
    driver_history_id: Optional[int] = field(init=False)

    # Entities
    personal_details: PersonalDetails = field(default_factory=lambda : PersonalDetails(address=Address()))
    driver_history: DriverHistory = field(default_factory=DriverHistory)

    @property
    def personal_details_id(self) -> Optional[int]:
        return self.personal_details.id

    @personal_details_id.setter
    def personal_details_id(self, value: str):
        pass

    @property
    def driver_history_id(self) -> Optional[int]:
        return self.driver_history.id

    @driver_history_id.setter
    def driver_history_id(self, value: str):
        pass

    @classmethod
    def from_dict(cls, data: dict):
        data = copy(data)
        if "personal_details" in data and data["personal_details"] is not None:
            if data["personal_details"]["relationship_status"] is None:
                data["personal_details"]["relationship_status"] = ""
            if data["personal_details"]["employment_status"] is None:
                data["personal_details"]["employment_status"] = ""
            data["personal_details"] = PersonalDetails.from_dict(data["personal_details"])

        if "driver_history" in data and data["driver_history"] is not None:
            if data["driver_history"]["licence_type"] is None:
                data["driver_history"]["licence_type"] = ""
            data["driver_history"] = DriverHistory.from_dict(data["driver_history"])

        if "driver_history_id" in data:
            del data["driver_history_id"]
        if "personal_details_id" in data:
            del data["personal_details_id"]

        return cls(**data)
