# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.insurance_type import InsuranceType  # noqa: F401,E501
from swagger_server import util


class InsurancePolicy(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, user_id: int=None, type: InsuranceType=None, start_date: date=None, end_date: date=None):  # noqa: E501
        """InsurancePolicy - a model defined in Swagger

        :param id: The id of this InsurancePolicy.  # noqa: E501
        :type id: int
        :param user_id: The user_id of this InsurancePolicy.  # noqa: E501
        :type user_id: int
        :param type: The type of this InsurancePolicy.  # noqa: E501
        :type type: InsuranceType
        :param start_date: The start_date of this InsurancePolicy.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this InsurancePolicy.  # noqa: E501
        :type end_date: date
        """
        self.swagger_types = {
            'id': int,
            'user_id': int,
            'type': InsuranceType,
            'start_date': date,
            'end_date': date
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'user_id',
            'type': 'type',
            'start_date': 'start_date',
            'end_date': 'end_date'
        }
        self._id = id
        self._user_id = user_id
        self._type = type
        self._start_date = start_date
        self._end_date = end_date

    @classmethod
    def from_dict(cls, dikt) -> 'InsurancePolicy':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InsurancePolicy of this InsurancePolicy.  # noqa: E501
        :rtype: InsurancePolicy
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this InsurancePolicy.


        :return: The id of this InsurancePolicy.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this InsurancePolicy.


        :param id: The id of this InsurancePolicy.
        :type id: int
        """

        self._id = id

    @property
    def user_id(self) -> int:
        """Gets the user_id of this InsurancePolicy.


        :return: The user_id of this InsurancePolicy.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this InsurancePolicy.


        :param user_id: The user_id of this InsurancePolicy.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def type(self) -> InsuranceType:
        """Gets the type of this InsurancePolicy.


        :return: The type of this InsurancePolicy.
        :rtype: InsuranceType
        """
        return self._type

    @type.setter
    def type(self, type: InsuranceType):
        """Sets the type of this InsurancePolicy.


        :param type: The type of this InsurancePolicy.
        :type type: InsuranceType
        """

        self._type = type

    @property
    def start_date(self) -> date:
        """Gets the start_date of this InsurancePolicy.


        :return: The start_date of this InsurancePolicy.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: date):
        """Sets the start_date of this InsurancePolicy.


        :param start_date: The start_date of this InsurancePolicy.
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def end_date(self) -> date:
        """Gets the end_date of this InsurancePolicy.


        :return: The end_date of this InsurancePolicy.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: date):
        """Sets the end_date of this InsurancePolicy.


        :param end_date: The end_date of this InsurancePolicy.
        :type end_date: date
        """

        self._end_date = end_date
