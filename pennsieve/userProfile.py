"""
Copyright (c) 2022 Patryk Orzechowski | Wagenaar Lab | University of Pennsylvania
"""

import os
import configparser
from pathlib import Path
from protos import agent_pb2


class UserProfile:
    """ A class to handle user credentials.
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

    def __init__(self, stub):
        self._stub = stub
        self._parse_config()
        self.whoami()

    def reauthenticate(self):
        """ Reauthenticates with GO agent on the server """
        request = agent_pb2.ReAuthenticateRequest()
        return self._stub.ReAuthenticate(request=request)

    def whoami(self):
        """ Checks and prints current user credentials """
        request = agent_pb2.GetUserRequest()
        response = self._stub.GetUser(request=request)
        self.session_token = response.session_token
        self.organization_id = response.organization_id
        self.api_host = self.config[response.profile]["api_host"]
        print(response)
        print(self.api_host)
        self.credentials = {
            "session_token": response.session_token,
            "organization_id": response.organization_id,
        }
        return self.credentials

    def switch(self, profile):
        """ Switches profile of the user to one defined in config file (by default ~/.pennsieve/config.ini)

        Parameters:
        -----------
        profile : str
            a name of the profile in config file
        """
        request = agent_pb2.SwitchProfileRequest(profile=profile)
        response = self._stub.SwitchProfile(request=request)
        self.whoami()

    def _parse_config(self, configFile=None):
        """ Reads Pennsieve config file and sets available configs for the user

        Parameters:
        -----------
        configFile : str, optional
           a name of the file with Pennsieve agent config (by default ~/.pennsieve/config.ini)
        """
        self.config = configparser.ConfigParser()
        if not configFile:
            configFile = os.path.join(Path.home(), ".pennsieve", "config.ini")
        self.config.read(configFile)
