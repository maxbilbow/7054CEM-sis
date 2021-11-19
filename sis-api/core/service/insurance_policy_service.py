from core.repository.insurance_policy import InsurancePolicyRepository


class InsurancePolicyService:
    __repo: InsurancePolicyRepository

    def __init__(self, repo=InsurancePolicyRepository()):
        self.__repo = repo

    def find_for_user(self, user_id: int):
        return self.__repo.find_by_user_id(user_id)
