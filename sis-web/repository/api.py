import requests
from flask_api import status

import config
from web_exceptions import BadRequest

URL = config.get("api.path")


def _json(response):
    if response.status_code == status.HTTP_204_NO_CONTENT:
        return None
    if 200 <= response.status_code < 300:
        return response.json()

    msg = f"{response.status_code}: {response.text}"
    if 400 <= response.status_code < 500:
        raise BadRequest(msg)
    else:
        raise Exception(msg)


class Api:
    @staticmethod
    def get(path: str, params=None, **kwargs):
        return _json(requests.get(f"{URL}{path}", params, **kwargs))

    @staticmethod
    def post(path: str, data=None, json=None, **kwargs):
        return _json(requests.post(f"{URL}{path}", data, json, **kwargs))

    @staticmethod
    def put(path: str, data=None, **kwargs):
        return _json(requests.put(f"{URL}{path}", data, **kwargs))

    @staticmethod
    def delete(path: str, **kwargs):
        return _json(requests.delete(f"{URL}{path}", **kwargs))
