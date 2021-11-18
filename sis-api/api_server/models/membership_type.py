# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api_server.models.base_model_ import Model
from api_server import util


class MembershipType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    SMART = "Smart"
    SILVER = "Silver"
    GOLD = "Gold"
    def __init__(self):  # noqa: E501
        """MembershipType - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'MembershipType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MembershipType of this MembershipType.  # noqa: E501
        :rtype: MembershipType
        """
        return util.deserialize_model(dikt, cls)
