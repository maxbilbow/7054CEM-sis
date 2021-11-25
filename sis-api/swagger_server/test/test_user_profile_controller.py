# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from core.repository.user import UserRepository
from core.service.user_service import UserService
from service.user_profile_service import UserProfileService
from swagger_server.models.user_profile import UserProfile  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserProfileController(BaseTestCase):
    """UserProfileController integration test stubs"""

    i = 0
    email: str
    pw: str
    user_id: int

    def setUp(self) -> None:
        self.i = self.i + 1
        self.email = f"email{self.i}"
        self.pw = "password"
        self.user_id = UserService().register(email=self.email, password=self.pw).id

    def tearDown(self) -> None:
        UserService().delete_user(self.user_id)

    def test_create_profile(self):
        """Test case for create_profile

        Create a user profile
        """
        body = UserProfile()
        response = self.client.open(
            '/api/v1/user/{user_id}/profile'.format(user_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_profile(self):
        """Test case for get_profile

        Get a user profile
        """
        response = self.client.open(
            '/api/v1/user/{user_id}/profile'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_profile(self):
        """Test case for remove_profile

        Remove a user profile
        """
        response = self.client.open(
            '/api/v1/user/{user_id}/profile'.format(user_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_profile(self):
        """Test case for update_profile

        Update and replace a user profile
        """
        body = UserProfile()
        response = self.client.open(
            '/api/v1/user/{user_id}/profile'.format(user_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
