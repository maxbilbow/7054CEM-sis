# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.benefits import Benefits  # noqa: E501
from swagger_server.models.membership import Membership  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMembershipController(BaseTestCase):
    """MembershipController integration test stubs"""

    def test_cancel_membership(self):
        """Test case for cancel_membership

        Cancel the current membership by setting its end_date to today
        """
        response = self.client.open(
            '/user/{user_id}/membership'.format(user_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_membership(self):
        """Test case for create_membership

        Create new membership
        """
        body = Membership()
        response = self.client.open(
            '/user/{user_id}/membership'.format(user_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_benefits(self):
        """Test case for get_benefits

        Get all benefits available for a user
        """
        response = self.client.open(
            '/user/{user_id}/benefits'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_current(self):
        """Test case for get_current

        Get current active membership for user
        """
        response = self.client.open(
            '/user/{user_id}/membership'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_membership(self):
        """Test case for update_membership

        Update a membership
        """
        body = Membership()
        response = self.client.open(
            '/user/{user_id}/membership'.format(user_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
