import connexion
import six

from swagger_server.models.claim import Claim  # noqa: E501
from swagger_server.models.claims import Claims  # noqa: E501
from swagger_server import util


def get_for_package(package_id):  # noqa: E501
    """Get all claims for a package

     # noqa: E501

    :param package_id: The id of the package
    :type package_id: int

    :rtype: Claims
    """
    return 'do some magic!'


def get_for_user(user_id):  # noqa: E501
    """Get all claims for a user

     # noqa: E501

    :param user_id: The id of the user
    :type user_id: int

    :rtype: Claims
    """
    return 'do some magic!'


def get_one(claim_id):  # noqa: E501
    """Get all claims for a package

     # noqa: E501

    :param claim_id: The id of the claim
    :type claim_id: int

    :rtype: Claim
    """
    return 'do some magic!'


def new_claim(body, user_id, package_id):  # noqa: E501
    """Create a new claim

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param user_id: The id of the user
    :type user_id: int
    :param package_id: The id of the package to claim against
    :type package_id: int

    :rtype: Claim
    """
    if connexion.request.is_json:
        body = Claim.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
