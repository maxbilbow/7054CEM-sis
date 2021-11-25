# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.address import Address  # noqa: F401,E501
from swagger_server import util


class HomeDetails(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, address: Address=None):  # noqa: E501
        """HomeDetails - a model defined in Swagger

        :param address: The address of this HomeDetails.  # noqa: E501
        :type address: Address
        """
        self.swagger_types = {
            'address': Address
        }

        self.attribute_map = {
            'address': 'address'
        }
        self._address = address

    @classmethod
    def from_dict(cls, dikt) -> 'HomeDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HomeDetails of this HomeDetails.  # noqa: E501
        :rtype: HomeDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self) -> Address:
        """Gets the address of this HomeDetails.


        :return: The address of this HomeDetails.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address: Address):
        """Sets the address of this HomeDetails.


        :param address: The address of this HomeDetails.
        :type address: Address
        """

        self._address = address