from dataclasses import dataclass, field

from core.model.home_details import HomeDetails
from core.model.insurance_policy import InsuranceType
from core.model.meta import PK, FK
from core.model.personal_details import PersonalDetails
from core.model.quote_sections import QuoteSections


@dataclass(frozen=True, eq=True)
class HomeQuoteSections(QuoteSections):
    quote_id: int = field(metadata={PK: True, FK: True}, default=-1)
    quote_type: InsuranceType = field(default=InsuranceType.Home)
    personal_details: PersonalDetails = field(default_factory=PersonalDetails)
    home_details: HomeDetails = field(default_factory=HomeDetails)
