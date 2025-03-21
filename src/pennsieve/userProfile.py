"""
Copyright (c) 2022 Patryk Orzechowski | Wagenaar Lab | University of Pennsylvania
"""

import logging

from .protos import agent_pb2
from .protos.agent_pb2 import UserResponse

logger = logging.getLogger(__name__)


class UserProfile:
    """A class to handle user credentials.
    Attributes:
    -----------
    _stub : object
        AgentStub from Pennsieve agent GO library
    session_token : str
        A token obtained from the server after reauthentication
    api_host : str
        A url of the host to which the queries will be sent
    organization_id : str
        An organization that the user belongs to
    config : object
        A config parsed from config.ini file using configparser

    Methods:
    --------
    reauthenticate()
        Reauthenticates with GO agent on the server.
    whoami()
        Checks and prints current user credentials.
    switch(profile)
        Switches profile of the user to one defined in config file.

    """

    def __init__(
        self,
        stub,
        profile_name=None,
    ):
        self._stub = stub
        if profile_name is None:
            self.current_user: UserResponse = self.whoami()
        else:
            self.switch(profile_name)
        logger.info(f"current profile is {self.current_user.profile}")

    def reauthenticate(self):
        """Reauthenticates with GO agent on the server"""
        request = agent_pb2.ReAuthenticateRequest()
        return self._stub.ReAuthenticate(request=request)

    def whoami(self) -> UserResponse:
        """Checks and prints current user credentials"""
        request = agent_pb2.GetUserRequest()
        response = self._stub.GetUser(request=request)
        return response

    def switch(self, profile):
        """Switches profile of the user to one defined in config file
            (by default ~/.pennsieve/config.ini)

        Parameters:
        -----------
        profile : str
            a name of the profile in config file
        """
        request = agent_pb2.SwitchProfileRequest(profile=profile)
        self.current_user = self._stub.SwitchProfile(request=request)
        logger.debug(f"current_user switched to: {self.current_user}")
        # Versions of the Agent prior to 1.3.1 did not populate the api_host field in SwitchProfile responses.
        if self.current_user.api_host == "":
            logger.warning(
                f"Base API URL missing from SwitchProfile response. Update Agent to version >= 1.3.2"
            )
        logger.info(f"Switched profile to: {self.current_user.profile}")
