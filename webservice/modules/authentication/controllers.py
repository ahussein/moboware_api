import math
from flask import Blueprint, jsonify, request
from webservice.utils.utils import crossdomain
from webservice.utils import constants
from webservice.utils import utils
from sqlalchemy.exc import IntegrityError
from webservice.modules.authentication.model import APIAuth
from webservice import log
from webservice import db

authentication_mod = Blueprint('apikey', __name__, url_prefix='/api/v<float:version>/apikey')


@authentication_mod.route('/', methods=['POST'])
@crossdomain
def generate_key(version):
    """
    Controller to generate new API key for a customer
    @return: Response and HTTP code
    """

    # API Version 1.X
    if math.floor(version) == 1:
        email = request.form.get('email', '')
        if not email:
            return jsonify({'status': 'error', 'message': 'Invalid customer email address'}), constants.HTTP_NOT_ACCEPTABLE

        api_key_entry = APIAuth.query.filter_by(email=email).first()

        api_key = utils.generate_hash_key()
        if api_key_entry is None:
            log.info('No API key found for customer with email:%s ....Generating new key', email)
            api_auth = APIAuth(key=api_key, email=email)
            db.session.add(api_auth)
        else:
            log.info('Customer with email:%s already has an API key. Re-Generating new key', email)
            api_key_entry.key = api_key

        try:
            db.session.commit()
        except IntegrityError, ex:
            return jsonify({"status": "error", "message": "error when committing object to database",
                            "exception": ex.message}), constants.HTTP_INTERNAL_ERROR
        else:
            return jsonify({'APIKEY': api_key, 'status': 'success'}), constants.HTTP_OK
    else:
        return jsonify({'status': 'error', 'message': 'Unsupported API version used.'}), constants.HTTP_VERSION_UNSUPPORTED
