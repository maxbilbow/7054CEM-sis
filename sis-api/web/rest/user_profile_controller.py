from flask import jsonify, request, current_app as app

from core.model import to_dict
from core.model.profile import Profile
from web.service.user_profile_service import UserProfileService


@app.route("/api/profile", methods=["GET"])
def get_profile(profile_service: UserProfileService):
    profile = profile_service.get_profile()
    return jsonify(to_dict(profile))


@app.route("/api/profile", methods=["POST"])
def update_profile(profile_service: UserProfileService):
    profile = Profile(**request.json)
    profile = profile_service.update_profile(profile)
    return jsonify(to_dict(profile))
