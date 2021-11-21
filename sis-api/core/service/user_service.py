from typing import Optional

from injector import singleton, inject
from passlib.hash import pbkdf2_sha256

from core.repository.user import UserRepository
from web.exceptions import BadRequest


@singleton
class UserService:

    @inject
    def __init__(self, repository: UserRepository = UserRepository()):
        self.repository = repository

    def register(self, email: str, password: str):
        # Create the user object
        password_hash = pbkdf2_sha256.encrypt(password)

        # Check for existing email address
        if self.repository.find_by_email(email):
            raise BadRequest("Email address already in use")

        return self.repository.insert_user(email, password_hash)

    def check_credentials(self, email, password) -> bool:
        user = self.repository.find_by_email(email)

        if user and pbkdf2_sha256.verify(password, user.password_hash):
            return True

        return False

    def get_user(self, user_id: int):
        return self.repository.find_by_id(user_id)

    def find_by_email(self, email: str):
        return self.repository.find_by_email(email)

    def update_user(self, user_id: int, email: Optional[str], password: Optional[str]):
        # Create the user object
        if password is not None:
            password = pbkdf2_sha256.encrypt(password)

        self.repository.update(user_id, email, password)
        return self.get_user(user_id)

    def delete_user(self, user_id: int):
        return self.repository.delete(user_id)
