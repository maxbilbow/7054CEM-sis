from typing import Union

from core.model.insurance_policy import InsuranceType
from core.model.quote import Quote
from core.repository.quote import QuoteRepository
from core.service.profile_service import ProfileService
from core.utils.deserialization import deserialize


class QuoteService:
    __repo: QuoteRepository

    def __init__(self, repo=QuoteRepository()):
        self.__repo = repo

    def get_quote(self, quote_id: int):
        return self.__repo.find_by_id(quote_id)

    def find_for_user(self, user_id: int):
        return self.__repo.find_by_userid(user_id)

    def new_quote(self, user_id: int, insurance_type: str) -> Quote:
        profile = ProfileService().get_profile(user_id)
        if InsuranceType[insurance_type] == InsuranceType.Motor:
            return self.__repo.new_motor_quote(user_id, profile)
        else:
            return self.__repo.new_home_quote(user_id, profile)

    def update_quote(self, quote_id: int, data: Union[dict, Quote]) -> Quote:
        quote: Quote
        if isinstance(data, Quote):
            quote = data
        else:
            data["id"] = quote_id
            quote = deserialize(data, Quote)
        return self.__repo.update(quote)

    def delete_quote(self, quote_id):
        return self.__repo.delete(quote_id)
