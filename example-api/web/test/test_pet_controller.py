# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ..models.pet import Pet  # noqa: E501
from ..models.pets import Pets  # noqa: E501
from . import BaseTestCase


class TestPetController(BaseTestCase):
    """PetController integration test stubs"""

    def test_add_pet(self):
        """Test case for add_pet

        Add a new pet to the store
        """
        body = Pet()
        response = self.client.open(
            '/pet',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_pets(self):
        """Test case for get_all_pets

        Gets all pets in the store
        """
        response = self.client.open(
            '/pet',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pet(self):
        """Test case for get_pet

        Get a pet in the store
        """
        response = self.client.open(
            '/pet/{pet_id}'.format(pet_id='pet_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_pet(self):
        """Test case for remove_pet

        Remove a pet in the store
        """
        response = self.client.open(
            '/pet/{pet_id}'.format(pet_id='pet_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_pet(self):
        """Test case for update_pet

        Update and replace a pet in the store
        """
        body = Pet()
        response = self.client.open(
            '/pet/{pet_id}'.format(pet_id='pet_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
