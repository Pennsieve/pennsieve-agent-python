import datetime
from pennsieve2.session import APISession


def test_unexpired_token():
    expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)
    session = APISession(
        token='session-token',
        expiration=expiration,
        organization_node_id='N:organization:00000000-aaaa-1111-bbbb-222222222222'
    )
    assert not session.is_almost_expired()


def test_unexpired_token_int():
    expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)
    session = APISession(
        token='session-token',
        expiration=int(expiration.timestamp()),
        organization_node_id='N:organization:00000000-aaaa-1111-bbbb-222222222222'
    )
    assert not session.is_almost_expired()


def test_expired_token():
    expiration = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(seconds=1)
    session = APISession(
        token='session-token',
        expiration=expiration,
        organization_node_id='N:organization:00000000-aaaa-1111-bbbb-222222222222'
    )
    assert session.is_almost_expired()


def test_expired_token_int():
    expiration = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(seconds=2)
    session = APISession(
        token='session-token',
        expiration=int(expiration.timestamp()),
        organization_node_id='N:organization:00000000-aaaa-1111-bbbb-222222222222'
    )
    assert session.is_almost_expired()


def test_almost_expired_token():
    expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=1)
    session = APISession(
        token='session-token',
        expiration=expiration,
        organization_node_id='N:organization:00000000-aaaa-1111-bbbb-222222222222'
    )
    assert session.is_almost_expired()
