from dataclasses import dataclass, field
from typing import Optional

from core.model.base_model import BaseModel


@dataclass(frozen=True, eq=True)
class User(BaseModel):
    id: int = field(metadata={"Key": True})
    email: str
    password_hash: Optional[str]


