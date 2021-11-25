from dataclasses import field

from core.model.base_model import BaseModel
from core.model.insurance_policy import InsuranceType


class QuoteSections(BaseModel):
    quote_id: int
    quote_type: InsuranceType


class QuoteSection:
    section_complete: bool = field(default=False)
