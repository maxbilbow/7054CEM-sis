import dataclasses
import datetime

import connexion
from flask_api import status

from core.model import to_dict
from core.model.membership import Membership
from core.repository.membership import MembershipRepository
from core.service.membership_service import MembershipService


def get_current(user_id):
    membership = MembershipService().get_for_user(user_id)
    if membership is None:
        return {}, status.HTTP_204_NO_CONTENT
    return to_dict(membership)


def cancel_membership(user_id):  # noqa: E501
    """Cancel the current membership by setting its end_date to today

     # noqa: E501

    :param user_id: The id of the user
    :type user_id: int

    :rtype: Membership
    """
    membership = MembershipService().cancel_membership(user_id)
    if membership is None:
        return {}, status.HTTP_204_NO_CONTENT
    else:
        return to_dict(membership)


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
        dict = connexion.request.get_json()
        dict["user_id"] = user_id
        dict["id"] = -1
        membership = Membership.from_dict(dict)  # noqa: E501
        return MembershipService().new_membership(user_id, membership.end_date)
    return 'Hmm...'


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
        dict = connexion.request.get_json()
        dict["user_id"] = user_id
        dict["id"] = -1
        membership = Membership.from_dict(dict)
        membership = MembershipService().update_membership(user_id, membership.end_date, membership.type)
        if membership is None:
            return {}, status.HTTP_204_NO_CONTENT
        return to_dict(membership)
        # noqa: E501
    return 'do some magic!'
