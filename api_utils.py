import requests
from http import HTTPStatus


def build_open311_resources_url(api_endpoint, resource, api_key):
    return f'{api_endpoint}{resource}.json?api_key={api_key}'


def build_open311_resources_url_with_id(api_endpoint, resource, service_code, api_key):
    return f'{api_endpoint}{resource}/' \
           f'{service_code}.json' \
           f'?api_key={api_key}'


def get_requests_from_stl(api_endpoint, resource, api_key):
    url = build_open311_resources_url(api_endpoint, resource, api_key)
    resp = requests.get(url).json()
    return resp


def get_resource_by_id(api_endpoint, resource, service_code, api_key):
    url = build_open311_resources_url_with_id(api_endpoint, resource, service_code, api_key)
    response = requests.get(url).json()
    if 'CODE' in response and response['CODE'] == HTTPStatus.NOT_FOUND:
        # TODO - confirm this behavior
        # STL API does not return HTTP.404 when service code not found or service code is parent service code
        # parent service codes do not have a service definition. Return response as service code with empty attr
        return {"SERVICE_CODE": service_code, "ERROR": {HTTPStatus.NOT_FOUND}}
    return response
