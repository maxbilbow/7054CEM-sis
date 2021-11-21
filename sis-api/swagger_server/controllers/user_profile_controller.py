import connexion
from flask_api import status

from core import model
from core.model.profile import Profile
from core.repository.user_profile import UserProfileRepository
from core.service.profile_service import ProfileService


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
        profile = ProfileService().insert_profile(json)
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
    if profile is None:
        return "Profile not found", status.HTTP_204_NO_CONTENT
    return model.to_dict(profile)


def remove_profile(user_id):  # noqa: E501
    """Remove a user profile

     # noqa: E501

    :param user_id: The id of the user to remove
    :type user_id: int

    :rtype: None
    """
    ProfileService().delete(user_id)
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
    if not connexion.request.is_json:
        return {}, status.HTTP_400_BAD_REQUEST
    else:
        body["user_id"] = user_id
        profile = Profile.from_dict(body)
        UserProfileRepository.update(profile)
        return model.to_dict(profile), status.HTTP_202_ACCEPTED
