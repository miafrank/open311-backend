from moto import mock_dynamodb2
import boto3
import json

from config import *
from db_utils import *
from api_utils import *


def mock_table_names():
    return 'mock_request_table', 'mock_services_table', 'mock_service_definition'


@mock_dynamodb2
def dynamodb_setup(table_name):
    dynamodb = boto3.resource('dynamodb', 'us-east-1')
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=REQUESTS_KEY_SCHEMA,
        AttributeDefinitions=REQUESTS_ATTR_DEF,
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    return dynamodb.Table('mock_activity_table')


def load_resource(resource_path):
    with open(resource_path) as resource:
        resource = json.load(resource)
    return resource


def test_insert_item():
    pass