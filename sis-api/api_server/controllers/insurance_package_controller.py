import connexion
import six

from api_server.models.insurance_package import InsurancePackage  # noqa: E501
from api_server.models.insurance_packages import InsurancePackages  # noqa: E501
from api_server import util


def create_package(body, user_id):  # noqa: E501
    """Create new package

     # noqa: E501

    :param body: Package to create
    :type body: dict | bytes
    :param user_id: The id of the user
    :type user_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = InsurancePackage.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_package(user_id, package_id):  # noqa: E501
    """Delete application

     # noqa: E501

    :param user_id: The id of the user to remove
    :type user_id: int
    :param package_id: The id of the insurance package
    :type package_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_active(user_id):  # noqa: E501
    """Get active packages

     # noqa: E501

    :param user_id: The id of the user
    :type user_id: int

    :rtype: InsurancePackages
    """
    return 'do some magic!'


def get_all(user_id, package_id):  # noqa: E501
    """Gets all packages for a user

     # noqa: E501

    :param user_id: The id of the user
    :type user_id: int
    :param package_id: The id of the insurance package
    :type package_id: int

    :rtype: InsurancePackage
    """
    return 'do some magic!'


def update(body, user_id):  # noqa: E501
    """Update package

     # noqa: E501

    :param body: Package to create
    :type body: dict | bytes
    :param user_id: The id of the user
    :type user_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = InsurancePackage.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
