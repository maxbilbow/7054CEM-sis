# AuthenticationController.py
import logging

from flask import request, render_template, jsonify, redirect, current_app as app
from flask_api import status
from injector import inject

from web.exceptions import AuthError
from web.rest.decorators import logout_required, login_required
from web.service.auth_service import AuthService


@inject
@app.route("/api/is-authenticated", methods=["GET"])
def get_auth_status(service: AuthService):
    user = service.get_authenticated_user()
    if user is not None:
        return jsonify({
            "authenticated": True
        })
    else:
        return jsonify({
            "authenticated": False
        })


@app.route("/login")
@logout_required
def get_login_page():
    return render_template("login.html")


@app.route("/register")
@logout_required
def get_register_page():
    return render_template("register.html")


@inject
@app.route("/logout")
@login_required
def logout(auth_service: AuthService):
    auth_service.logout()
    return redirect('/')


@inject
@logout_required
@app.route('/api/login', methods=['POST'])
def login(auth_service: AuthService):
    try:
        auth_service.login(
            request.form.get('email'),
            request.form.get('password')
        )
        return get_auth_status(auth_service), status.HTTP_202_ACCEPTED
    except AuthError as ae:
        logging.exception(ae)
        return jsonify({
            "error": str(ae)
        }), status.HTTP_400_BAD_REQUEST
    except Exception as e:
        logging.exception(e)
        auth_service.logout()
        return jsonify({
            "data": {
                "id": "review",
                "type": "submit",
                "attributes": {
                    "result": "fail",
                    "message": str(e)
                }
            }
        }), status.HTTP_500_INTERNAL_SERVER_ERROR


@inject
@logout_required
@app.route('/api/register', methods=['POST'])
def register(auth_service: AuthService):
    print(request.form)
    try:
        auth_service.register(
            request.form.get('email'),
            request.form.get('password')
        )
        return get_auth_status(auth_service), status.HTTP_201_CREATED
    except AuthError as ae:
        logging.exception("Authentication Error")
        return jsonify({
            "error": str(ae)
        }), status.HTTP_400_BAD_REQUEST
    except Exception as e:
        logging.exception(e)
        return jsonify({
            "error": str(e)
        }), status.HTTP_500_INTERNAL_SERVER_ERROR
