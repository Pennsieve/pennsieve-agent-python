from protos import agent_pb2
#import pennsieve_agent
import os
import configparser
from pathlib import Path


class UserProfile(object):

    def __init__(self, stub):
        self._stub=stub
        self._parse_config()
        self.whoami()

    def create(self):
        pass


    def reconnect(self):
        request = agent_pb2.ReAuthenticate()
        return self.stub.ReAuthenticate(request=request)


    def whoami(self):
        request = agent_pb2.GetUserRequest()
        response = self._stub.GetUser(request=request)
        print(str(response))
        self.session_token = response.session_token
        self.organization_id = response.organization_id
        self.api_host = self.config[response.profile]['api_host']
        print(response)
        print(self.api_host)
        self.credentials = {'session_token': response.session_token, 'organization_id' : response.organization_id}
        #return context

    def switch(self, profile):
        self.whoami()
        print('-------')
        request = agent_pb2.SwitchProfileRequest(profile=profile)
        response = self._stub.SwitchProfile(request=request)
        self.reconnect()
        self.whoami()


    def _parse_config(self, configFile=None):
        self.config=configparser.ConfigParser()
        if not configFile:
            configFile=os.path.join(Path.home(),'.pennsieve','config.ini')
        self.config.read(configFile)


"""
	string id = 2;
	string name = 3;
	string sessionToken = 4;
	string profile = 8;
	string environment = 9;
	string organizationId = 10;
	string organizationName = 11;"""

"""

CancelUpload
Subscribe
Unsubscribe

"""
