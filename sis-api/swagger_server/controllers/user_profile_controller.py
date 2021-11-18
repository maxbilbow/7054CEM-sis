import dataclasses

import connexion

from core import model
from core.model import custom_asdict_factory
from core.model.profile import Profile
from core.repository import mysql
from core.repository.user_profile import UserProfileRepository


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
        json = connexion.request.get_json()
        json["user_id"] = user_id
        profile = Profile(**json)
        UserProfileRepository.insert(profile)
        return profile

    return "Whoops..."


def get_profile(user_id):  # noqa: E501
    """Get a user profile

     # noqa: E501

    :param user_id: The id of the user to retrieve
    :type user_id: int

    :rtype: UserProfile
    """
    profile = UserProfileRepository.find_by_user_id(user_id)
    return model.to_dict(profile)


def remove_profile(user_id):  # noqa: E501
    """Remove a user profile

     # noqa: E501

    :param user_id: The id of the user to remove
    :type user_id: int

    :rtype: None
    """
    UserProfileRepository.delete(user_id)
    return 'User Profile deleted'


def update_profile(body, user_id):  # noqa: E501
    """Update and replace a user profile

     # noqa: E501

    :param body:
    :type body: dict | bytes
    :param user_id: The id of the user to update
    :type user_id: int

    :rtype: dict
    """
    if connexion.request.is_json:
        json = connexion.request.get_json()
        json["user_id"] = user_id
        profile = Profile(**json)
        UserProfileRepository.update(user_id, profile)
        return model.to_dict(profile)
    return 'do some magic!'
