# /src/app.py

from flask import Flask

from .config import app_config


def create_app(env_name):
    """
    Create flask app

    :param env_name:
    :return:
    """

    # initialization the app
    app = Flask(__name__)

    # load the config setting from config file
    app.config.from_object(app_config[env_name])

    # create the initial root
    @app.route('/', methods=['GET'])
    def index():
        """
        Initial main page
        """
        return 'Hell yeah!'

    return app
