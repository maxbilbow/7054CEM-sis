import connexion
import six

from swagger_server.models.claim_history import ClaimHistory  # noqa: E501
from swagger_server.models.claim_note import ClaimNote  # noqa: E501
from swagger_server import util


def add_note(body, claim_id):  # noqa: E501
    """Add note

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param claim_id: The id of the claim
    :type claim_id: int

    :rtype: ClaimNote
    """
    if connexion.request.is_json:
        body = ClaimNote.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_history(claim_id):  # noqa: E501
    """Get history for a claim

     # noqa: E501

    :param claim_id: The id of the claim
    :type claim_id: int

    :rtype: ClaimHistory
    """
    return 'do some magic!'


def get_note(note_id):  # noqa: E501
    """Get claim note

     # noqa: E501

    :param note_id: The id of the history item
    :type note_id: int

    :rtype: ClaimNote
    """
    return 'do some magic!'
