import requests
from http import HTTPStatus
from env import api_key, base_api_url, api_headers


def fetch_all(resource):
    url = build_url(resource=resource)
    return requests.get(url).json()


def fetch_by_id(resource, code):
    url = build_url(resource=resource, code=code)
    response = requests.get(url).json()

    if 'CODE' in response and response['CODE'] == HTTPStatus.NOT_FOUND:
        # TODO - Save parent service code
        # STL API does not return HTTP.404 when service code not found or service code is parent service code
        # parent service codes do not have a service definition. Return response as service code with empty attr
        return {"SERVICE_CODE": code, "ERROR": {HTTPStatus.NOT_FOUND}}
    else:
        # TODO - Save resource (service def, request, or service)
        return response


def build_url(**kwargs):
    if kwargs['code']:
        return f'{base_api_url}{kwargs["resource"]}/{kwargs["code"]}{api_headers}{api_key}'
    else:
        return f'{base_api_url}{kwargs["resource"]}{api_headers}{api_key}'
