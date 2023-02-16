import datetime
import os
from unittest.mock import patch

import pytest

from pennsieve2.session import APISession, APISessionProvider


@pytest.fixture(scope="session")
def test_resources_dir():
    return os.path.join(os.path.dirname(__file__), "resources")


@pytest.fixture()
def mock_api_session_provider():
    provider = MockAPISessionProvider()
    yield provider
    provider._api_session = None


@pytest.fixture()
def mock_requests_session():
    with patch("requests.Session", autospec=True) as s:
        yield s


class MockAPISessionProvider(APISessionProvider):
    token = "new-token"
    org_id = "N:organization:00000000-aaaa-1111-bbbb-222222222222"

    def __init__(self):
        super().__init__()

    def new_api_session(self) -> APISession:
        return APISession(
            token=self.token,
            expiration=datetime.datetime.now(datetime.timezone.utc),
            organization_node_id=self.org_id,
        )
