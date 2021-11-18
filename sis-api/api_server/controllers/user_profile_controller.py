import connexion
import six

from api_server.models.user_profile import UserProfile  # noqa: E501
from api_server import util


def create_profile(body, user_id):  # noqa: E501
    """Create a user profile

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param user_id: The id of the user to update
    :type user_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_profile(user_id):  # noqa: E501
    """Get a user profile

     # noqa: E501

    :param user_id: The id of the user to retrieve
    :type user_id: int

    :rtype: UserProfile
    """
    return 'do some magic!'


def remove_profile(user_id):  # noqa: E501
    """Remove a user profile

     # noqa: E501

    :param user_id: The id of the user to remove
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def update_profile(body, user_id):  # noqa: E501
    """Update and replace a user profile

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param user_id: The id of the user to update
    :type user_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
