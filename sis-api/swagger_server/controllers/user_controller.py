import dataclasses

import connexion

# from swagger_server.models.user import User  # noqa: E501
from core.model.user import User
from core.repository.user import UserRepository
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501


def create_user(body):  # noqa: E501
    """Create a user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        json = connexion.request.get_json()  # noqa: E501
        user = UserRepository.insert_user(json["email"], json["password_hash"])
        return {
            "user_id": user.id
        }

    return 'do some magic!'


def find_by_email(email):  # noqa: E501
    """Get a user id by email

     # noqa: E501

    :param email: The email of the user to retrieve
    :type email: str

    :rtype: str
    """
    user = UserRepository.find_by_email(email)
    return user.id


def get_user(user_id):  # noqa: E501
    """Get a user

     # noqa: E501

    :param user_id: The id of the user to retrieve
    :type user_id: int

    :rtype: User
    """
    return dataclasses.asdict(UserRepository.find_by_id(user_id))


def remove_user(user_id):  # noqa: E501
    """Remove a user

     # noqa: E501

    :param user_id: The id of the user to remove
    :type user_id: int

    :rtype: None
    """
    UserRepository.delete(user_id)
    return 'It is done.'


def update_user(user_id):  # noqa: E501
    """Update and replace a user

     # noqa: E501

    :param user_id: The id of the user to update
    :type user_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()
        data["id"] = -1
        body = User(**data)  # noqa: E501
        UserRepository.update(user_id, body)

    return 'do some magic!'
