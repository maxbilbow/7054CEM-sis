from flask import jsonify, request, current_app as app
from flask_api import status

from rest.decorators import handle_errors
from web_exceptions import BadRequest
from service.membership_service import MembershipService
from service.user_profile_service import UserProfileService


@app.route("/api/membership", methods=["GET"])
@handle_errors
def get_membership(membership_service: MembershipService):
    try:
        membership = membership_service.get()
        if membership is None:
            return {}, status.HTTP_404_NOT_FOUND
        return jsonify(membership), status.HTTP_200_OK
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/membership", methods=["POST"])
@handle_errors
def create_membership(membership_service: MembershipService):
    try:
        end_date = request.json["end_date"]
        start_date = request.json["end_date"]
        membership_type = request.json["type"] if "type" in request.json else None
        membership = membership_service.new_membership(end_date, start_date, membership_type)
        return jsonify(membership), status.HTTP_201_CREATED
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/membership", methods=["PUT"])
@handle_errors
def update_membership(membership_service: MembershipService):
    try:
        start_date = request.json["start_date"]
        end_date = request.json["end_date"]
        membership_type = request.json["type"]
        membership = membership_service.update_membership(start_date, end_date, membership_type)
        return jsonify(membership), status.HTTP_202_ACCEPTED
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/membership", methods=["DELETE"])
@handle_errors
def cancel_membership(membership_service: MembershipService):
    try:
        membership = membership_service.cancel_membership()
        if membership:
            return jsonify(membership), status.HTTP_202_ACCEPTED
        else:
            return jsonify(None), status.HTTP_204_NO_CONTENT
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/membership/get_eligible_type", methods=["GET"])
@handle_errors
def get_eligible_type(profile_service: UserProfileService):
    profile = profile_service.get()
    return get_membership_type(points=profile["points"]), status.HTTP_200_OK


def get_membership_type(points: int) -> str:
    if points >= 5:
        return "Gold"
    elif points >= 3:
        return "Silver"
    else:
        return "Smart"
