import dataclasses
import datetime

import connexion

from core.model import to_dict
from core.model.membership import Membership
from core.repository.membership import MembershipRepository


def get_current(user_id):
    membership = MembershipRepository.find_by_user_id(user_id)
    if membership is None:
        return {}, 404
    return to_dict(membership)


def cancel_membership(user_id):  # noqa: E501
    """Cancel the current membership by setting its end_date to today

     # noqa: E501

    :param user_id: The id of the user
    :type user_id: int

    :rtype: Membership
    """
    membership = MembershipRepository.find_by_user_id(user_id)
    membership = dataclasses.replace(membership, end_date=datetime.date.today())
    if membership.start_date == membership.end_date:
        MembershipRepository.delete(membership)
        return None
    else:
        membership = MembershipRepository.update_current(user_id, membership)
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
        membership = Membership(**dict)  # noqa: E501
        return MembershipRepository.create(user_id, membership.type, membership.start_date, membership.end_date)
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
        membership = Membership(**dict)
        membership = MembershipRepository.update_current(user_id, membership)
        return to_dict(membership)
        # noqa: E501
    return 'do some magic!'
