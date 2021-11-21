#!/usr/bin/env python3
from os.path import dirname

import connexion

from core import config
from swagger_server import encoder


def main():
    config.load_config(r"%s/config.yml" % dirname(__file__))
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Smart Insurance System'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
