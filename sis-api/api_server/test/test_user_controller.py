# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from api_server.models.inline_response200 import InlineResponse200  # noqa: E501
from api_server.models.user import User  # noqa: E501
from api_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        Create a user
        """
        body = User()
        response = self.client.open(
            '/user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_by_email(self):
        """Test case for find_by_email

        Get a user id by email
        """
        response = self.client.open(
            '/user-id/{email}'.format(email='email_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        Get a user
        """
        response = self.client.open(
            '/user/{user_id}'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_user(self):
        """Test case for remove_user

        Remove a user
        """
        response = self.client.open(
            '/user/{user_id}'.format(user_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        Update and replace a user
        """
        body = User()
        response = self.client.open(
            '/user',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
