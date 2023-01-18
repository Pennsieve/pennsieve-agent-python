import logging
from abc import ABC, abstractmethod

import requests
import traceback

from pennsieve2.session import APISessionProvider, APISession

logger = logging.getLogger(__name__)


class AbstractClient(ABC):
    @abstractmethod
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
        pass

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass


class HttpApiClient(AbstractClient):

    def __init__(self, api_host: str, api2_host: str, api_session_provider: APISessionProvider,
                 http_session: requests.Session = None):
        self.api_host = api_host
        self.api2_host = api2_host
        self._api_session_provider = api_session_provider
        self._http_session = requests.Session() if http_session is None else http_session

    def get(self, url, **kwargs):
        return self._call(url, method="get", **kwargs)

    def post(self, url, json, **kwargs):
        return self._call(url, method="post", json=json, **kwargs)

    def put(self, url, json, **kwargs):
        return self._call(url, method="put", json=json, **kwargs)

    def delete(self, url, **kwargs):
        return self._call(url, method="delete", **kwargs)

    def reset_base_urls(self, api_host, api2_host):
        if self._api_session_provider.is_switchable():
            self.api_host = api_host
            self.api2_host = api2_host
            self._api_session_provider.clear_session()
        else:
            raise RuntimeError(f'cannot switch profile of APISessionProvider {type(self._api_session_provider)}')

    def close(self):
        self._http_session.close()

    def _get_default_headers(self):
        """Returns default headers for Pennsieve."""
        api_session: APISession = self._api_session_provider.get_api_session()
        return {
            "Content-Type": "application/json",
            "Accept": "application/json; charset=utf-8",
            "Authorization": "Bearer " + api_session.token,
            "X-ORGANIZATION-ID": api_session.organization_node_id,
        }

    def _call(self, url, method, **kwargs):
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
            url = self.api_host + url

        headers = self._get_default_headers()
        # Let user add additional headers or override
        if "headers" in kwargs:
            headers.update(kwargs["headers"])
        kwargs["headers"] = headers

        try:
            logger.debug(str(kwargs))
            if method.lower() == "get":
                response = self._http_session.get(url=url, **kwargs)
            elif method.lower() == "post":
                response = self._http_session.post(url=url, **kwargs)
            elif method.lower() == "put":
                response = self._http_session.put(url=url, **kwargs)
            elif method.lower() == "delete":
                response = self._http_session.delete(url=url, **kwargs)
            else:
                raise NotImplementedError("Not implemented")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
        except:  # pylint: disable=W0702
            traceback.print_exc()
