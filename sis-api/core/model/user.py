from dataclasses import dataclass, field
from typing import Optional

from core.model.base_model import BaseModel
from core.model.meta import PK


@dataclass(frozen=True, eq=True)
class User(BaseModel):
    id: Optional[int] = field(metadata={PK: True})
    email: str
    password_hash: Optional[str]


