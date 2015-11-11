"""
Backend model
"""
from webservice.utils.model import BaseModel


class Backend(BaseModel):
    api_key = db.Column(db.String(120), unique=True)

    def __init__(self, api_key):
        self.api_key = api_key

    def __repr__(self):
        return 'api_key: %s' % self.api_key
