from dataclasses import dataclass, field
from typing import Optional

from .profile import Profile


@dataclass(frozen=True, eq=True)
class User:
    id: int = field(metadata={"Key": True})
    email: str
    password_hash: str

    # Entities
    profile: Optional[Profile] = field(default=None)


