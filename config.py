# Table names
REQUESTS_TABLE_NAME = 'requests'
SERVICES_TABLE_NAME = 'services'
SERVICE_DEFINITIONS_TABLE_NAME = 'service_definitions'

# Key Schemas
REQUESTS_KEY_SCHEMA = [
    {
        "AttributeName": "SERVICE_REQUEST_ID",
        "KeyType": "HASH"
    },
]

SERVICES_KEY_SCHEMA = [
    {
        "AttributeName": "SERVICE_CODE",
        "KeyType": "HASH"
    },
]

SERVICE_DEFINITIONS_KEY_SCHEMA = [
    {
        'AttributeName': 'SERVICE_CODE',
        'KeyType': 'HASH'
    },
]

# Attribute Definitions
REQUESTS_ATTR_DEF = [
    {
        'AttributeName': 'SERVICE_REQUEST_ID',
        'AttributeType': 'N'
    },

]

SERVICES_ATTR_DEF = [
    {
        'AttributeName': 'SERVICE_CODE',
        'AttributeType': 'N'
    },

]

SERVICE_DEFINITIONS_ATTR_DEF = [
    {
        'AttributeName': 'SERVICE_CODE',
        'AttributeType': 'N'
    },

]

# API Urls
STL_API_URL = 'https://www.stlouis-mo.gov/powernap/stlouis/api.cfm/'
REQUESTS_RESOURCE = 'requests'
SERVICES_RESOURCE = 'services'

# STL Specific config values noted here in the API documentation under GET Service List:
# https://www.stlouis-mo.gov/government/departments/information-technology/web-development/city-api/csb-api.cfm
# Top level service/parent service types have a value of 0
PARENT_SERVICE_CODE = 0
# Level for the current service type definition, the top level is 1
HIERARCHY_LEVEL = 1
