from typing import Optional

from flask import session
from injector import singleton, inject
from passlib.hash import pbkdf2_sha256

from core.model.user import User
from web.repository.user_repository import UserRepository
from web.exceptions import AuthError


@singleton
class AuthService:

    @inject
    def __init__(self, repository: UserRepository):
        self.repository = repository

    @staticmethod
    def get_user_id() -> int:
        user = None if 'authenticated_user' not in session else session['authenticated_user']
        if user is None:
            raise AuthError("Authenticated user not found")

        return user["id"]

    @staticmethod
    def update_session(user: User):
        session['authenticated_user'] = user
        return user

    def register(self, email: str, password: str, login=True):
        # Create the user object
        password_hash = pbkdf2_sha256.encrypt(password)

        # Check for existing email address
        if self.repository.find_user_by_email(email):
            raise AuthError("Email address already in use")

        user = self.repository.create_user(email, password_hash)
        if user is None:
            raise AuthError("Failed to create new user")

        if login:
            return self.update_session(user)
        else:
            return user

    @staticmethod
    def logout():
        session.clear()

    def login(self, email, password) -> User:

        user = self.repository.find_user_by_email(email)

        if user and pbkdf2_sha256.verify(password, user.password_hash):
            return self.update_session(user)

        raise AuthError("Invalid login credentials")

    @staticmethod
    def get_authenticated_user() -> Optional[User]:
        user = None if 'authenticated_user' not in session else session['authenticated_user']
        if user is not None:
            return user
        else:
            return None

    def is_authenticated(self):
        return self.get_authenticated_user() is not None
