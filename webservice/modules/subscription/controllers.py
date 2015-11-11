"""
Subscription controllers
"""
import math
from flask import Blueprint, jsonify, request
from webservice.utils.utils import crossdomain
from webservice.utils import constants
from webservice.utils import utils
from webservice import log
from webservice import RECURLY_API_KEY
from webservice.modules.authentication.decorators import require_app_key
from recurly import Account
from recurly import NotFoundError
from recurly import Subscription


utils.setup_backend_api_key(api_key=RECURLY_API_KEY)

subscription_mod = Blueprint('subscription', __name__, url_prefix='/api/v<float:version>/subscription')

defaults = {}


@subscription_mod.route('', methods=['POST'])
@require_app_key
@crossdomain
def add_subscription(version):
    errors = []
    if math.floor(version) == 1:
        email = request.form.get('email')
        plan_code = request.form.get('plan_code')
        currency = request.form.get('currency', 'USD')
        quantity = int(request.form.get('quantity', 1))
        if not plan_code:
            message = 'No plan code provided. Cannot continue'
            log.error(message)
            errors.append(message)
        try:
            account = Account.get(email)
        except NotFoundError:
            message = 'No recurly account found with email address:%s' % email
            log.error(message)
            errors.append(message)
        else:
            if not errors:
                subscription = Subscription()
                subscription.plan_code = plan_code
                subscription.currency = currency
                subscription.quantity = quantity
                subscription.account = account
                try:
                    subscription.save()
                except Exception, ex:
                    message = 'Failed to create subscription for customer: %s Reason:%s' % (email, str(ex))
                    log.error(message)
                    errors.append(message)
        if errors:
            return jsonify({'status': 'error', 'message': '\n'.join(errors)}), constants.HTTP_NOT_ACCEPTABLE
        return jsonify({'status': 'success'}), constants.HTTP_OK
    else:
        return jsonify({'status': 'error', 'message': 'Unsupported API version used.'}), constants.HTTP_VERSION_UNSUPPORTED
