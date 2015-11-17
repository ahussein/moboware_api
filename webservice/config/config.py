class DefaultConfig(object):
    """
    Default Config (Is used when MOBOWAREAPICONFIG environment variable is not set)
    """
    APP_NAME = 'moboware-api'
    DEBUG = True
    LOG_LEVEL = 'WARNING'
    LOG_DIR = 'logs'
    SQLALCHEMY_DATABASE_URI = "sqlite:///database/api.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "Ch4ng3M3!"
    RECURLY_API_KEY = '643b428845334d0daafb319e83fc3b46'


class Development(DefaultConfig):
    """
    Config class for development.
    """
    DEBUG = True
    LOG_LEVEL = 'INFO'
    SQLALCHEMY_DATABASE_URI = "sqlite:///database/api_test.db"


class UnitTesting(DefaultConfig):
    """
    Config class for unittests
    """
    DEBUG = True
    LOG_LEVEL = 'INFO'
    SQLALCHEMY_DATABASE_URI = "sqlite:///database/api_unittest.db"
