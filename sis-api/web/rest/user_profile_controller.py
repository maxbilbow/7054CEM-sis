import dataclasses as dataclasses
from flask import jsonify

from core.model import custom_asdict_factory
from web.flask_app import app
from web.service.user_profile_service import UserProfileService


@app.route("/api/profile", methods=["GET"])
def get_profile(profile_service: UserProfileService):

    profile = profile_service.get_profile()
    return jsonify(dataclasses.asdict(profile, dict_factory=custom_asdict_factory))
