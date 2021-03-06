# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.driver_details import DriverDetails  # noqa: F401,E501
from swagger_server.models.insurance_type import InsuranceType  # noqa: F401,E501
from swagger_server.models.quote_sections import QuoteSections  # noqa: F401,E501
from swagger_server.models.vehicle_details import VehicleDetails  # noqa: F401,E501
from swagger_server.models.vehicle_usage import VehicleUsage  # noqa: F401,E501
from swagger_server import util


class VehicleQuoteSections(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, quote_id: int=None, quote_type: InsuranceType=None, driver_details: DriverDetails=None, vehicle_details: VehicleDetails=None, vehicle_usage: VehicleUsage=None, additional_drivers: List[DriverDetails]=None):  # noqa: E501
        """VehicleQuoteSections - a model defined in Swagger

        :param quote_id: The quote_id of this VehicleQuoteSections.  # noqa: E501
        :type quote_id: int
        :param quote_type: The quote_type of this VehicleQuoteSections.  # noqa: E501
        :type quote_type: InsuranceType
        :param driver_details: The driver_details of this VehicleQuoteSections.  # noqa: E501
        :type driver_details: DriverDetails
        :param vehicle_details: The vehicle_details of this VehicleQuoteSections.  # noqa: E501
        :type vehicle_details: VehicleDetails
        :param vehicle_usage: The vehicle_usage of this VehicleQuoteSections.  # noqa: E501
        :type vehicle_usage: VehicleUsage
        :param additional_drivers: The additional_drivers of this VehicleQuoteSections.  # noqa: E501
        :type additional_drivers: List[DriverDetails]
        """
        self.swagger_types = {
            'quote_id': int,
            'quote_type': InsuranceType,
            'driver_details': DriverDetails,
            'vehicle_details': VehicleDetails,
            'vehicle_usage': VehicleUsage,
            'additional_drivers': List[DriverDetails]
        }

        self.attribute_map = {
            'quote_id': 'quote_id',
            'quote_type': 'quote_type',
            'driver_details': 'driver_details',
            'vehicle_details': 'vehicle_details',
            'vehicle_usage': 'vehicle_usage',
            'additional_drivers': 'additional_drivers'
        }
        self._quote_id = quote_id
        self._quote_type = quote_type
        self._driver_details = driver_details
        self._vehicle_details = vehicle_details
        self._vehicle_usage = vehicle_usage
        self._additional_drivers = additional_drivers

    @classmethod
    def from_dict(cls, dikt) -> 'VehicleQuoteSections':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VehicleQuoteSections of this VehicleQuoteSections.  # noqa: E501
        :rtype: VehicleQuoteSections
        """
        return util.deserialize_model(dikt, cls)

    @property
    def quote_id(self) -> int:
        """Gets the quote_id of this VehicleQuoteSections.


        :return: The quote_id of this VehicleQuoteSections.
        :rtype: int
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id: int):
        """Sets the quote_id of this VehicleQuoteSections.


        :param quote_id: The quote_id of this VehicleQuoteSections.
        :type quote_id: int
        """

        self._quote_id = quote_id

    @property
    def quote_type(self) -> InsuranceType:
        """Gets the quote_type of this VehicleQuoteSections.


        :return: The quote_type of this VehicleQuoteSections.
        :rtype: InsuranceType
        """
        return self._quote_type

    @quote_type.setter
    def quote_type(self, quote_type: InsuranceType):
        """Sets the quote_type of this VehicleQuoteSections.


        :param quote_type: The quote_type of this VehicleQuoteSections.
        :type quote_type: InsuranceType
        """

        self._quote_type = quote_type

    @property
    def driver_details(self) -> DriverDetails:
        """Gets the driver_details of this VehicleQuoteSections.


        :return: The driver_details of this VehicleQuoteSections.
        :rtype: DriverDetails
        """
        return self._driver_details

    @driver_details.setter
    def driver_details(self, driver_details: DriverDetails):
        """Sets the driver_details of this VehicleQuoteSections.


        :param driver_details: The driver_details of this VehicleQuoteSections.
        :type driver_details: DriverDetails
        """

        self._driver_details = driver_details

    @property
    def vehicle_details(self) -> VehicleDetails:
        """Gets the vehicle_details of this VehicleQuoteSections.


        :return: The vehicle_details of this VehicleQuoteSections.
        :rtype: VehicleDetails
        """
        return self._vehicle_details

    @vehicle_details.setter
    def vehicle_details(self, vehicle_details: VehicleDetails):
        """Sets the vehicle_details of this VehicleQuoteSections.


        :param vehicle_details: The vehicle_details of this VehicleQuoteSections.
        :type vehicle_details: VehicleDetails
        """

        self._vehicle_details = vehicle_details

    @property
    def vehicle_usage(self) -> VehicleUsage:
        """Gets the vehicle_usage of this VehicleQuoteSections.


        :return: The vehicle_usage of this VehicleQuoteSections.
        :rtype: VehicleUsage
        """
        return self._vehicle_usage

    @vehicle_usage.setter
    def vehicle_usage(self, vehicle_usage: VehicleUsage):
        """Sets the vehicle_usage of this VehicleQuoteSections.


        :param vehicle_usage: The vehicle_usage of this VehicleQuoteSections.
        :type vehicle_usage: VehicleUsage
        """

        self._vehicle_usage = vehicle_usage

    @property
    def additional_drivers(self) -> List[DriverDetails]:
        """Gets the additional_drivers of this VehicleQuoteSections.


        :return: The additional_drivers of this VehicleQuoteSections.
        :rtype: List[DriverDetails]
        """
        return self._additional_drivers

    @additional_drivers.setter
    def additional_drivers(self, additional_drivers: List[DriverDetails]):
        """Sets the additional_drivers of this VehicleQuoteSections.


        :param additional_drivers: The additional_drivers of this VehicleQuoteSections.
        :type additional_drivers: List[DriverDetails]
        """

        self._additional_drivers = additional_drivers
