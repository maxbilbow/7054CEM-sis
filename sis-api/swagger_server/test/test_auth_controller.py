# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_app_get_secret(self):
        """Test case for app_get_secret

        Return secret string
        """
        response = self.client.open(
            '/secret',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
