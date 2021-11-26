from dataclasses import is_dataclass

from connexion.apps.flask_app import FlaskJSONEncoder

from core.utils.serialization import serialize
from swagger_server.models.base_model_ import Model as SwaggerModel


class JSONEncoder(FlaskJSONEncoder):
    include_nulls = True

    def default(self, o):
        if is_dataclass(o) or isinstance(o, SwaggerModel):
            return serialize(o).for_api(self.include_nulls)

        return FlaskJSONEncoder.default(self, o)
