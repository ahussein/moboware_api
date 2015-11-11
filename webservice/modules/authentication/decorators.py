from functools import wraps
from flask import request, abort
from webservice import log

from webservice.modules.authentication.model import APIAuth


def find_api_key(key):
    """
    Match API keys
    @param key: API key from request
    @return: boolean
    """
    if key is None:
        return False

    api_key_entry = APIAuth.query.filter_by(key=key).first()
    if api_key_entry:
        return True

def require_app_key(f):
    """
    @param f: flask function
    @return: decorator, return the wrapped function or abort json object.
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.form.get('api_key')
        if find_api_key(key):
            return f(*args, **kwargs)
        else:
            log.warning("Unauthorized key %s trying to use API: " % key)
            abort(401)

    return decorated
