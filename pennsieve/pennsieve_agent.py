import sys
import argparse
#import configparser
import grpc

#import os

from protos import agent_pb2_grpc, agent_pb2
from manifest import Manifest
#from userProfile import UserProfile
from api import PennsieveAPI
#from pathlib import Path


class PennsieveApp(object):

    def __init__(self, target='localhost:9000', options=None, compression=None):
        channel = grpc.insecure_channel(target)
        try:
            grpc.channel_ready_future(channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            sys.exit('Error connecting to server')
        else:
            self.stub = agent_pb2_grpc.AgentStub(channel)
        self.manifest = Manifest(self.stub)
        assert (self.stub is not None)
#        self._parse_config(configFile)
        self.api = PennsieveAPI(self.stub)
#        self.user = self.api.getUser()
        self.test= self



    def _parse_config(self, configFile):
        self.config=configparser.ConfigParser()
        if not configFile:
            configFile=os.path.join(Path.home(),'.pennsieve','config.ini')
        self.config.read(configFile)

#        for key in self.config:
#            print(key)
#        print(str(self.config.sections()))

