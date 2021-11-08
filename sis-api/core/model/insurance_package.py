from dataclasses import dataclass, field
from enum import Enum

from .roles import Role


class InsuranceType(Enum):
    Home = "Home"
    Motor = "Motor"


@dataclass(frozen=True, eq=True)
class InsurancePackage:
    id: int = field(metadata={"Key": True})
    type: Role = field(repr=False, default=Role.NONE)

