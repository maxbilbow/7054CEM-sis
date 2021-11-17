import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def create_user(body):  # noqa: E501
    """Create a user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_by_email(email):  # noqa: E501
    """Get a user id by email

     # noqa: E501

    :param email: The email of the user to retrieve
    :type email: str

    :rtype: str
    """
    return 'do some magic!'


def get_user(user_id):  # noqa: E501
    """Get a user

     # noqa: E501

    :param user_id: The id of the user to retrieve
    :type user_id: int

    :rtype: User
    """
    return 'do some magic!'


def remove_user(user_id):  # noqa: E501
    """Remove a user

     # noqa: E501

    :param user_id: The id of the user to remove
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def update_user(body):  # noqa: E501
    """Update and replace a user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
