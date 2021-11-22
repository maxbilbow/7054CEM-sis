from flask import current_app as app

from service.insurance_policy_service import InsurancePolicyService


@app.route("/api/my-policies", methods=["GET"])
def get_policies(insurance_policy_service: InsurancePolicyService):
    pass


@app.route("/api/my-policies", methods=["POST"])
def update_profile(profile_service: InsurancePolicyService):
    pass
