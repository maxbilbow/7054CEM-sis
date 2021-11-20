from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True, eq=True)
class User:
    id: int = field(metadata={"Key": True})
    email: str
    password_hash: Optional[str]


