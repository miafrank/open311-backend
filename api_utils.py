import requests


def build_open311_resources_url(api_endpoint, resource, api_key):
    return f'{api_endpoint}{resource}.json?api_key={api_key}'


def get_requests_from_stl(api_endpoint, resource, api_key):
    return requests.get(build_open311_resources_url(api_endpoint, resource, api_key)).json()
