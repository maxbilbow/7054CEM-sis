import connexion
# from swagger_server.models.user import User  # noqa: E501
from flask_api import status

from core.model import to_dict
from core.model.user import User
from core.service.user_service import UserService
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
        try:
            user = UserService().register(json["email"], json["password"])
            return {
                "user_id": user.id
            }
        except BadRequest as br:
            return str(br), status.HTTP_400_BAD_REQUEST

    return {}, status.HTTP_400_BAD_REQUEST


def find_by_email(email):  # noqa: E501
    """Get a user id by email

     # noqa: E501

    :param email: The email of the user to retrieve
    :type email: str

    :rtype: str
    """
    user = UserService().find_by_email(email)
    if user is None:
        return "User not found with email address", 404
    return user.id


def check_credentials(body):  # noqa: E501
    """Get a user id by email

     # noqa: E501

    :param email: The email of the user to retrieve
    :type email: str

    :rtype: str
    """
    if not connexion.request.is_json:
        return {}, status.HTTP_400_BAD_REQUEST

    json = connexion.request.get_json()  # noqa: E501
    valid = UserService().check_credentials(json["email"], json["password"])
    if valid:
        user = UserService().find_by_email(json["email"])
        return {
            "user_id": user.id,
            "authenticated": True
        }
    else:
        return {"authenticated": False}, status.HTTP_401_UNAUTHORIZED


def get_user(user_id):  # noqa: E501
    """Get a user

     # noqa: E501

    :param user_id: The id of the user to retrieve
    :type user_id: int

    :rtype: User
    """

    return to_dict(UserService().get_user(user_id))


def remove_user(user_id):  # noqa: E501
    """Remove a user

     # noqa: E501

    :param user_id: The id of the user to remove
    :type user_id: int

    :rtype: None
    """
    UserService().delete_user(user_id)
    return {}, status.HTTP_204_NO_CONTENT


def update_user(user_id):  # noqa: E501
    """Update and replace a user

     # noqa: E501

    :param user_id: The id of the user to update
    :type user_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        data = connexion.request.get_json()
        user = UserService().update_user(user_id, data["email"], data["password"])
        return to_dict(user), status.HTTP_202_ACCEPTED

    return {}, status.HTTP_400_BAD_REQUEST
