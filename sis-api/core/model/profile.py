from copy import copy
from dataclasses import dataclass, field

from .base_model import BaseModel
from .roles import Role


@dataclass(frozen=True, eq=True)
class Profile(BaseModel):
    user_id: int = field(metadata={"Key": True}, default=-1)
    name: str = field(default="")
    points: int = field(default=0)
    role: Role = field(default=Role.Member)

    # Entities
    # membership: Optional[Membership] = field(default=None)

    # insurance_packages: List[InsurancePolicy] = field(default_factory=list)

    def __post_init__(self):
        if isinstance(self.role, str):
            raise TypeError("membership type is not an enum")

    @classmethod
    def from_dict(cls, data: dict):
        data = copy(data)
        data["role"] = Role[data["role"]]
        return cls(**data)
