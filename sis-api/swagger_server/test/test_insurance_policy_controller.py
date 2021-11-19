# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.insurance_policies import InsurancePolicies  # noqa: E501
from swagger_server.models.insurance_policy import InsurancePolicy  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInsurancePolicyController(BaseTestCase):
    """InsurancePolicyController integration test stubs"""

    def test_create_package(self):
        """Test case for create_package

        Create new package
        """
        body = InsurancePolicy()
        response = self.client.open(
            '/user/{user_id}/insurance_package'.format(user_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_package(self):
        """Test case for delete_package

        Delete application
        """
        response = self.client.open(
            '/user/{user_id}/insurance_package/{package_id}'.format(user_id=56, package_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_active(self):
        """Test case for get_active

        Get active packages
        """
        response = self.client.open(
            '/user/{user_id}/insurance_package'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all(self):
        """Test case for get_all

        Gets all packages for a user
        """
        response = self.client.open(
            '/user/{user_id}/insurance_package/{package_id}'.format(user_id=56, package_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update(self):
        """Test case for update

        Update package
        """
        body = InsurancePolicy()
        response = self.client.open(
            '/user/{user_id}/insurance_package'.format(user_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
