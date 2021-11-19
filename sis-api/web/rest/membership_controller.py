from flask import jsonify, request
from flask_api import status

from core.model import to_dict, to_date
from core.model.membership_type import MembershipTypeFactory, MembershipType
from web.app_errors import BadRequest
from web.flask_app import app
from web.service.membership_service import MembershipService
from web.service.user_profile_service import UserProfileService


@app.route("/api/membership", methods=["GET"])
def get_membership(membership_service: MembershipService):
    try:
        membership = membership_service.get()
        if membership is None:
            return {}, status.HTTP_404_NOT_FOUND
        return jsonify(to_dict(membership)), status.HTTP_200_OK
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/membership", methods=["POST"])
def create_membership(membership_service: MembershipService):
    try:
        end_date = to_date(request.json["end_date"])
        membership = membership_service.new_membership(end_date)
        return jsonify(to_dict(membership)), status.HTTP_201_CREATED
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/membership", methods=["PUT"])
def update_membership(membership_service: MembershipService):
    try:
        end_date = to_date(request.json["end_date"])
        membership_type = MembershipType[request.json["type"]]
        membership = membership_service.update_membership(end_date, membership_type)
        return jsonify(to_dict(membership)), status.HTTP_202_ACCEPTED
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/membership", methods=["DELETE"])
def cancel_membership(membership_service: MembershipService):
    try:
        membership = membership_service.cancel_membership()
        return jsonify(to_dict(membership) if membership else {}), status.HTTP_202_ACCEPTED
    except BadRequest as be:
        return str(be), status.HTTP_400_BAD_REQUEST


@app.route("/api/membership/get_eligible_type", methods=["GET"])
def get_eligible_type(profile_service: UserProfileService):
    profile = profile_service.get_profile()
    return MembershipTypeFactory.get_membership_type(role=profile.role, points=profile.points).name, status.HTTP_200_OK
