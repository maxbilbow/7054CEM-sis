from typing import Optional

from flask import jsonify, request, current_app as app
from flask_api import status

from rest.decorators import handle_errors
from service.quote_service import QuoteService


@app.route("/api/quote", methods=["GET"], defaults={"quote_id": None})
@app.route("/api/quote/<quote_id>", methods=["GET"])
@handle_errors
def get_quotes(quote_id: Optional[int], quote_service: QuoteService):
    if quote_id is not None:
        return _get_quote(quote_id, quote_service)
    quotes = quote_service.get_all()
    return jsonify(quotes), status.HTTP_200_OK


def _get_quote(quote_id: int, quote_service: QuoteService):
    quote = quote_service.get(quote_id)
    if quote is None:
        return {}, status.HTTP_404_NOT_FOUND
    return jsonify(quote), status.HTTP_200_OK


@app.route("/api/quote", methods=["POST"])
@handle_errors
def new_quote(quote_service: QuoteService):
    response = quote_service.new_quote(request.json["type"])
    return jsonify(response), status.HTTP_201_CREATED


@app.route("/api/quote", methods=["PUT"])
@handle_errors
def update_quote(quote_service: QuoteService):
    quote = quote_service.update_quote(request.json)
    return jsonify(quote), status.HTTP_202_ACCEPTED


@app.route("/api/quote/<quote_id>", methods=["DELETE"])
@handle_errors
def delete_quote(quote_id: int, quote_service: QuoteService):
    result = quote_service.delete_quote(quote_id)
    return jsonify(result), status.HTTP_204_NO_CONTENT
