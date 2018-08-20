# /src/models/TermModel

import datetime
from . import db


class TermModel(db.Model):
    """
    Term Entity
    """

    # Defining table name
    __tablename__ = 'terms'

    # Defining entity fields and columns
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __int__(self, data):
        # Pre-set object attributes
        self.term = data.get('term')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for attr, attr_value in data.items():
            setattr(self, attr, attr_value)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_term(term):
        return TermModel.query.filter_by(term=term).first()

    @staticmethod
    def get_all_term(id):
        return TermModel.query.all()

    def __repr__(self):
        return "<id {}>".format(self.id)
