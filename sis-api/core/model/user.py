from dataclasses import dataclass, field
from typing import Optional

from .profile import Profile


@dataclass(frozen=True, eq=True)
class User:
    id: int = field(metadata={"Key": True})
    email: str
    password: str
    profile: Optional[Profile] = field(repr=False)
