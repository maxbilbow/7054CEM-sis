from core.model.insurance_policy import InsuranceType
from core.model.quote import Quote
from core.repository.quote import QuoteRepository


class QuoteService:
    __repo: QuoteRepository

    def __init__(self, repo=QuoteRepository()):
        self.__repo = repo

    def get_quote(self, quote_id: int):
        return self.__repo.find_by_id(quote_id)

    def find_for_user(self, user_id: int):
        return self.__repo.find_by_userid(user_id)

    def new_quote(self, user_id: int, insurance_type: InsuranceType):
        return self.__repo.insert(Quote(-1, user_id, insurance_type))

    def update_quote(self, quote_id: int, data: dict):
        data["id"] = quote_id
        quote = Quote.from_dict(data)
        return self.__repo.update(quote)

    def delete_quote(self, quote_id):
        return self.__repo.delete(quote_id)
