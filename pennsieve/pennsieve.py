"""
Copyright (c) 2022 Patryk Orzechowski | Wagenaar Lab | University of Pennsylvania
"""

import sys
import argparse
import grpc
import requests
import json

from protos import agent_pb2_grpc, agent_pb2
from manifest import Manifest
from userProfile import UserProfile


class Pennsieve:
    """ The main class of Python Pennsieve agent

    Attributes:
    -----------
    api : object
        a singleton for backward compatibility
    manifest : object
        a manifest with files to be uploaded
    user : object
        class managing user credentials
    datasets : dict
        a dictionary with all the datasets the user has access to

    Methods:
    --------
    getUser()
        Returns current user.
    getManifests()
        Returns available manifest in form of a list.
    getDatasets()
        Returns available datasets in form of a list.
    useDataset(dataset_id)
        specifies which dataset on the server will be used
    call(url, method, **kwargs)
        Invokes get/post/put/delete on the server endpoint defined in url.
    get(url, **kwargs)
        Invokes GET endpoint on a server. Passing server name in url is optional.
    post(url, json, **kwargs)
        Invokes POST endpoint on a server. Passing server name in url is optional.
    put(url, json, **kwargs)
        Invokes PUT endpoint on a server. Passing server name in url is optional.
    delete(url, **kwargs)
        Invokes DELETE endpoint on a server. Passing server name in url is optional.
    subscribe(id)
        Subscribes for notifications.
    unsubscribe(id)
        Unsubscribes from notifications.
    """

    def __init__(self, target="localhost:9000"):
        """ Initialization of Pennsieve Python agent

            Parameters:
            -----------
            target : str
                a socket with running GO agent
        """
        channel = grpc.insecure_channel(target)
        try:
            grpc.channel_ready_future(channel).result(timeout=100)
        except grpc.FutureTimeoutError:
            sys.exit("Error connecting to server")
        else:
            self.stub = agent_pb2_grpc.AgentStub(channel)
        assert self.stub is not None

        self.api = self
        self.manifest = Manifest(self.stub)
        self.user = UserProfile(self.stub)
        self.datasets = None

    def _get_default_headers(self):
        """ Returns default headers for Pennsieve. """
        return {
            "Content-Type": "application/json",
            "Accept": "application/json; charset=utf-8",
            "Authorization": "Bearer " + self.user.credentials["session_token"],
            "X-ORGANIZATION-ID": self.user.credentials["organization_id"],
        }

    def getUser(self):
        """ Returns current user.
        Return:
        -------
            user : str
                Current user credentials.
        """
        return self.user.whoami()

    def getManifests(self):
        """ Returns available manifest in form of a list

        Return:
        --------
            manifest : list
                A list storing all manifests.
        """
        return self.manifest.list()

    def getDatasets(self):
        """ Lists datasets for which the authenticated user has access to

        Return:
        --------
            datasets : dict
                a dictionary with user-defined names as keys and AWS ids as values
        """

        response = self.get("/datasets")
        self.datasets = dict(
            map(lambda x: (x["content"]["name"], x["content"]["id"]), response)
        )
        return self.datasets

    def useDataset(self, dataset_id):
        """ Specifies which dataset on the server will be used

        Parameters:
        --------
            dataset_id : string
                either dataset name or AWS-like dataset id of the dataset to which the changes will be applied
        """
        if self.datasets and dataset_id in self.datasets.keys():
            dataset_id = self.datasets[dataset_id]
        request = agent_pb2.UseDatasetRequest(dataset_id=dataset_id)
        return self.stub.UseDataset(request=request)

    def call(self, url, method, **kwargs):
        """ Calls get/post/put/delete endpoints directly on the server

        Parameters:
        -----------
        url : str
            address of the server to be called (e.g. api.pennsieve.io)
        method : str
            get, post, put or delete - an endpoint to be invoked
        kwargs : dict
            a dictionary storing additional information, e.g. json - request payload required for some of the enpoints (e.g. post)

        Raises:
        -------
            requests.exceptions.HTTPError : in case of http error
            Exception : in case of other error
        Return:
        --------
        String in JSON format with response from the server.

        """
        if url.startswith("/"):
            url = self.user.api_host + url
        if "headers" not in kwargs:
            headers = self._get_default_headers()
        else:
            headers = kwargs["headers"]
        try:
            if method.lower() == "get":
                response = requests.get(url=url, headers=headers, **kwargs)
            elif method.lower() == "post":
                response = requests.post(url=url, headers=headers, **kwargs)
            elif method.lower() == "put":
                response = requests.put(url=url, headers=headers, **kwargs)
            elif method.lower() == "delete":
                response = requests.delete(url=url, headers=headers, **kwargs)
            else:
                raise Exception("Not implemented")
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other excpetion occurred: {err}")
        else:
            return response.json()  # content.decode('utf-8'))

    def get(self, url, **kwargs):
        """Invokes GET endpoint on a server. Passing server name in url is optional.

        Parameters:
        -----------
        url : str
            the address of the server endpoint to be called (e.g. api.pennsieve.io/datasets). The name of the server can be ommitted.
        kwargs : dict
            a dictionary storing additional information

        Return:
        --------
        String in JSON format with response from the server.
        """
        return self.call(url, method="get", **kwargs)

    def post(self, url, json, **kwargs):
        """Invokes POST endpoint on a server. Passing server name in url is optional.

        Parameters:
        -----------
        url : str
            the address of the server endpoint to be called (e.g. api.pennsieve.io/datasets).
            The name of the server can be omitted.
        json : dict
            a request payload with parameters defined by a given endpoint
        kwargs : dict
            additional information

        Return:
        --------
        String in JSON format with response from the server.
        """
        return self.call(url, method="post", json=json, **kwargs)

    def put(self, url, json, **kwargs):
        """Invokes PUT endpoint on a server. Passing server name in url is optional.

        Parameters:
        -----------
        url : str
            the address of the server endpoint to be called (e.g. api.pennsieve.io/datasets).
            The name of the server can be omitted.
        json : dict
            a request payload with parameters defined by a given endpoint
        kwargs : dict
            additional information

        Return:
        --------
        String in JSON format with response from the server.
        """
        return self.call(url, method="put", json=json, **kwargs)

    def delete(self, url, **kwargs):
        """Invokes DELETE endpoint on a server. Passing server name in url is optional.

        Parameters:
        -----------
        url : str
            the address of the server endpoint to be called. The name of the server can be omitted.
        kwargs : dict
            additional information

        Return:
        --------
        String in JSON format with response from the server.
        """
        return self.call(url, method="delete", **kwargs)

    def subscribe(self, id):
        """ Creates a subscriber with id that would receive messages from the GO agent.
        Parameters:
        -----------
        id : int
            an identifier of a subscriber

        Return:
        -------
        response : str
            A response from the server
        """

        request = agent_pb2.SubscribeRequest(id=id)
        return self.stub.Subscribe(request=request)

    def unsubscribe(self, id):
        """ Unsubscribes a subscriber with identifier id from receiving messages from the GO agent.
        Parameters:
        -----------
        id : int
            an identifier of a subscriber

        Return:
        -------
        response : str
            A response from the server
        """

        request = agent_pb2.SubscribeRequest(id=id)
        return self.stub.Unsubscribe(request=request)
