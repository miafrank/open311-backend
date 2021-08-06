from api_utils import build_url

resource, code = 'services', '15'


def test_build_open311_resources_url():
    url = build_url(resource=resource)
    expected = 'https://test_api.com/services.json?api_key=123'
    assert url == expected


def test_build_open311_resources_url_with_id():
    url = build_url(resource=resource, code=code)
    expected = 'https://test_api.com/services/15.json?api_key=123'
    assert url == expected
