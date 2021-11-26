# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.quote import Quote  # noqa: E501
from swagger_server.models.quotes import Quotes  # noqa: E501
from swagger_server.test import BaseTestCase


class TestQuotesController(BaseTestCase):
    """QuotesController integration test stubs"""

    def test_calculate_price(self):
        """Test case for calculate_price

        Calculate and store a price for a quote
        """
        body = None
        response = self.client.open(
            '/quote/{quote_id}/calculate-price'.format(quote_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_quote(self):
        """Test case for delete_quote

        Delete quote
        """
        response = self.client.open(
            '/quote/{quote_id}'.format(quote_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_for_user(self):
        """Test case for get_for_user

        Get all quotes for a user
        """
        response = self.client.open(
            '/user/{user_id}/quote'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_quote(self):
        """Test case for get_quote

        Get quote by id
        """
        response = self.client.open(
            '/quote/{quote_id}'.format(quote_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_new_quote(self):
        """Test case for new_quote

        Create a new quote
        """
        body = Quote()
        response = self.client.open(
            '/user/{user_id}/quote'.format(user_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_quote(self):
        """Test case for update_quote

        Update a quote
        """
        body = Quote()
        response = self.client.open(
            '/quote/{quote_id}'.format(quote_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
