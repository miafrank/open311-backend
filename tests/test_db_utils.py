import json
from http import HTTPStatus

import pytest
from moto import mock_dynamodb2
from db_utils import *

requests_table_name, services_table_name, service_definition_name = (REQUESTS_TABLE_NAME,
                                                                     SERVICES_TABLE_NAME,
                                                                     SERVICE_DEFINITIONS_TABLE_NAME)


@mock_dynamodb2
def dynamodb_setup(table_name, key_schema, attr_def):
    db = boto3.resource('dynamodb', 'us-east-1')
    db.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attr_def,
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    return db.Table(table_name)


def load_resource(resource_path):
    with open(resource_path) as resource:
        resource = json.load(resource)
    return resource


@mock_dynamodb2
@pytest.mark.parametrize("table_name, key_schema, attr_def",
                         [(requests_table_name,
                           REQUESTS_KEY_SCHEMA,
                           REQUESTS_ATTR_DEF),
                          (services_table_name,
                           SERVICES_KEY_SCHEMA,
                           SERVICES_ATTR_DEF)])
def test_create_table(table_name, key_schema, attr_def):
    table = create_table(table_name, key_schema, attr_def)
    assert table == boto3.resource('dynamodb').Table(name=table_name)


@mock_dynamodb2
@pytest.mark.parametrize("table_name, key_schema, attr_def, response, expected",
                         [(services_table_name,
                           SERVICES_KEY_SCHEMA,
                           SERVICES_ATTR_DEF,
                           load_resource('tests/services.json'), HTTPStatus.OK),
                          (requests_table_name,
                           REQUESTS_KEY_SCHEMA,
                           REQUESTS_ATTR_DEF,
                           load_resource('tests/requests.json'), HTTPStatus.OK)])
def test_insert_item(table_name, key_schema, attr_def, response, expected):
    # moto not up to date with boto3 to allow empty attributes
    # overwrite empty attributes with None
    for res in response:
        for k, v in res.items():
            if not v:
                res[k] = None
    requests_table = dynamodb_setup(table_name, key_schema, attr_def)
    item = insert_resource(requests_table, response)
    assert item['ResponseMetadata']['HTTPStatusCode'] == expected


@mock_dynamodb2
@pytest.mark.parametrize("table_name, key_schema, attr_def, service_codes, service_definition_response, expected",
                         [(service_definition_name,
                           SERVICE_DEFINITIONS_KEY_SCHEMA,
                           SERVICES_ATTR_DEF,
                           load_resource('tests/services.json'),
                           load_resource('tests/service_definition_886.json'), HTTPStatus.OK),
                          (service_definition_name,
                           SERVICE_DEFINITIONS_KEY_SCHEMA,
                           SERVICES_ATTR_DEF,
                           load_resource('tests/services.json'),
                           load_resource('tests/service_definition_1864.json'), HTTPStatus.OK)])
def test_insert_item_with_id(table_name, key_schema, attr_def, service_codes, service_definition_response, expected):
    service_definition_table = dynamodb_setup(table_name,
                                              key_schema,
                                              attr_def)
    item = insert_resources_with_id(service_definition_table,
                                    service_definition_response)

    assert item['ResponseMetadata']['HTTPStatusCode'] == expected


@pytest.mark.parametrize("response, expected",
                         [(load_resource('tests/services.json'), 2),
                          ([], 0)])
def test_child_service_codes(response, expected):
    service_codes = get_child_service_codes(response)
    assert len(service_codes) == expected
