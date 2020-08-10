import logging
from os import environ

from db import db_client
import db_utils
from config import *


def create_tables():
    existing_tables = db_client().list_tables()['TableNames']

    if REQUESTS_TABLE_NAME not in existing_tables:
        db_utils.create_table(REQUESTS_TABLE_NAME, REQUESTS_KEY_SCHEMA, REQUESTS_ATTR_DEF)
    if SERVICES_TABLE_NAME not in existing_tables:
        db_utils.create_table(SERVICES_KEY_SCHEMA, SERVICES_KEY_SCHEMA, SERVICES_ATTR_DEF)


def setup():
    aws_access_key_id = environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = environ.get('AWS_SECRET_ACCESS_KEY')
    stl_open_311_api_key = environ.get('STL_API_KEY')

    if not aws_access_key_id or not aws_secret_access_key:
        raise EnvironmentError(logging.error("Missing access key id or secret access key AWS credential"))
    if not stl_open_311_api_key:
        raise EnvironmentError(logging.error("API key for STL Open 311 API missing."))

    # If tables do not exist, create tables
    create_tables()


if __name__ == "__main__":
    setup()
