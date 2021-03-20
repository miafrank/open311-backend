import boto3


def db_client():
    return boto3.client('dynamodb')


def db_resource():
    return boto3.resource('dynamodb')


def db_table(table_name):
    return db_resource().Table(table_name)
