# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from api_server.models.claim import Claim  # noqa: E501
from api_server.models.claims import Claims  # noqa: E501
from api_server.test import BaseTestCase


class TestClaimsController(BaseTestCase):
    """ClaimsController integration test stubs"""

    def test_get_for_package(self):
        """Test case for get_for_package

        Get all claims for a package
        """
        response = self.client.open(
            '/package/{package_id}/claim'.format(package_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_for_user(self):
        """Test case for get_for_user

        Get all claims for a user
        """
        response = self.client.open(
            '/user/{user_id}/claim'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_one(self):
        """Test case for get_one

        Get all claims for a package
        """
        response = self.client.open(
            '/claim/{claim_id}'.format(claim_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_new_claim(self):
        """Test case for new_claim

        Create a new claim
        """
        body = Claim()
        response = self.client.open(
            '/user/{user_id}/insurance_package/{package_id}'.format(user_id=56, package_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
