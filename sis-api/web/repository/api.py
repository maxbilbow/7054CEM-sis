from injector import singleton

import config
import requests

URL = config.get("api.path")


def _json(response):
    if response.status_code == 404:
        return None
    if response.status_code < 200 or response.status_code >= 300:
        raise Exception(response.status_code, response.text)
    return response.json()


@singleton
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
