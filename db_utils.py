from config import *
from db import *


def create_table(table_name, key_schema, attr_def):
    return db_resource().create_table(TableName=table_name,
                                      KeySchema=key_schema,
                                      AttributeDefinitions=attr_def,
                                      ProvisionedThroughput={
                                          'ReadCapacityUnits': 1,
                                          'WriteCapacityUnits': 1
                                      })


def insert_resource(table_name_resource, response):
    # table name corresponds directly to resources "requests" and "services"
    for item in response:
        if table_name_resource.name == REQUESTS_TABLE_NAME:
            # store LAT, LONG as strings - DynamoDB cannot store numbers with precision points
            item["LAT"] = str(item["LAT"])
            item["LONG"] = str(item["LONG"])
            table_name_resource.put_item(Item=item)
        elif table_name_resource.name == SERVICES_TABLE_NAME:
            table_name_resource.put_item(Item=item)
        else:
            # TODO test this and come up with better reponse
            return "Table not found"


def get_child_service_codes(response):
    # filter out top level parent services with no service definition
    service_definitions = [service
                           for service in response
                           if service["PARENT_SERVICE_CODE"] != PARENT_SERVICE_CODE
                           or service["HIERARCHY_LEVEL"] != HIERARCHY_LEVEL]

    return list(map(lambda x: x["SERVICE_CODE"], service_definitions))


def insert_resources_with_id(table_name_resource, response):
    # todo this is fucked. this interface is not like the others. need to parse service code in db item
    for item in response:
        table_name_resource.put_item(Item={'SERVICE_CODE': response['SERVICE_CODE'], 'ITEMS': item})
