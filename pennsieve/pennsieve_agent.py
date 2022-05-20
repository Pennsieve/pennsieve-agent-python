import argparse
import grpc
from protos import agent_pb2_grpc, agent_pb2
from manifest import Manifest
from userProfile import UserProfile


class PennsieveApp(object):
    def __init__(self, target='localhost:9000', options=None, compression=None):
        channel = grpc.insecure_channel(target)
        self.stub = agent_pb2_grpc.AgentStub(channel)
        self.manifest = Manifest(self.stub)
        self.profile = UserProfile(self.stub)
        assert (self.stub is not None)

