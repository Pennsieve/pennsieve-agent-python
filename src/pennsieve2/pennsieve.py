"""
Copyright (c) 2022 Patryk Orzechowski | Wagenaar Lab | University of Pennsylvania
"""

import logging
import sys
import traceback

import grpc
import requests
from tqdm.auto import tqdm

from .manifest import Manifest
from .protos import agent_pb2, agent_pb2_grpc
from .userProfile import UserProfile

# Set it up to get info messages:
# import logging
# logging.basicConfig()
# logging.root.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG)


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
    __init__()
        sets headers for GET/POST requests + by default connects to the Pennsieve Agent
    connect(...)
        establishes a connection to the Pennsieve Agent
    get_user()
        Returns current user.
    list_manifests()
        Returns all available manifest in form of a list.
    get_datasets(dataset_id)
        Returns available datasets in form of a list.
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
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json; charset=utf-8",
        }
        if connect:
            self.connect(
                target=target,
                api_host=api_host,
                api_port=api_port,
                api_key=api_key,
                api_secret=api_secret,
                bucket=bucket,
                chunk_size=chunk_size,
                n_workers=n_workers,
                config_file=config_file,
                profile_name=profile_name,
            )

    def connect(
        self,
        target="localhost:9000",
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
        """Initialization of Pennsieve Python agent

        Parameters:
        -----------
        target : str
            a socket with running GO agent
        api_host : str
            a host to connect to
        api_port : str
            a port to connect to
        api_key, api_secret, bucket, chunk_size, n_workers : str
            currently not used
        config file : str
            a path to ~/.pennsieve/config.ini file
        profile name : str
            a profile name to use from config file

        """
        if api_host is not None and api_port is not None:
            target = f"{api_host}:{api_port}"
        channel = grpc.insecure_channel(target)
        try:
            grpc.channel_ready_future(channel).result(timeout=100)
        except grpc.FutureTimeoutError:
            sys.exit("Error connecting to server")
        else:
            self.stub = agent_pb2_grpc.AgentStub(channel)
        assert self.stub is not None

        self.api = self
        self.user = UserProfile(
            self.stub,
            api_host=api_host,
            api_port=api_port,
            api_key=api_key,
            api_secret=api_secret,
            bucket=bucket,
            chunk_size=chunk_size,
            n_workers=n_workers,
            config_file=config_file,
            profile_name=profile_name,
        )
        if self.user.credentials is not None:
            self.headers.update(
                {
                    "Authorization": "Bearer " + self.user.credentials["session_token"],
                    "X-ORGANIZATION-ID": self.user.credentials["organization_id"],
                }
            )
        self.datasets = self.get_datasets()
        self.manifest = Manifest(self.stub)
        print("Please set the dataset with use_dataset([name])")
        return self

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
        return self.user  # .whoami()

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
        if self.datasets and dataset_id in self.datasets.keys():
            self.dataset = self.datasets[dataset_id]
        elif dataset_id in self.datasets.values():
            self.dataset = dataset_id
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
            kwargs["headers"] = self.headers
        try:
            logging.debug(str(kwargs))
            if method.lower() == "get":
                response = requests.get(url=url, **kwargs)
            elif method.lower() == "post":
                response = requests.post(url=url, **kwargs)
            elif method.lower() == "put":
                response = requests.put(url=url, **kwargs)
            elif method.lower() == "delete":
                response = requests.delete(url=url, **kwargs)
            else:
                raise NotImplementedError("Not implemented")
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
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

        Example:
        --------
        p=Pennsieve()
        p.get('https://api.pennsieve.io/discover/datasets', params={'limit':20})

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
