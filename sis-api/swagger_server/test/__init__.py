import logging

import connexion
from flask_testing import TestCase

from core.test import test_db
from swagger_server.encoder import JSONEncoder


class BaseTestCase(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        test_db.set_up()

    @classmethod
    def tearDownClass(cls) -> None:
        test_db.tear_down()

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        return app.app
