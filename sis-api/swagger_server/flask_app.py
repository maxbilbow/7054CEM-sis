# Import the Flask class. An instance of this class will be our WSGI application.
from flask import Flask

import connexion

from swagger_server import encoder, db

# app = connexion.App(__name__, specification_dir='./swagger/')
# app.app.json_encoder = encoder.JSONEncoder
# app.add_api('swagger.yaml', arguments={'title': 'Smart Insurance System'}, pythonic_params=True)