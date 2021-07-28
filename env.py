from dotenv import load_dotenv
import logging
from os import getenv


def setup_env():
    load_dotenv()
    _aws_access_key_id()
    _aws_secret_access_key()


def _aws_access_key_id():
    if getenv('AWS_ACCESS_KEY_ID'):
        pass
    else:
        raise EnvironmentError(logging.error("Missing access key id or secret access key AWS credential"))


def _aws_secret_access_key():
    if getenv('AWS_SECRET_ACCESS_KEY'):
        pass
    else:
        raise EnvironmentError(logging.error("Missing access key id or secret access key AWS credential"))


def api_key():
    key = getenv('STL_API_KEY')
    if key:
        return key
    else:
        raise EnvironmentError(logging.error("API Key invalid."))
