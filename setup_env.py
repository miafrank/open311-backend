import logging
from os import environ

from db import db_client
from db_utils import *
from config import *


def init_tables(stl_api_key):
    existing_tables = db_client().list_tables()['TableNames']

    if REQUESTS_TABLE_NAME not in existing_tables:
        logging.info(f'Creating {REQUESTS_TABLE_NAME} table and inserting data from STL API')

        create_table(REQUESTS_TABLE_NAME, REQUESTS_KEY_SCHEMA, REQUESTS_ATTR_DEF)

        insert_item(db_resource_table(REQUESTS_TABLE_NAME),
                    get_requests_from_stl(STL_API_URL, REQUESTS_TABLE_NAME, stl_api_key))

    if SERVICES_TABLE_NAME not in existing_tables:
        logging.info(f'Creating {SERVICES_TABLE_NAME} table and inserting data from STL API')

        create_table(SERVICES_TABLE_NAME, SERVICES_KEY_SCHEMA, SERVICES_ATTR_DEF)
        insert_item(get_requests_from_stl(STL_API_URL, SERVICES_TABLE_NAME, stl_api_key))

    if SERVICE_DEFINITIONS_TABLE_NAME not in existing_tables:
        logging.info(f'Creating {SERVICE_DEFINITIONS_TABLE_NAME} table and inserting data from STL API')

        create_table(SERVICE_DEFINITIONS_TABLE_NAME, SERVICE_DEFINITIONS_KEY_SCHEMA, SERVICE_DEFINITIONS_ATTR_DEF)
        insert_item(get_requests_from_stl(STL_API_URL, SERVICE_DEFINITIONS_TABLE_NAME, stl_api_key))


def setup():
    aws_access_key_id = environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = environ.get('AWS_SECRET_ACCESS_KEY')
    stl_api_key = environ.get('STL_API_KEY')

    if not aws_access_key_id or not aws_secret_access_key:
        raise EnvironmentError(logging.error("Missing access key id or secret access key AWS credential"))
    if not stl_api_key:
        raise EnvironmentError(logging.error("API key for STL Open 311 API missing."))

    init_tables(stl_api_key)


if __name__ == "__main__":
    setup()
