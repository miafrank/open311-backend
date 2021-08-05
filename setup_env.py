from env import setup_env
from api_utils import *
from db_utils import *
from db import *


def init_tables():
    create_tables(REQUESTS_TABLE_NAME, REQUESTS_KEY_SCHEMA, REQUESTS_ATTR_DEF)
    insert_resource(db_table(REQUESTS_TABLE_NAME), fetch_all(REQUESTS_TABLE_NAME))

    create_tables(SERVICES_TABLE_NAME, SERVICES_KEY_SCHEMA, SERVICES_ATTR_DEF)
    insert_resource(db_table(SERVICES_TABLE_NAME), fetch_all(SERVICES_TABLE_NAME))

    create_tables(SERVICE_DEFINITIONS_TABLE_NAME, SERVICE_DEFINITIONS_KEY_SCHEMA, SERVICE_DEFINITIONS_ATTR_DEF)
    service_codes = get_child_service_codes(fetch_all(SERVICES_TABLE_NAME))

    for service_code in service_codes:
        service_def = fetch_by_id(STL_API_URL, service_code)
        insert_resources_with_id(db_table(SERVICE_DEFINITIONS_TABLE_NAME), service_def)


if __name__ == "__main__":
    # Load environment variables
    setup_env()
    # Create tables and insert data
    init_tables()
