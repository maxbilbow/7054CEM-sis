# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.attachment import Attachment  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAttachmentsController(BaseTestCase):
    """AttachmentsController integration test stubs"""

    def test_get_attachment(self):
        """Test case for get_attachment

        Download attachment
        """
        response = self.client.open(
            '/attachments/{attachment_id}'.format(attachment_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
