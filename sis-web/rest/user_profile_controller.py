from flask import jsonify, request, current_app as app
from flask_api import status

from service.user_profile_service import UserProfileService


@app.route("/api/profile", methods=["GET"])
def get_profile(profile_service: UserProfileService):
    profile = profile_service.get()
    return jsonify(profile)


@app.route("/api/profile", methods=["POST"])
def update_profile(profile_service: UserProfileService):
    profile = profile_service.insert_or_update(request.json)
    return jsonify(profile), status.HTTP_202_ACCEPTED
