import json
from moto import mock_dynamodb2
import pytest

from db_utils import *
from config import *
from db import *

requests_table_name, services_table_name, service_definition_name = (REQUESTS_TABLE_NAME,
                                                                     SERVICES_TABLE_NAME,
                                                                     SERVICE_DEFINITIONS_TABLE_NAME)


@mock_dynamodb2
def dynamodb_setup(table_name, key_schema, attr_def):
    dynamodb = boto3.resource('dynamodb', 'us-east-1')
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attr_def,
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    return dynamodb.Table(table_name)


def load_resource(resource_path):
    with open(resource_path) as resource:
        resource = json.load(resource)
    return resource


@mock_dynamodb2
@pytest.mark.parametrize("table_name, key_schema, attr_def, response",
                         [(services_table_name,
                           SERVICES_KEY_SCHEMA,
                           SERVICES_ATTR_DEF,
                           load_resource('tests/services.json')),
                          (requests_table_name,
                           REQUESTS_KEY_SCHEMA,
                           REQUESTS_ATTR_DEF,
                           load_resource('tests/requests.json'))])
def test_insert_item(table_name, key_schema, attr_def, response):
    # moto not up to date with boto3 to allow empty attributes
    # overwrite empty attributes with None
    for res in response:
        for k, v in res.items():
            if not v:
                res[k] = None
    requests_table = dynamodb_setup(table_name, key_schema, attr_def)
    item = insert_item(requests_table, response)
    assert item['ResponseMetadata']['HTTPStatusCode'] == 200


