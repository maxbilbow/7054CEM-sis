from functools import wraps

from flask import session, redirect
from flask_api import status

# Decorators
from web_exceptions import AuthError, BadRequest


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'authenticated_user' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/login'), status.HTTP_307_TEMPORARY_REDIRECT

    return wrap


def login_required_post(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'authenticated_user' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/login'), status.HTTP_401_UNAUTHORIZED

    return wrap


# Decorators
def logout_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not 'authenticated_user' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


def handle_errors(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except AuthError as ae:
            return str(ae), status.HTTP_401_UNAUTHORIZED
        except BadRequest as be:
            return str(be), status.HTTP_400_BAD_REQUEST
        except Exception as e:
            return str(e), status.HTTP_500_INTERNAL_SERVER_ERROR

    return wrap
