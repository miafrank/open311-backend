from api_utils import build_url


resource, code = 'services', '15'


def test_build_open311_resources_url():
    url = build_url(resource=resource)
    expected = 'https://www.stlouis-mo.gov/powernap/stlouis/api.cfm/services.json?api_key=api_key'
    assert url == expected


def test_build_open311_resources_url_with_id():
    url = build_url(resource=resource, code=code)
    expected = 'https://www.stlouis-mo.gov/powernap/stlouis/api.cfm/services/1500.json?api_key=api_key'
    assert url == expected
