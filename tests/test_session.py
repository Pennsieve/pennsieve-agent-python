import datetime
from pennsieve2.session import APISession
from tests.conftest import MockAPISessionProvider


def test_unexpired_token(mock_api_session_provider):
    expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)
    session = APISession(
        token='session-token',
        expiration=expiration,
        organization_node_id='N:organization:00000000-aaaa-1111-bbbb-222222222222'
    )
    assert not session.is_almost_expired()

    mock_api_session_provider._api_session = session
    from_provider = mock_api_session_provider.get_api_session()
    assert from_provider.token == session.token


def test_unexpired_token_int(mock_api_session_provider):
    expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)
    session = APISession(
        token='session-token',
        expiration=int(expiration.timestamp()),
        organization_node_id='N:organization:00000000-aaaa-1111-bbbb-222222222222'
    )
    assert not session.is_almost_expired()

    mock_api_session_provider._api_session = session
    from_provider = mock_api_session_provider.get_api_session()
    assert from_provider.token == session.token


def test_expired_token(mock_api_session_provider):
    expiration = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(seconds=1)
    session = APISession(
        token='session-token',
        expiration=expiration,
        organization_node_id='N:organization:00000000-aaaa-1111-bbbb-222222222222'
    )
    assert session.is_almost_expired()

    mock_api_session_provider._api_session = session
    from_provider = mock_api_session_provider.get_api_session()
    assert from_provider.token == MockAPISessionProvider.token


def test_expired_token_int(mock_api_session_provider):
    expiration = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(seconds=2)
    session = APISession(
        token='session-token',
        expiration=int(expiration.timestamp()),
        organization_node_id='N:organization:00000000-aaaa-1111-bbbb-222222222222'
    )
    assert session.is_almost_expired()

    mock_api_session_provider._api_session = session
    from_provider = mock_api_session_provider.get_api_session()
    assert from_provider.token == MockAPISessionProvider.token


def test_almost_expired_token(mock_api_session_provider):
    expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=1)
    session = APISession(
        token='session-token',
        expiration=expiration,
        organization_node_id='N:organization:00000000-aaaa-1111-bbbb-222222222222'
    )
    assert session.is_almost_expired()

    mock_api_session_provider._api_session = session
    from_provider = mock_api_session_provider.get_api_session()
    assert from_provider.token == MockAPISessionProvider.token
