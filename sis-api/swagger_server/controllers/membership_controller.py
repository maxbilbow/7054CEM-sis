import connexion
import six

from swagger_server.models.benefits import Benefits  # noqa: E501
from swagger_server.models.membership import Membership  # noqa: E501
from swagger_server import util


def cancel_membership(user_id):  # noqa: E501
    """Cancel the current membership by setting its end_date to today

     # noqa: E501

    :param user_id: The id of the user
    :type user_id: int

    :rtype: Membership
    """
    return 'do some magic!'


def create_membership(body, user_id):  # noqa: E501
    """Create new membership

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param user_id: The id of the user
    :type user_id: int

    :rtype: Membership
    """
    if connexion.request.is_json:
        body = Membership.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_benefits(user_id):  # noqa: E501
    """Get all benefits available for a user

     # noqa: E501

    :param user_id: The id of the user
    :type user_id: int

    :rtype: Benefits
    """
    return 'do some magic!'


def update_membership(body, user_id):  # noqa: E501
    """Update a membership

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param user_id: The id of the user
    :type user_id: int

    :rtype: Membership
    """
    if connexion.request.is_json:
        body = Membership.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
