from core.model.insurance_policy import InsuranceType
from core.model.quote import Quote
from web.service.auth_service import AuthService


class QuoteService:
    def get_all(self):
        return [Quote(-1, AuthService.get_user_id())]

    def get(self, quote_id: int):
        return Quote(quote_id, AuthService.get_user_id())

    def new_quote(self, insurance_type: InsuranceType):
        return -1

    def update_quote(self, quote: dict):
        return self.get(quote["id"])

    def delete_quote(self, quote_id: int):
        return True
