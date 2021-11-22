from typing import Optional

from flask import session
from injector import singleton, inject

from web_exceptions import AuthError
from service.user_service import UserService


@singleton
class AuthService:

    @inject
    def __init__(self, user: UserService):
        self.__user = user

    @staticmethod
    def get_user_id() -> int:
        user = None if 'authenticated_user' not in session else session['authenticated_user']
        if user is None:
            raise AuthError("Authenticated user not found")

        return user["id"]

    @staticmethod
    def update_session(user: dict):
        session['authenticated_user'] = user
        return user

    def register(self, email: str, password: str, login=True):
        user = self.__user.create_user(email, password)
        if user is None:
            raise AuthError("Failed to create new user")

        if login:
            return self.update_session(user)
        else:
            return user

    @staticmethod
    def logout():
        session.clear()

    def login(self, email, password) -> dict:
        user = self.__user.check_credentials(email, password)

        if user:
            return self.update_session(user)

        raise AuthError("Invalid login credentials")

    @staticmethod
    def get_authenticated_user() -> Optional[dict]:
        user = None if 'authenticated_user' not in session else session['authenticated_user']
        if user is not None:
            return user
        else:
            return None

    def is_authenticated(self):
        return self.get_authenticated_user() is not None
