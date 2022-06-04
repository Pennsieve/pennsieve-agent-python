import sys
import argparse
#import configparser
import grpc

#import os

from protos import agent_pb2_grpc, agent_pb2
from manifest import Manifest
#from userProfile import UserProfile
#from api import PennsieveAPI
import requests
import json
from userProfile import UserProfile

#from pathlib import Path


class Pennsieve():

    def __init__(self, target='localhost:9000', options=None, compression=None):

        channel = grpc.insecure_channel(target)
        try:
            grpc.channel_ready_future(channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            sys.exit('Error connecting to server')
        else:
            self.stub = agent_pb2_grpc.AgentStub(channel)
        assert (self.stub is not None)

        self.api = self
        self.manifest = Manifest(self.stub)
        self.user=UserProfile(self.stub)


    def _parse_config(self, configFile):
        self.config=configparser.ConfigParser()
        if not configFile:
            configFile=os.path.join(Path.home(),'.pennsieve','config.ini')
        self.config.read(configFile)


    def _get_default_headers(self):
        return { "Content-Type" : "application/json",
                 "Accept" : "application/json; charset=utf-8",
                 "Authorization" : "Bearer " + self.user.credentials['session_token'],
                 "X-ORGANIZATION-ID" : self.user.credentials['organization_id']}


    def getUser(self):
        return self.user.whoami()


    def call(self, url, method, **kwargs):
        if url.startswith('/'):
            url=self.user.api_host + url
        if 'headers' not in kwargs:
            headers=self._get_default_headers()
        else:
            headers=kwargs['headers']
        try:
            if method.lower() == 'get':
                response = requests.get(url=url, headers=headers, **kwargs)
            elif method.lower() == 'post':
                response = requests.post(url=url, headers=headers, **kwargs)
            elif method.lower() == 'put':
                response = requests.put(url=url, headers=headers, **kwargs)
            elif method.lower() == 'delete':
                response = requests.delete(url=url, headers=headers, **kwargs)
            else:
                raise Exception('Not implemented')
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other excpetion occurred: {err}')
        else:
            return response.json() #content.decode('utf-8'))


    def get(self, url, **kwargs):
        return self.call(url, method='get', **kwargs)

    def post(self, url, json, **kwargs):
        return self.call(url, method='post', json=json, **kwargs)

    def put(self, url, json, **kwargs):
        return self.call(url, method='put', json=json, **kwargs)

    def delete(self, url, **kwargs):
        return self.call(url, method='delete', **kwargs)

    def subscribe(self, id):
        request = agent_pb2.SubscribeRequest(id=id)
        return self.stub.Subscribe(request=request)

    def unsubscribe(self, id):
        request = agent_pb2.SubscribeRequest(id=id)
        return self.stub.Unsubscribe(request=request)

