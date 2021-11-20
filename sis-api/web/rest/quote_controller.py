from flask import jsonify, request, current_app as app
from flask_api import status

from core.model import to_dict
from web.exceptions import BadRequest
from web.service.quote_service import QuoteService


@app.route("/api/quote", methods=["GET"])
def get_saved_quotes(quote_service: QuoteService):
    quotes = quote_service.get_all()
    return jsonify(to_dict(quotes)), status.HTTP_200_OK


@app.route("/api/quote", methods=["POST"])
def new_quote(quote_service: QuoteService):
    try:
        quote_id = quote_service.new_quote(request.json["type"])
        return jsonify({"quote_id": quote_id}), status.HTTP_201_CREATED
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/quote/<quote_id>", methods=["GET"])
def get_saved_quote(quote_id: int, quote_service: QuoteService):
    try:
        quote = quote_service.get(quote_id)
        if quote is None:
            return {}, status.HTTP_404_NOT_FOUND
        return jsonify(to_dict(quote)), status.HTTP_200_OK
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/quote", methods=["PUT"])
def update_saved_quote(quote_service: QuoteService):
    try:
        quote = quote_service.update_quote(request.json)
        return jsonify(to_dict(quote)), status.HTTP_202_ACCEPTED
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/quote/<quote_id>", methods=["DELETE"])
def cancel_quote(quote_id: int, quote_service: QuoteService):
    try:
        result = quote_service.delete_quote(quote_id)
        return jsonify(result), status.HTTP_204_NO_CONTENT
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST
