import os
from unittest.mock import patch

from pennsieve.direct import (API_HOST_DEFAULT, new_client,
                               new_client_from_config)
from pennsieve.direct.provider import PythonAPISessionProvider


def test_constructor_params():
    api_key = "my-key"
    api_secret = "my-secret"
    api_host = "https://example.com/api"
    client = PythonAPISessionProvider(api_key=api_key, api_secret=api_secret, api_host=api_host)
    assert client.api_key == api_key
    assert client.api_secret == api_secret
    assert client.api_host == api_host


@patch.dict(
    os.environ,
    {
        "PENNSIEVE_API_KEY": "env-var-key",
        "PENNSIEVE_API_SECRET": "env-var-secret",
        "PENNSIEVE_API_HOST": "https://example.com/env/api",
    },
)
def test_env_variables():
    client = new_client()
    provider: PythonAPISessionProvider = client._api_session_provider
    assert provider.api_key == "env-var-key"
    assert provider.api_secret == "env-var-secret"
    assert client.api_host == "https://example.com/env/api"


def test_config_file(test_resources_dir):
    config_file = os.path.join(test_resources_dir, "config.ini")
    client = new_client_from_config(config_file=config_file)
    provider: PythonAPISessionProvider = client._api_session_provider
    assert provider.api_key == "org-A-non-prod-token"
    assert provider.api_secret == "org-A-non-prod-secret"
    assert client.api_host == "https://example.com/non-prod/api"


def test_config_profile(test_resources_dir):
    config_file = os.path.join(test_resources_dir, "config.ini")
    client = new_client_from_config(config_file=config_file, profile_name="org-B")
    provider: PythonAPISessionProvider = client._api_session_provider
    assert provider.api_key == "org-B-token"
    assert provider.api_secret == "org-B-secret"
    assert client.api_host == API_HOST_DEFAULT
