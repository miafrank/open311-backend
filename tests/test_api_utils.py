from api_utils import *


api_endpoint, resource, api_key = 'endpoint/', 'services', 'api_key'


def test_build_open311_resources_url():
    url = build_open311_resources_url(api_endpoint, resource, api_key)
    expected = 'endpoint/services.json?api_key=api_key'
    assert url == expected


def test_build_open311_resources_url_with_id():
    url = build_open311_resources_url_with_id(api_endpoint, resource, '1500', api_key)
    expected = 'endpoint/services/1500.json?api_key=api_key'
    assert url == expected