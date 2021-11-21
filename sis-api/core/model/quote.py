from copy import copy
from dataclasses import dataclass, field
from typing import Optional

from core.model.base_model import BaseModel
from core.model.insurance_policy import InsuranceType


@dataclass(frozen=True, eq=True)
class Quote(BaseModel):
    id: int = field(metadata={"Key": True})
    user_id: int
    type: InsuranceType
    created: int = field(default=-1)
    updated: int = field(default=-1)
    is_complete: bool = field(default=False)
    price: Optional[float] = field(default=None)

    def __post_init__(self):
        if isinstance(self.type, str):
            raise TypeError("Insurance type is not an enum")

    @classmethod
    def from_dict(cls, data: dict):
        data = copy(data)
        data["type"] = InsuranceType[data["type"]]
        data["is_complete"] = True if data["is_complete"] else False
        return cls(**data)


