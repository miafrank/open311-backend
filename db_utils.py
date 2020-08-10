from pprint import pprint
from os import environ

from api_utils import get_requests_from_stl
from db import db_client, db_resource
from config import *


def create_table(table_name, key_schema, attr_def):
    return db_resource().create_table(TableName=table_name,
                                      KeySchema=key_schema,
                                      AttributeDefinitions=attr_def,
                                      ProvisionedThroughput={
                                          'ReadCapacityUnits': 1,
                                          'WriteCapacityUnits': 1
                                      })


def insert_item(table_name):
    stl_open_311_api_key = environ['STL_API_KEY']

    # table name corresponds directly to resource (endpoint) name
    response = get_requests_from_stl(STL_API_URL, table_name, stl_open_311_api_key)
    requests_table = db_resource().Table(table_name)

    for item in response:
        if table_name == 'requests':
            # Store LAT, LONG as strings - DynamoDB cannot store numbers with precision points
            item["LAT"] = str(item["LAT"])
            item["LONG"] = str(item["LONG"])

        requests_table.put_item(Item=item)


def scan_table(table_name):
    table = db_client.scan(TableName=table_name)
    items = [item for item in table['Items']]
    return pprint(items[0:10])
