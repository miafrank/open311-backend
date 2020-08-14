import json
import os
import sys

import boto3
from moto import mock_dynamodb2

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

import db_utils
import config
from pprint import pprint
from db import *

requests_table_name, services_table_name, service_definition_name = ('mock_request_table',
                                                                     'mock_services_table',
                                                                     'mock_service_definition')


@mock_dynamodb2
def dynamodb_setup(table_name):
    dynamodb = boto3.resource('dynamodb', 'us-east-1')
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=config.REQUESTS_KEY_SCHEMA,
        AttributeDefinitions=config.REQUESTS_ATTR_DEF,
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
def test_insert_item():
    response = load_resource('/Users/miafrank/Dev/open311-backend/tests/requests.json')
    # moto not up to date with boto3 to allow empty attributes
    # overwrite empty attributes with None
    for res in response:
        for k, v in res.items():
            if not v:
                res[k] = None
    requests_table = dynamodb_setup(requests_table_name)
    item = db_utils.insert_item(requests_table, response)

    assert item['ResponseMetadata']['HTTPStatusCode'] == 200
