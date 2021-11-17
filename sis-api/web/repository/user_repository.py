from core.model.user import User
from .profile_repository import ProfileRepository


class UserRepository:

    @staticmethod
    def get_user(id: int) -> User:
        profile = ProfileRepository.get_profile(user_id=id)
        email = "Unknown"
        name = "Unknown"
        return User(id=id, profile=profile, email=email, name=name)
