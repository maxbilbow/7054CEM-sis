from core.model.profile import Profile
from core.model.roles import Role


class ProfileRepository:

    @staticmethod
    def get_profile(user_id: int) -> Profile:
        return Profile(user_id=user_id, role=Role.Member, membership=None, points=0)
