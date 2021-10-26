import os

import connexion

from web import encoder


def create_app():
    abs_file_path = os.path.abspath(os.path.dirname(__file__))
    openapi_path = os.path.join(abs_file_path, "web", "swagger")
    app = connexion.FlaskApp(
        __name__, specification_dir=openapi_path, options={"swagger_ui": True, "serve_spec": True}
    )
    app.add_api("swagger.yaml", arguments={'title': 'Pet Store'}, strict_validation=True, pythonic_params=True)
    flask_app = app.app
    flask_app.json_encoder = encoder.JSONEncoder

    return flask_app
