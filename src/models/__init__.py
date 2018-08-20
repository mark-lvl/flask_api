# /src/models/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize db instance
db = SQLAlchemy()

bcrypt = Bcrypt()