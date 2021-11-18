# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.claim_history import ClaimHistory  # noqa: E501
from swagger_server.models.claim_note import ClaimNote  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClaimHistoryController(BaseTestCase):
    """ClaimHistoryController integration test stubs"""

    def test_add_note(self):
        """Test case for add_note

        Add note
        """
        body = ClaimNote()
        response = self.client.open(
            '/claim/{claim_id}/history'.format(claim_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_history(self):
        """Test case for get_history

        Get history for a claim
        """
        response = self.client.open(
            '/claim/{claim_id}/history'.format(claim_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_note(self):
        """Test case for get_note

        Get claim note
        """
        response = self.client.open(
            '/claim-history/{note_id}'.format(note_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
