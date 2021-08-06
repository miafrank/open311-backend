import os

from dotenv import load_dotenv
import logging
from os import getenv


def setup_env():
    try:
        # TODO - maybe instead of reading this in - there is a dotenv method to use?
        open('env', 'r')
        load_dotenv()
    except(IOError, ValueError):
        logging.error('Cannot set application environment variables.')


def _get_env(env_name, msg):
    env = getenv(env_name)
    if env:
        return env
    else:
        raise KeyError(logging.error(msg))


def aws_access_key_id():
    return _get_env('AWS_ACCESS_KEY_ID', 'Missing access key id or secret access key AWS credential')


def aws_secret_access_key():
    return _get_env('AWS_SECRET_ACCESS_KEY', 'Missing access key id or secret access key AWS credential')


def api_key():
    return _get_env('STL_API_KEY', 'Missing API key')


def base_api_url():
    return _get_env('BASE_API_URL', 'Missing base url')


def api_headers():
    return _get_env('API_HEADERS', 'Missing API Headers')
