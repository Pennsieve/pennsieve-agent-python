"""
Copyright (c) 2022 Patryk Orzechowski | Wagenaar Lab | University of Pennsylvania
"""
from __future__ import annotations

import logging
import sys

import grpc
from tqdm.auto import tqdm

from .direct.client import AbstractClient, HttpApiClient
from .manifest import Manifest
from .protos import agent_pb2, agent_pb2_grpc
from .userProfile import UserProfile


# Set it up to get info messages:
# import logging
# logging.basicConfig()
# logging.root.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG)


class Pennsieve(AbstractClient):
    """The main class of Python Pennsieve agent

    Attributes:
    -----------
    api : object
        a singleton for backward compatibility
    manifest : object
        a manifest with files to be uploaded
    user : object
        class managing user credentials

    Methods:
    --------
    __init__()
        sets headers for GET/POST requests + by default connects to the Pennsieve Agent
    connect(...)
        establishes a connection to the Pennsieve Agent
    get_user()
        Returns current user.
    list_manifests()
        Returns all available manifest in form of a list.
    get_datasets(dataset_id)
        Returns available datasets in form of a dict.
    set_dataset(dataset_id)
        specifies which dataset on the server will be used
    use_dataset(dataset_id)
        same as set_dataset(dataset_id)
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
    agent_version()
        Returns information on Pennsieve Agent version
    stop()
        Stops the Pennsieve Agent

    """

    def __init__(
            self,
            connect=True,
            target="localhost:9000",
            profile_name=None,
    ):
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json; charset=utf-8",
        }
        self.stub = None
        self.api = self
        self.user = None
        self._datasets = None
        self.dataset = None
        self.manifest = None
        self.http_api: HttpApiClient | None = None
        if connect:
            self.connect(
                target=target,
                profile_name=profile_name,
            )

    def connect(
            self,
            target="localhost:9000",
            profile_name=None,
    ):
        """Initialization of Pennsieve Python agent

        Parameters:
        -----------
        target : str
            a socket with running GO agent
        profile name : str
            a profile name to use from config file

        """
        channel = grpc.insecure_channel(target)
        try:
            grpc.channel_ready_future(channel).result(timeout=100)
        except grpc.FutureTimeoutError:
            sys.exit("Error connecting to server")
        else:
            self.stub = agent_pb2_grpc.AgentStub(channel)
        assert self.stub is not None
        self.user = UserProfile(
            self.stub,
            profile_name=profile_name,
        )
        self.http_api = HttpApiClient.for_agent(api_host=self.user.current_user.api_host,
                                                api2_host=self.user.current_user.api2_host,
                                                stub=self.stub)

        self.manifest = Manifest(self.stub)
        print("Please set the dataset with use_dataset([name])")
        return self

    def get_user(self):
        """Returns current user.
        Return:
        -------
            user : str
                Current user credentials.
        """
        return self.user  # .whoami()

    def switch(self, profile_name):
        self._datasets = None
        self.dataset = None
        self.manifest.manifest = None
        self.user.switch(profile_name)
        self.http_api.set_base_urls(self.user.current_user.api_host, self.user.current_user.api2_host)

    def list_manifests(self):
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
        if self._datasets is None:
            response = self.get("/datasets")
            if isinstance(response, list) and len(response) > 0:
                self._datasets = dict(
                    map(
                        lambda x: (x["content"]["name"], x["content"]["id"])
                        if "content" in x.keys()
                           and "name" in x["content"].keys()
                           and "id" in x["content"].keys()
                        else None,
                        response,
                    )
                )
        return self._datasets

    def set_dataset(self, dataset_id):
        return self.use_dataset(dataset_id)

    def use_dataset(self, dataset_id):
        """Specifies which dataset on the server will be used

        Parameters:
        --------
            dataset_id : string
                dataset name or AWS-like dataset id to which the changes will be applied
        """
        self.get_datasets()
        if self._datasets and dataset_id in self._datasets.keys():
            self.dataset = self._datasets[dataset_id]
        elif dataset_id in self._datasets.values():
            self.dataset = dataset_id
        assert self.dataset is not None
        request = agent_pb2.UseDatasetRequest(dataset_id=self.dataset)
        return self.stub.UseDataset(request=request)

    def get(self, url, **kwargs):
        return self.http_api.get(url, **kwargs)

    def post(self, url, json, **kwargs):
        return self.http_api.post(url, json=json, **kwargs)

    def put(self, url, json, **kwargs):
        return self.http_api.put(url, json=json, **kwargs)

    def delete(self, url, **kwargs):
        return self.http_api.delete(url, **kwargs)

    def subscribe(self, subscriber_id, show_progress=False, callback=None):
        """Creates a subscriber with id that would receive messages from the GO agent.
        Parameters:
        -----------
        subscriber_id : int
            an identifier of a subscriber
        show_progress : bool
            switches on/off progress bars from tqdm
        callback : function
            a function to capture events from Pennsieve Agent
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
            if callback is not None:
                callback(events_dict)

            logging.debug(str(events_dict))
            # decrypt all fields of the message

            if events_dict["type"] == 0:  # general info
                logging.info(str(events_dict["event_info"].details))
            elif events_dict["type"] == 1:  # upload status: file_id, total, current, worker_id
                logging.debug("UPLOAD STATUS: " + str(events_dict["upload_status"]))
                file_id = events_dict["upload_status"].file_id
                total = events_dict["upload_status"].total
                current = events_dict["upload_status"].current
                worker_id = events_dict["upload_status"].worker_id
                status = events_dict["upload_status"].status

                if show_progress and total > 0:
                    pbar = tqdm(
                        desc=file_id.split("/")[-1],
                        total=total,
                        unit="B",
                        unit_scale=True,
                        unit_divisor=1024,
                        position=0,
                        leave=True,
                    )
                    pbar.n = current
                    pbar.update()
                elif total > 0:
                    logging.info(
                        f"Worker: {worker_id} File: {file_id}  Progress: {current}/{total}"
                    )
                if status == 2:  # status: COMPLETE
                    logging.info("Upload completed.")

    def unsubscribe(self, subscriber_id):
        """Unsubscribes a subscriber with identifier id from receiving messages from the GO agent.
        Parameters:
        -----------
        subscriber_id : int
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
