# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class VehicleDetails(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, section_complete: bool=None, quote_id: int=None, alarm_fitter: bool=None, immobilizer_fitted: bool=None, tracking_device_fitted: bool=None, is_import: bool=None, off_side_drive: bool=None, number_of_seats: float=None, current_value: float=None, is_modified: bool=None):  # noqa: E501
        """VehicleDetails - a model defined in Swagger

        :param section_complete: The section_complete of this VehicleDetails.  # noqa: E501
        :type section_complete: bool
        :param quote_id: The quote_id of this VehicleDetails.  # noqa: E501
        :type quote_id: int
        :param alarm_fitter: The alarm_fitter of this VehicleDetails.  # noqa: E501
        :type alarm_fitter: bool
        :param immobilizer_fitted: The immobilizer_fitted of this VehicleDetails.  # noqa: E501
        :type immobilizer_fitted: bool
        :param tracking_device_fitted: The tracking_device_fitted of this VehicleDetails.  # noqa: E501
        :type tracking_device_fitted: bool
        :param is_import: The is_import of this VehicleDetails.  # noqa: E501
        :type is_import: bool
        :param off_side_drive: The off_side_drive of this VehicleDetails.  # noqa: E501
        :type off_side_drive: bool
        :param number_of_seats: The number_of_seats of this VehicleDetails.  # noqa: E501
        :type number_of_seats: float
        :param current_value: The current_value of this VehicleDetails.  # noqa: E501
        :type current_value: float
        :param is_modified: The is_modified of this VehicleDetails.  # noqa: E501
        :type is_modified: bool
        """
        self.swagger_types = {
            'section_complete': bool,
            'quote_id': int,
            'alarm_fitter': bool,
            'immobilizer_fitted': bool,
            'tracking_device_fitted': bool,
            'is_import': bool,
            'off_side_drive': bool,
            'number_of_seats': float,
            'current_value': float,
            'is_modified': bool
        }

        self.attribute_map = {
            'section_complete': 'section_complete',
            'quote_id': 'quote_id',
            'alarm_fitter': 'alarm_fitter',
            'immobilizer_fitted': 'immobilizer_fitted',
            'tracking_device_fitted': 'tracking_device_fitted',
            'is_import': 'is_import',
            'off_side_drive': 'off_side_drive',
            'number_of_seats': 'number_of_seats',
            'current_value': 'current_value',
            'is_modified': 'is_modified'
        }
        self._section_complete = section_complete
        self._quote_id = quote_id
        self._alarm_fitter = alarm_fitter
        self._immobilizer_fitted = immobilizer_fitted
        self._tracking_device_fitted = tracking_device_fitted
        self._is_import = is_import
        self._off_side_drive = off_side_drive
        self._number_of_seats = number_of_seats
        self._current_value = current_value
        self._is_modified = is_modified

    @classmethod
    def from_dict(cls, dikt) -> 'VehicleDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VehicleDetails of this VehicleDetails.  # noqa: E501
        :rtype: VehicleDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def section_complete(self) -> bool:
        """Gets the section_complete of this VehicleDetails.


        :return: The section_complete of this VehicleDetails.
        :rtype: bool
        """
        return self._section_complete

    @section_complete.setter
    def section_complete(self, section_complete: bool):
        """Sets the section_complete of this VehicleDetails.


        :param section_complete: The section_complete of this VehicleDetails.
        :type section_complete: bool
        """

        self._section_complete = section_complete

    @property
    def quote_id(self) -> int:
        """Gets the quote_id of this VehicleDetails.


        :return: The quote_id of this VehicleDetails.
        :rtype: int
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id: int):
        """Sets the quote_id of this VehicleDetails.


        :param quote_id: The quote_id of this VehicleDetails.
        :type quote_id: int
        """

        self._quote_id = quote_id

    @property
    def alarm_fitter(self) -> bool:
        """Gets the alarm_fitter of this VehicleDetails.


        :return: The alarm_fitter of this VehicleDetails.
        :rtype: bool
        """
        return self._alarm_fitter

    @alarm_fitter.setter
    def alarm_fitter(self, alarm_fitter: bool):
        """Sets the alarm_fitter of this VehicleDetails.


        :param alarm_fitter: The alarm_fitter of this VehicleDetails.
        :type alarm_fitter: bool
        """

        self._alarm_fitter = alarm_fitter

    @property
    def immobilizer_fitted(self) -> bool:
        """Gets the immobilizer_fitted of this VehicleDetails.


        :return: The immobilizer_fitted of this VehicleDetails.
        :rtype: bool
        """
        return self._immobilizer_fitted

    @immobilizer_fitted.setter
    def immobilizer_fitted(self, immobilizer_fitted: bool):
        """Sets the immobilizer_fitted of this VehicleDetails.


        :param immobilizer_fitted: The immobilizer_fitted of this VehicleDetails.
        :type immobilizer_fitted: bool
        """

        self._immobilizer_fitted = immobilizer_fitted

    @property
    def tracking_device_fitted(self) -> bool:
        """Gets the tracking_device_fitted of this VehicleDetails.


        :return: The tracking_device_fitted of this VehicleDetails.
        :rtype: bool
        """
        return self._tracking_device_fitted

    @tracking_device_fitted.setter
    def tracking_device_fitted(self, tracking_device_fitted: bool):
        """Sets the tracking_device_fitted of this VehicleDetails.


        :param tracking_device_fitted: The tracking_device_fitted of this VehicleDetails.
        :type tracking_device_fitted: bool
        """

        self._tracking_device_fitted = tracking_device_fitted

    @property
    def is_import(self) -> bool:
        """Gets the is_import of this VehicleDetails.


        :return: The is_import of this VehicleDetails.
        :rtype: bool
        """
        return self._is_import

    @is_import.setter
    def is_import(self, is_import: bool):
        """Sets the is_import of this VehicleDetails.


        :param is_import: The is_import of this VehicleDetails.
        :type is_import: bool
        """

        self._is_import = is_import

    @property
    def off_side_drive(self) -> bool:
        """Gets the off_side_drive of this VehicleDetails.


        :return: The off_side_drive of this VehicleDetails.
        :rtype: bool
        """
        return self._off_side_drive

    @off_side_drive.setter
    def off_side_drive(self, off_side_drive: bool):
        """Sets the off_side_drive of this VehicleDetails.


        :param off_side_drive: The off_side_drive of this VehicleDetails.
        :type off_side_drive: bool
        """

        self._off_side_drive = off_side_drive

    @property
    def number_of_seats(self) -> float:
        """Gets the number_of_seats of this VehicleDetails.


        :return: The number_of_seats of this VehicleDetails.
        :rtype: float
        """
        return self._number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, number_of_seats: float):
        """Sets the number_of_seats of this VehicleDetails.


        :param number_of_seats: The number_of_seats of this VehicleDetails.
        :type number_of_seats: float
        """

        self._number_of_seats = number_of_seats

    @property
    def current_value(self) -> float:
        """Gets the current_value of this VehicleDetails.


        :return: The current_value of this VehicleDetails.
        :rtype: float
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value: float):
        """Sets the current_value of this VehicleDetails.


        :param current_value: The current_value of this VehicleDetails.
        :type current_value: float
        """

        self._current_value = current_value

    @property
    def is_modified(self) -> bool:
        """Gets the is_modified of this VehicleDetails.


        :return: The is_modified of this VehicleDetails.
        :rtype: bool
        """
        return self._is_modified

    @is_modified.setter
    def is_modified(self, is_modified: bool):
        """Sets the is_modified of this VehicleDetails.


        :param is_modified: The is_modified of this VehicleDetails.
        :type is_modified: bool
        """

        self._is_modified = is_modified
