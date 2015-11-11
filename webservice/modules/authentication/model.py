from webservice import db
from webservice.utils.model import BaseModel

# class BaseModel(db.Model):
#     """
#     a base model for other database tables to inherit
#     """
#     __abstract__ = True
#     identifier = db.Column(db.Integer, primary_key=True)
#     date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
#     date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
#                               onupdate=db.func.current_timestamp())


class APIAuth(BaseModel):
    """
    Model for APIKEYs.
    """
    # identifier = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    description = db.Column(db.String(255), unique=False)

    def __init__(self, key, email, description=''):
        self.key = key
        self.email = email
        self.description = description

    def __repr__(self):
        return '<Key %r>' % self.email
