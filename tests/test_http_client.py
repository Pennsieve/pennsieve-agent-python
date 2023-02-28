from pennsieve2.direct import HttpApiClient
from tests.conftest import MockAPISessionProvider

DEFAULT_EXPECTED_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json; charset=utf-8",
    "Authorization": f"Bearer {MockAPISessionProvider.token}",
    "X-ORGANIZATION-ID": MockAPISessionProvider.org_id,
}


def test_get(mock_api_session_provider, mock_requests_session):
    client = HttpApiClient(
        "https://api.example.com", "https://api2.example.com", mock_api_session_provider
    )
    client.get("/datasets")
    method_calls = mock_requests_session.method_calls
    assert len(method_calls) == 1
    (m, _, kwargs) = method_calls[0]
    assert m == "().get"
    assert_contains_value(kwargs, "url", f"{client.api_host}/datasets")
    assert_contains_value(kwargs, "headers", DEFAULT_EXPECTED_HEADERS)


def test_post(mock_api_session_provider, mock_requests_session):
    client = HttpApiClient(
        "https://api.example.com", "https://api2.example.com", mock_api_session_provider
    )
    expected_payload = {"key": "value"}
    client.post("/datasets", json=expected_payload)
    method_calls = mock_requests_session.method_calls
    assert len(method_calls) == 1
    (m, _, kwargs) = method_calls[0]
    assert m == "().post"
    assert_contains_value(kwargs, "url", f"{client.api_host}/datasets")
    assert_contains_value(kwargs, "headers", DEFAULT_EXPECTED_HEADERS)
    assert_contains_value(kwargs, "json", expected_payload)


def test_put(mock_api_session_provider, mock_requests_session):
    client = HttpApiClient(
        "https://api.example.com", "https://api2.example.com", mock_api_session_provider
    )
    expected_payload = {"key": "value"}
    client.put("/datasets", json=expected_payload)
    method_calls = mock_requests_session.method_calls
    assert len(method_calls) == 1
    (m, _, kwargs) = method_calls[0]
    assert m == "().put"
    assert_contains_value(kwargs, "url", f"{client.api_host}/datasets")
    assert_contains_value(kwargs, "headers", DEFAULT_EXPECTED_HEADERS)
    assert_contains_value(kwargs, "json", expected_payload)


def test_delete(mock_api_session_provider, mock_requests_session):
    client = HttpApiClient(
        "https://api.example.com", "https://api2.example.com", mock_api_session_provider
    )
    client.delete("/datasets/1")
    method_calls = mock_requests_session.method_calls
    assert len(method_calls) == 1
    (m, _, kwargs) = method_calls[0]
    assert m == "().delete"
    assert_contains_value(kwargs, "url", f"{client.api_host}/datasets/1")
    assert_contains_value(kwargs, "headers", DEFAULT_EXPECTED_HEADERS)


def test_custom_headers(mock_api_session_provider, mock_requests_session):
    client = HttpApiClient(
        "https://api.example.com", "https://api2.example.com", mock_api_session_provider
    )
    custom_header = {"X-CUSTOM-HEADER": "custom-value"}
    client.get("/datasets", headers=custom_header)
    method_calls = mock_requests_session.method_calls
    assert len(method_calls) == 1
    (_, _, kwargs) = method_calls[0]
    assert_contains_value(kwargs, "headers", dict(DEFAULT_EXPECTED_HEADERS, **custom_header))


def test_header_override(mock_api_session_provider, mock_requests_session):
    client = HttpApiClient(
        "https://api.example.com", "https://api2.example.com", mock_api_session_provider
    )
    override_header = {"Accept": "text/html"}
    client.get("/datasets", headers=override_header)
    method_calls = mock_requests_session.method_calls
    (_, _, kwargs) = method_calls[0]
    assert_contains_value(kwargs, "headers", dict(DEFAULT_EXPECTED_HEADERS, **override_header))
    assert kwargs["headers"]["Accept"] != DEFAULT_EXPECTED_HEADERS["Accept"]


def test_reset_base_urls(mock_api_session_provider, mock_requests_session):
    client = HttpApiClient(
        "https://api.example.com", "https://api2.example.com", mock_api_session_provider
    )
    new_api_host = "https//new.example.com"
    new_api2_host = "https//new2.example.com"
    client.reset_base_urls(new_api_host, new_api2_host)
    client.get("/datasets")
    method_calls = mock_requests_session.method_calls
    assert len(method_calls) == 1
    (_, _, kwargs) = method_calls[0]
    assert_contains_value(kwargs, "url", f"{new_api_host}/datasets")


def assert_contains_value(mapping, key, value):
    assert key in mapping
    assert mapping[key] == value
