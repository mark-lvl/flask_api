# /src/models/UserModel

import datetime
from . import db, bcrypt


class UserModel(db.Model):
    """
    User Entity
    """

    # Defining table name
    __tablename__ = 'users'

    # Defining entity fields and columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __int__(self, data):
        # Pre-set object attributes
        self.username = data.get('username')
        self.password = self.__generate_hash(data.get('password'))
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for attr, attr_value in data.items():
            if key == 'password':
                self.password = self.__generate_hash(attr_value)
            setattr(self, attr, attr_value)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_user_by_id(id):
        return UserModel.query.get(id)

    @staticmethod
    def get_all_users(id):
        return UserModel.query.all()

    def __repr(self):
        return "<id {}>".format(self.id)

    def __generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)
