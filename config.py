# Table names
REQUESTS_TABLE_NAME = 'requests'
SERVICES_TABLE_NAME = 'services'
SERVICE_DEFINITIONS_TABLE_NAME = 'service_definition'

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

SERVICE_DEFINITIONS_KEY_SCHEMA = []

# Attribute Definitions
REQUESTS_ATTR_DEF = [
    {
        'AttributeName': 'SERVICE_REQUEST_ID',
        'AttributeType': 'N'
    },

]

SERVICES_ATTR_DEF = [
    {
        'AttributeName': 'SERVICE_REQUEST_ID',
        'AttributeType': 'N'
    },

]

SERVICE_DEFINITIONS_ATTR_DEF = []

# API Urls
STL_API_URL = 'https://www.stlouis-mo.gov/powernap/stlouis/api.cfm/'
REQUESTS_RESOURCE = 'requests'
SERVICES_RESOURCE = 'services'
