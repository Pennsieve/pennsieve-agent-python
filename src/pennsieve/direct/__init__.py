import os

import requests

from pennsieve.direct.client import HttpApiClient
from pennsieve.direct.provider import PythonAPISessionProvider

API_HOST_DEFAULT = "https://api.pennsieve.io"

API2_HOST_DEFAULT = "https://api2.pennsieve.io"


def new_client(api_key=None, api_secret=None, api_host=None, api2_host=None) -> HttpApiClient:
    def _resolve_param(param, env_var_name, default_value=None):
        if param is not None:
            return param
        env_value = os.environ.get(env_var_name)
        if env_value is not None:
            return env_value
        return default_value

    api_key = _resolve_param(api_key, "PENNSIEVE_API_KEY")
    api_secret = _resolve_param(api_secret, "PENNSIEVE_API_SECRET")
    api_host = _resolve_param(api_host, "PENNSIEVE_API_HOST", API_HOST_DEFAULT)
    api2_host = _resolve_param(api2_host, "PENNSIEVE_API2_HOST", API2_HOST_DEFAULT)
    return _build_client(api_key, api_secret, api_host, api2_host)


def new_client_from_config(config_file=None, profile_name=None) -> HttpApiClient:
    def _resolve_param_from_config(parsed_config, config_key, default_value=None):
        config_value = parsed_config.get(config_key)
        if config_value is not None:
            return config_value
        return default_value

    from pennsieve.direct.config import Config

    config = Config(config_file, profile_name)
    api_key = _resolve_param_from_config(config, "api_token")
    api_secret = _resolve_param_from_config(config, "api_secret")
    api_host = _resolve_param_from_config(config, "api_host", API_HOST_DEFAULT)
    api2_host = _resolve_param_from_config(config, "api2_host", API2_HOST_DEFAULT)
    return _build_client(api_key, api_secret, api_host, api2_host)


def _build_client(api_key, api_secret, api_host, api2_host):
    http_session = requests.Session()
    api_session_provider = PythonAPISessionProvider(
        api_key=api_key, api_secret=api_secret, api_host=api_host, http_session=http_session
    )
    return HttpApiClient(
        api_host=api_host,
        api2_host=api2_host,
        api_session_provider=api_session_provider,
        http_session=http_session,
    )