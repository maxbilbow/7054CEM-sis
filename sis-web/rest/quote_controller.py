from typing import Optional

from flask import jsonify, request, current_app as app
from flask_api import status

from web_exceptions import BadRequest
from service.quote_service import QuoteService


@app.route("/api/quote", methods=["GET"], defaults={"quote_id": None})
@app.route("/api/quote/<quote_id>", methods=["GET"])
def get_quotes(quote_id: Optional[int], quote_service: QuoteService):
    if quote_id is not None:
        return _get_quote(quote_id, quote_service)
    quotes = quote_service.get_all()
    return jsonify(quotes), status.HTTP_200_OK


def _get_quote(quote_id: int, quote_service: QuoteService):
    try:
        quote = quote_service.get(quote_id)
        if quote is None:
            return {}, status.HTTP_404_NOT_FOUND
        return jsonify(quote), status.HTTP_200_OK
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/quote", methods=["POST"])
def new_quote(quote_service: QuoteService):
    try:
        response = quote_service.new_quote(request.json["type"])
        return jsonify(response), status.HTTP_201_CREATED
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/quote", methods=["PUT"])
def update_quote(quote_service: QuoteService):
    try:
        quote = quote_service.update_quote(request.json)
        return jsonify(quote), status.HTTP_202_ACCEPTED
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/quote/<quote_id>", methods=["DELETE"])
def delete_quote(quote_id: int, quote_service: QuoteService):
    try:
        result = quote_service.delete_quote(quote_id)
        return jsonify(result), status.HTTP_204_NO_CONTENT
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST
