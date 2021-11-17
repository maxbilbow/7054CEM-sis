from core.model.user import User
from flask import session
from injector import singleton, inject
from passlib.hash import pbkdf2_sha256


class UserService:

    def register(self, email: str, password: str, login=True) -> User:
        # Create the user object
        user = User(
            email=email,
            # Encrypt the password
            password_hash=pbkdf2_sha256.encrypt(password)
        )

        # Check for existing email address
        if self.repository.find_user_by_email(email):
            raise AuthError("Email address already in use")

        if self.repository.create_user(user) is None:
            raise AuthError("Failed to create new user")

        if login:
            return self.update_session(user.to_dict())
        else:
            return user.to_dict()