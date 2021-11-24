from dataclasses import dataclass, field
from typing import Optional

from core.model.base_model import BaseModel
from core.model.meta import PK, GENERATED


@dataclass(frozen=False, eq=True)
class Address(BaseModel):
    id: Optional[int] = field(metadata={PK: True, GENERATED: True}, default=None)
    number_or_name: Optional[str] = field(default=None)
    street: Optional[str] = field(default=None)
    town: Optional[str] = field(default=None)
    county: Optional[str] = field(default=None)
    postcode: Optional[str] = field(default=None)