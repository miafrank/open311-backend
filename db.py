import boto3
import logging


def db_client():
    return boto3.client('dynamodb')


def db_resource():
    return boto3.resource('dynamodb')


def db_table(table_name):
    return db_resource().Table(table_name)


def existing_tables():
    return db_client().list_tables()['TableNames']


def create_tables(table_name, key_schema, attr_def):
    if table_name not in existing_tables():
        logging.info(f'Creating {table_name}')
    else:
        # TODO - Consider action when table already exists. Log?
        pass
    return db_resource().create_table(TableName=table_name,
                                      KeySchema=key_schema,
                                      AttributeDefinitions=attr_def,
                                      ProvisionedThroughput={
                                          'ReadCapacityUnits': 1,
                                          'WriteCapacityUnits': 1
                                      })
