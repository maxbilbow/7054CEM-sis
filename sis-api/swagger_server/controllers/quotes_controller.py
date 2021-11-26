import dataclasses

import connexion
import six
from flask_api import status

from core.model import to_dict
from core.service import quote_price
from core.service.quote_service import QuoteService


def delete_quote(quote_id):  # noqa: E501
    """Delete quote

     # noqa: E501

    :param quote_id: The id of the quote to remove
    :type quote_id: int

    :rtype: None
    """
    QuoteService().delete_quote(quote_id)
    return {}, status.HTTP_204_NO_CONTENT


def get_for_user(user_id):  # noqa: E501
    """Get all quotes for a user

     # noqa: E501

    :param user_id: The id of the user
    :type user_id: int

    :rtype: Quotes
    """
    quotes = QuoteService().find_for_user(user_id)
    return quotes


def get_quote(quote_id):  # noqa: E501
    """Get quote by id

     # noqa: E501

    :param quote_id: The id of the quote
    :type quote_id: int

    :rtype: Quote
    """
    quote = QuoteService().get_quote(quote_id)
    if quote is None:
        return {}, status.HTTP_204_NO_CONTENT
    return quote


def new_quote(body, user_id):  # noqa: E501
    """Create a new quote

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param user_id: The id of the user for whome to quote
    :type user_id: int

    :rtype: Quote
    """
    if connexion.request.is_json:
        insurance_type = connexion.request.get_json()["type"]  # noqa: E501
        quote = QuoteService().new_quote(user_id, insurance_type)
        return {
                   "quote_id": quote.id
               }, status.HTTP_201_CREATED
    return {}, status.HTTP_400_BAD_REQUEST


def update_quote(body, quote_id):  # noqa: E501
    """Update a quote

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param quote_id: The id of the quote to update
    :type quote_id: int

    :rtype: Quote
    """
    quote = QuoteService().update_quote(quote_id, body)
    return quote, status.HTTP_202_ACCEPTED


def calculate_price(quote_id, body=None):  # noqa: E501
    """Calculate and store a price for a quote

     # noqa: E501

    :param quote_id: The id of the quote to update
    :type quote_id: int
    :param body:
    :type body: dict | bytes

    :rtype: Quote
    """
    qs = QuoteService()
    quote = qs.get_quote(quote_id)
    if quote is None:
        return "Quote not found", status.HTTP_404_NOT_FOUND
    dataclasses.replace(quote, price=quote_price.calculate(quote))
    return qs.update_quote(quote_id, quote)
