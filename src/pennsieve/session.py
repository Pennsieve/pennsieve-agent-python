from __future__ import annotations

import datetime
from abc import ABC, abstractmethod


class APISession:
    """Holds session info for Pennsieve API

    Attributes:
    ----------
    token: str
        The AccessToken returned by Cognito. This token is needed to access Pennsieve API endpoints.
        Used as the Bearer token in the Authorization header in Pennsieve API requests.
    organization_node_id: str
        The node id of the user's organization.
        Used as the value of the X-ORGANIZATION-ID header in Pennsieve API requests.
    expiration: datetime.datetime
        the expiration datetime of the token in UTC

    Methods:
    --------
    is_almost_expired()
        returns True if token is "near" its expiration time, False if not

    """

    EXPIRATION_MARGIN = datetime.timedelta(minutes=5)

    def __init__(self, token: str, expiration: datetime.datetime | int, organization_node_id: str):
        """Constructor for APISession

        Parameters:
        ----------
        token: str
            The AccessToken returned by Cognito.
            Used as the Bearer token in the Authorization header for Pennsieve API requests.
        expiration: datetime | int
            The expiration datetime of the token in UTC.
            If this is a datetime, it should be in UTC.
            If this is an int, it should be a POSIX timestamp. It will be converted to a datetime
        organization_node_id: str
            The node id of the user's organization.
            Used as the value of the X-ORGANIZATION-ID header in Pennsieve API requests.
        """
        self.token = token
        self.expiration = (
            datetime.datetime.fromtimestamp(expiration, datetime.timezone.utc)
            if isinstance(expiration, int)
            else expiration
        )
        self.organization_node_id = organization_node_id

    def is_almost_expired(self) -> bool:
        now = datetime.datetime.now(datetime.timezone.utc)
        if now > self.expiration - APISession.EXPIRATION_MARGIN:
            return True
        return False

    def __str__(self):
        return str(self.__dict__)


class APISessionProvider(ABC):
    """Class that provides APISession. The returned session will not be expired"""

    @abstractmethod
    def __init__(self):
        self._api_session = None

    def get_api_session(self) -> APISession:
        """Returns a non-expired APISession"""
        if self._api_session is None or self._api_session.is_almost_expired():
            self._api_session = self.new_api_session()
        return self._api_session

    @abstractmethod
    def new_api_session(self) -> APISession:
        pass

    def clear_session(self, options: dict = None):
        self._api_session = None

    def close(self):
        pass
