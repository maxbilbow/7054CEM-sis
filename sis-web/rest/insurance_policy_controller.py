from flask import current_app as app

from rest.decorators import handle_errors
from service.insurance_policy_service import InsurancePolicyService


@app.route("/api/my-policies", methods=["GET"])
@handle_errors
def get_policies(insurance_policy_service: InsurancePolicyService):
    pass


@app.route("/api/my-policies", methods=["POST"])
@handle_errors
def update_profile(profile_service: InsurancePolicyService):
    pass
