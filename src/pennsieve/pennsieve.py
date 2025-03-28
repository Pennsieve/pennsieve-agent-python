"""
Copyright (c) 2022 Patryk Orzechowski | Wagenaar Lab | University of Pennsylvania
"""
from __future__ import annotations

import logging
import sys

import grpc
from tqdm.auto import tqdm

from .direct import API2_HOST_DEFAULT, API_HOST_DEFAULT
from .direct.client import AbstractClient, BaseHttpApiClient, HttpApiClient
from .manifest import Manifest
from .protos import agent_pb2, agent_pb2_grpc
from .protos.agent_pb2_grpc import AgentStub
from .session import APISession, APISessionProvider
from .timeSeries import TimeSeries
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
        connect: bool = True,
        target: str = "localhost:9000",
        connect_timeout_seconds: float | None = 1,
        profile_name: str | None = None,
        http_api_client: BaseHttpApiClient | None = None,
    ):
        """Creates a Pennsieve Python client

        Parameters:
        -----------
        connect : bool
            connect to Pennsieve Agent if true (default is true)
        target : str
            address of the Pennsieve Agent (default is 'localhost:9000' which is the Agent's default address)
        connect_timeout_seconds: float | None
            number of seconds to wait for the initial connection to the Agent
            (default is 100 seconds, None means no timeout)
        profile name : str
            a profile name to use from config file (default is None which will use the currently active profile)
        http_api_client : BaseHttpApiClient
            allows override of the default client. The default client depends on the value of connect.
            If connect is True, the default client uses the Agent to get authentication information.
            If connect is False, the default client does no authentication and can only be used to
            call public Discover API endpoints. If connect is subsequently called, this client
            will be replaced by one that uses the Agent as in the 'connect=True' case.

        """

        self.stub = None
        self.api = self
        self.user = None
        self._datasets = None
        self.dataset = None
        self.manifest = None
        self.timeseries = None
        if http_api_client is None:
            self.http_api = self.build_no_auth_http_api_client()
        else:
            self.http_api = http_api_client
        if connect:
            self.connect(
                target=target,
                profile_name=profile_name,
                connect_timeout_seconds=connect_timeout_seconds,
            )

    def connect(
        self,
        target: str = "localhost:9000",
        connect_timeout_seconds: float | None = 1,
        profile_name: str | None = None,
    ):
        """Initialization of Pennsieve Python agent

        Parameters:
        -----------
        target : str
            a socket with running GO agent
        connect_timeout_seconds: float | None
                number of seconds to wait for the initial connection to the Agent
                (default is 100 seconds, None means no timeout)
        profile name : str
            a profile name to use from config file

        """
        channel = grpc.insecure_channel(target)
        try:
            grpc.channel_ready_future(channel).result(timeout=connect_timeout_seconds)
        except grpc.FutureTimeoutError:
            print("""Error connecting to the Pennsieve Agent
            
Please start the Pennsieve agent in the terminal using 'pennsieve agent', or
initialize the Pennsieve Python Client without Agent support by providing
the 'connect=false' parameter.
            """)
            return
        else:
            self.stub = agent_pb2_grpc.AgentStub(channel)
        assert self.stub is not None
        self.user = UserProfile(
            self.stub,
            profile_name=profile_name,
        )
        self.http_api = self.build_agent_http_api_client(
            api_host=self.user.current_user.api_host,
            api2_host=self.user.current_user.api2_host,
            stub=self.stub,
        )

        self.manifest = Manifest(self.stub)
        self.timeseries = TimeSeries(self.stub)
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
        self.http_api.reset_base_urls(
            self.user.current_user.api_host, self.user.current_user.api2_host
        )

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

    @staticmethod
    def build_agent_http_api_client(api_host, api2_host, stub: AgentStub) -> HttpApiClient:
        return HttpApiClient(api_host, api2_host, AgentAPISessionProvider(stub))

    @staticmethod
    def build_no_auth_http_api_client() -> BaseHttpApiClient:
        return BaseHttpApiClient(API_HOST_DEFAULT, API2_HOST_DEFAULT)


class AgentAPISessionProvider(APISessionProvider):
    def __init__(self, stub: AgentStub):
        super().__init__()
        self._stub = stub

    def new_api_session(self) -> APISession:
        request = agent_pb2.ReAuthenticateRequest()
        response = self._stub.ReAuthenticate(request=request)
        return APISession(
            token=response.session_token,
            expiration=response.token_expire,
            organization_node_id=response.organization_id,
        )
