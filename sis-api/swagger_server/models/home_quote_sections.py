# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.home_details import HomeDetails  # noqa: F401,E501
from swagger_server.models.insurance_type import InsuranceType  # noqa: F401,E501
from swagger_server.models.personal_details import PersonalDetails  # noqa: F401,E501
from swagger_server.models.quote_sections import QuoteSections  # noqa: F401,E501
from swagger_server import util


class HomeQuoteSections(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, quote_id: int=None, quote_type: InsuranceType=None, personal_details: PersonalDetails=None, home_details: HomeDetails=None):  # noqa: E501
        """HomeQuoteSections - a model defined in Swagger

        :param quote_id: The quote_id of this HomeQuoteSections.  # noqa: E501
        :type quote_id: int
        :param quote_type: The quote_type of this HomeQuoteSections.  # noqa: E501
        :type quote_type: InsuranceType
        :param personal_details: The personal_details of this HomeQuoteSections.  # noqa: E501
        :type personal_details: PersonalDetails
        :param home_details: The home_details of this HomeQuoteSections.  # noqa: E501
        :type home_details: HomeDetails
        """
        self.swagger_types = {
            'quote_id': int,
            'quote_type': InsuranceType,
            'personal_details': PersonalDetails,
            'home_details': HomeDetails
        }

        self.attribute_map = {
            'quote_id': 'quote_id',
            'quote_type': 'quote_type',
            'personal_details': 'personal_details',
            'home_details': 'home_details'
        }
        self._quote_id = quote_id
        self._quote_type = quote_type
        self._personal_details = personal_details
        self._home_details = home_details

    @classmethod
    def from_dict(cls, dikt) -> 'HomeQuoteSections':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HomeQuoteSections of this HomeQuoteSections.  # noqa: E501
        :rtype: HomeQuoteSections
        """
        return util.deserialize_model(dikt, cls)

    @property
    def quote_id(self) -> int:
        """Gets the quote_id of this HomeQuoteSections.


        :return: The quote_id of this HomeQuoteSections.
        :rtype: int
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id: int):
        """Sets the quote_id of this HomeQuoteSections.


        :param quote_id: The quote_id of this HomeQuoteSections.
        :type quote_id: int
        """

        self._quote_id = quote_id

    @property
    def quote_type(self) -> InsuranceType:
        """Gets the quote_type of this HomeQuoteSections.


        :return: The quote_type of this HomeQuoteSections.
        :rtype: InsuranceType
        """
        return self._quote_type

    @quote_type.setter
    def quote_type(self, quote_type: InsuranceType):
        """Sets the quote_type of this HomeQuoteSections.


        :param quote_type: The quote_type of this HomeQuoteSections.
        :type quote_type: InsuranceType
        """

        self._quote_type = quote_type

    @property
    def personal_details(self) -> PersonalDetails:
        """Gets the personal_details of this HomeQuoteSections.


        :return: The personal_details of this HomeQuoteSections.
        :rtype: PersonalDetails
        """
        return self._personal_details

    @personal_details.setter
    def personal_details(self, personal_details: PersonalDetails):
        """Sets the personal_details of this HomeQuoteSections.


        :param personal_details: The personal_details of this HomeQuoteSections.
        :type personal_details: PersonalDetails
        """

        self._personal_details = personal_details

    @property
    def home_details(self) -> HomeDetails:
        """Gets the home_details of this HomeQuoteSections.


        :return: The home_details of this HomeQuoteSections.
        :rtype: HomeDetails
        """
        return self._home_details

    @home_details.setter
    def home_details(self, home_details: HomeDetails):
        """Sets the home_details of this HomeQuoteSections.


        :param home_details: The home_details of this HomeQuoteSections.
        :type home_details: HomeDetails
        """

        self._home_details = home_details
