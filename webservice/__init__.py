# coding=utf-8
__version__ = 1.1
version = __version__

import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from logbook import Logger
import config
from utils.logging import DevelopmentLoggingSetup
from flask import  jsonify
from utils import constants
from utils import utils

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# Start the Flask awesomeness.
app = Flask(__name__)

# Should we use default config (Production) or is it overridden by a environmental variable?
config_name = os.getenv('MOBOWAREAPICONFIG',
                        'DefaultConfig')  # Return the value of the environment variable RESTAPICONFIG if it exists, #\ or "Default" if it doesnt’t. value defaults to None.

# Setup Config
API_CONFIG = config.defined[config_name]
app.config.from_object(API_CONFIG)

# setup the recurly backend API-KEY
RECURLY_API_KEY = API_CONFIG.RECURLY_API_KEY

# Setup SQLAlchemy
db = SQLAlchemy(app)

# Logging
log = Logger(__name__)
log_setup = DevelopmentLoggingSetup(app.config['LOG_LEVEL'])
log_setup.set_default_setup(logger = log, file_path=app.config['LOG_DIR'] + '%s.log' % app.config['APP_NAME'])

# Load App Key Auth Decorators
from modules.authentication.decorators import require_app_key

## Api routing
from modules.authentication.controllers import authentication_mod
app.register_blueprint(authentication_mod)

from modules.subscription.controllers import subscription_mod
app.register_blueprint(subscription_mod)


@app.route("/version", methods=['POST', 'OPTIONS'])
@require_app_key
def api_latest_version():
    """
    Check version of the API, protected with authorization.
    """
    return jsonify({'status': 'success', 'version': version}), constants.HTTP_OK

@app.route('/list_routes', methods=['GET', 'OPTIONS'])
def list_routes():
    import urllib

    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)
    return jsonify({'routes': sorted(output), 'status': 'success'}), constants.HTTP_OK

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
