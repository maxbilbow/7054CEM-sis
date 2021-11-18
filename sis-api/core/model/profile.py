from dataclasses import dataclass, field
from typing import Optional, List

from .benefit import Benefit
from .insurance_package import InsurancePackage
from .membership import Membership
from .roles import Role


@dataclass(frozen=True, eq=True)
class Profile:
    user_id: int = field(metadata={"Key": True})
    name: str = field(default="")
    points: int = field(default=0)
    role: Role = field(default=Role.Member)

    # Entities
    membership: Optional[Membership] = field(default=None)
    # insurance_packages: List[InsurancePackage] = field(default_factory=list)



