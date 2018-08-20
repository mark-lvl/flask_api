# /run.py

import os

from src.app import create_app

if __name__ == '__main__':
    app = create_app(os.getenv('APP_SETTINGS'))
    # run app
    app.run()