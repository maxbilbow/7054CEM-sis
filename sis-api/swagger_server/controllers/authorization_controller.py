from typing import List

from connexion.exceptions import OAuthProblem

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""

TOKEN_DB = {
    'asdf1234567890': {
        'uid': 100
    }
}


def check_api_key(api_key, required_scopes):
    info = TOKEN_DB.get(api_key, None)

    if not info:
        raise OAuthProblem('Invalid token')

    return info


def get_secret(user):
    return f"You are {user} and the secret is 'wbevuec'"
