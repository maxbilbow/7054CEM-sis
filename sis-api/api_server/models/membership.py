# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.membership_type import MembershipType  # noqa: F401,E501
from swagger_server import util


class Membership(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, user_id: int=None, start_date: date=None, end_date: date=None, type: MembershipType=None):  # noqa: E501
        """Membership - a model defined in Swagger

        :param id: The id of this Membership.  # noqa: E501
        :type id: int
        :param user_id: The user_id of this Membership.  # noqa: E501
        :type user_id: int
        :param start_date: The start_date of this Membership.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this Membership.  # noqa: E501
        :type end_date: date
        :param type: The type of this Membership.  # noqa: E501
        :type type: MembershipType
        """
        self.swagger_types = {
            'id': int,
            'user_id': int,
            'start_date': date,
            'end_date': date,
            'type': MembershipType
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'user_id',
            'start_date': 'start_date',
            'end_date': 'end_date',
            'type': 'type'
        }
        self._id = id
        self._user_id = user_id
        self._start_date = start_date
        self._end_date = end_date
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Membership':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Membership of this Membership.  # noqa: E501
        :rtype: Membership
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Membership.


        :return: The id of this Membership.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Membership.


        :param id: The id of this Membership.
        :type id: int
        """

        self._id = id

    @property
    def user_id(self) -> int:
        """Gets the user_id of this Membership.


        :return: The user_id of this Membership.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this Membership.


        :param user_id: The user_id of this Membership.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def start_date(self) -> date:
        """Gets the start_date of this Membership.


        :return: The start_date of this Membership.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: date):
        """Sets the start_date of this Membership.


        :param start_date: The start_date of this Membership.
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def end_date(self) -> date:
        """Gets the end_date of this Membership.


        :return: The end_date of this Membership.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: date):
        """Sets the end_date of this Membership.


        :param end_date: The end_date of this Membership.
        :type end_date: date
        """

        self._end_date = end_date

    @property
    def type(self) -> MembershipType:
        """Gets the type of this Membership.


        :return: The type of this Membership.
        :rtype: MembershipType
        """
        return self._type

    @type.setter
    def type(self, type: MembershipType):
        """Sets the type of this Membership.


        :param type: The type of this Membership.
        :type type: MembershipType
        """

        self._type = type
