from dataclasses import is_dataclass

from connexion.apps.flask_app import FlaskJSONEncoder
import six

from core.utils.serialization import serialize
from swagger_server.models.base_model_ import Model


class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if is_dataclass(o):
            return serialize(o).for_api()
        if isinstance(o, Model):
            dikt = {}
            for attr, _ in six.iteritems(o.swagger_types):
                value = getattr(o, attr)
                if value is None and not self.include_nulls:
                    continue
                attr = o.attribute_map[attr]
                dikt[attr] = value
            return dikt
        return FlaskJSONEncoder.default(self, o)
