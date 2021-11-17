from core.model.profile import Profile


class ProfileRepository:

    @staticmethod
    def get_profile(user_id: int) -> Profile:
        return Profile(id=id)
