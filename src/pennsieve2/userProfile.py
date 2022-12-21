"""
Copyright (c) 2022 Patryk Orzechowski | Wagenaar Lab | University of Pennsylvania
"""

import configparser
import logging
import os
from pathlib import Path

from .protos import agent_pb2


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
        api_host=None,
        api_port=None,
        api_key=None,
        api_secret=None,
        bucket=None,
        chunk_size=None,
        n_workers=None,
        config_file=None,
        profile_name=None,
    ):
        self._stub = stub
        # overwriting config with environmental variables
        if api_host is None or api_key is None or api_secret is None:
            self._parse_config(config_file)
        if api_host is not None:
            os.environ["PENNSIEVE_API_HOST"] = api_host
        if api_port is not None:
            os.environ["PENNSIEVE_API_PORT"] = api_port
        if api_key is not None:
            os.environ["PENNSIEVE_API_KEY"] = api_key
        if api_secret is not None:
            os.environ["PENNSIEVE_API_SECRET"] = api_secret
        if bucket is not None:
            os.environ["PENNSIEVE_API_BUCKET"] = bucket
        if chunk_size is not None:
            os.environ["PENNSIEVE_AGENT_CHUNK_SIZE"] = chunk_size
        if n_workers is not None:
            os.environ["PENNSIEVE_AGENT_UPLOAD_WORKERS"] = n_workers

        if profile_name is not None:
            self.switch(profile_name)
        self.reauthenticate()
        self.whoami()

    def reauthenticate(self):
        """Reauthenticates with GO agent on the server"""
        request = agent_pb2.ReAuthenticateRequest()
        return self._stub.ReAuthenticate(request=request)

    def whoami(self):
        """Checks and prints current user credentials"""
        request = agent_pb2.GetUserRequest()
        response = self._stub.GetUser(request=request)
        self.session_token = response.session_token
        self.organization_id = response.organization_id
        self.api_host = "https://api.pennsieve.io"
        if "api_host" in self.config[response.profile.lower()]:
            self.api_host = self.config[response.profile.lower()]["api_host"]
        logging.info(response)
        logging.info(self.api_host)
        self.credentials = {
            "session_token": response.session_token,
            "organization_id": response.organization_id,
        }
        return self.credentials

    def switch(self, profile):
        """Switches profile of the user to one defined in config file
            (by default ~/.pennsieve/config.ini)

        Parameters:
        -----------
        profile : str
            a name of the profile in config file
        """
        logging.info("Switching profile to: " + profile)
        request = agent_pb2.SwitchProfileRequest(profile=profile)
        response = self._stub.SwitchProfile(request=request)
        return response

    def _parse_config(self, config_file=None):
        """Reads Pennsieve config file and sets available configs for the user

        Parameters:
        -----------
        configFile : str, optional
           a name of the file with Pennsieve agent config (by default ~/.pennsieve/config.ini)
        """
        self.config = configparser.ConfigParser()
        if not config_file:
            config_file = os.path.join(Path.home(), ".pennsieve", "config.ini")
        self.config.read(config_file)
