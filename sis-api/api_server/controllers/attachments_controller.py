import connexion
import six

from api_server.models.attachment import Attachment  # noqa: E501
from api_server import util


def get_attachment(attachment_id):  # noqa: E501
    """Download attachment

     # noqa: E501

    :param attachment_id: The id of the attachment
    :type attachment_id: int

    :rtype: Attachment
    """
    return 'do some magic!'