"""
Copyright (c) 2022 Patryk Orzechowski | Wagenaar Lab | University of Pennsylvania
"""

import sys
import traceback
import grpc
import requests

from tqdm.auto import tqdm
from .protos import agent_pb2_grpc, agent_pb2
from .manifest import Manifest
from .userProfile import UserProfile


class Pennsieve:
    """The main class of Python Pennsieve agent

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
    get_user()
        Returns current user.
    get_manifests()
        Returns available manifest in form of a list.
    get_datasets()
        Returns available datasets in form of a list.
    use_dataset(dataset_id)
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
        """Initialization of Pennsieve Python agent

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
        self.datasets = self.get_datasets()
        self.dataset = None

    def _get_default_headers(self):
        """Returns default headers for Pennsieve."""
        return {
            "Content-Type": "application/json",
            "Accept": "application/json; charset=utf-8",
            "Authorization": "Bearer " + self.user.credentials["session_token"],
            "X-ORGANIZATION-ID": self.user.credentials["organization_id"],
        }

    def get_user(self):
        """Returns current user.
        Return:
        -------
            user : str
                Current user credentials.
        """
        return self.user.whoami()

    def get_manifests(self):
        """Returns available manifest in form of a list

        Return:
        --------
            manifest : list
                A list storing all manifests.
        """
        return self.manifest.list_manifests()

    def get_datasets(self):
        """Lists datasets for which the authenticated user has access to

        Return:
        --------
            datasets : dict
                a dictionary with user-defined names as keys and AWS ids as values
        """

        response = self.get("/datasets")
        self.dataset = None
        if isinstance(response, list) and len(response) > 0:
            self.datasets = dict(
                map(
                    lambda x: (x["content"]["name"], x["content"]["id"])
                    if "content" in x.keys()
                    and "name" in x["content"].keys()
                    and "id" in x["content"].keys()
                    else None,
                    response,
                )
            )
        return self.datasets

    def use_dataset(self, dataset_id):
        """Specifies which dataset on the server will be used

        Parameters:
        --------
            dataset_id : string
                dataset name or AWS-like dataset id to which the changes will be applied
        """
        if self.datasets and dataset_id in self.datasets.keys():
            self.dataset = self.datasets[dataset_id]
        assert self.dataset is not None
        request = agent_pb2.UseDatasetRequest(dataset_id=self.dataset)
        return self.stub.UseDataset(request=request)

    def call(self, url, method, **kwargs):
        """Calls get/post/put/delete endpoints directly on the server

        Parameters:
        -----------
        url : str
            address of the server to be called (e.g. api.pennsieve.io)
        method : str
            get, post, put or delete - an endpoint to be invoked
        kwargs : dict
            a dictionary storing additional information, e.g. json
            contains request payload required for some of the enpoints (e.g. post)

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
                raise NotImplementedError("Not implemented")
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except:  # pylint: disable=W0702
            traceback.print_exc()

        return response.json()  # content.decode('utf-8'))

    def get(self, url, **kwargs):
        """Invokes GET endpoint on a server. Passing server name in url is optional.

        Parameters:
        -----------
        url : str
            the address of the server endpoint to be called (e.g. api.pennsieve.io/datasets).
            The name of the server can be ommitted.
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

    def subscribe(self, subscriber_id):
        """Creates a subscriber with id that would receive messages from the GO agent.
        Parameters:
        -----------
        id : int
            an identifier of a subscriber

        Return:
        -------
        response : str
            A response from the server
        """

        request = agent_pb2.SubscribeRequest(id=subscriber_id)
        for response in self.stub.Subscribe(request=request):
            key_list = response.DESCRIPTOR.fields_by_name.keys()
            events_dict = {}
            for key in key_list:
                events_dict[key] = getattr(response, key)
            # decrypt all fields of the message
            # print(str(d)) #debug
            if events_dict["type"] == 0:  # general info
                print(str(events_dict["event_info"].details))
            elif events_dict["type"] == 1:  # upload status: file_id, total, current, worker_id
                file_id = events_dict["upload_status"].file_id
                total = events_dict["upload_status"].total
                current = events_dict["upload_status"].current
                worker_id = events_dict["upload_status"].worker_id

                pbar = tqdm(
                    desc=file_id.split("/")[-1],
                    total=total,
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                    position=0,
                    leave=True,
                )
                #                   for i in tqdm(worker_id, position=0, leave=True):
                pbar.n = current
                pbar.update()

    #                pbar = tqdm(
    #                pbar.update()
    #                pbar.refresh()

    #            elif events_dict['type'] == 3:  #sync status
    #                sync_status   = events_dict['sync_status'].status
    #                total         = events_dict['sync_status'].total
    #                if sync_status == 2:
    #                    print(f'Upload complete. Uploaded {total} file(s).')
    #                    return

    def unsubscribe(self, subscriber_id):
        """Unsubscribes a subscriber with identifier id from receiving messages from the GO agent.
        Parameters:
        -----------
        id : int
            an identifier of a subscriber

        Return:
        -------
        response : str
            A response from the server
        """

        request = agent_pb2.SubscribeRequest(id=subscriber_id)
        return self.stub.Unsubscribe(request=request)

    def agent_version(self):
        """Returns agent and python client version

        Return:
        -------
        version : str
            Version of Pennsieve Python agent, i.e. __version__

        """
        request = agent_pb2.VersionRequest()
        version_number = self.stub.Version(request=request).version
        log_level = self.stub.Version(request=request).log_level
        print(f"Pennsieve Agent version: {version_number}, log level: {log_level}")

    def stop(self):
        """Stops the agent"""
        request = agent_pb2.StopRequest()
        return self.stub.Stop(request=request)
