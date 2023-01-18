import os

import pytest

from pennsieve2.direct.config import Config


def test_no_error_for_unaccessed_missing_config_file():
    Config(config_file='/non/existent/config.ini')


def test_no_config_file():
    with pytest.raises(FileNotFoundError):
        config = Config(config_file='/non/existent/config.ini')
        config.get('key')


def test_config_file(test_resources_dir):
    config_file = os.path.join(test_resources_dir, 'config.ini')
    config = Config(config_file=config_file)
    assert config.get('api_token') == 'org-A-non-prod-token'
    assert config.get('api_host') == 'https://example.com/non-prod/api'


def test_profile_name(test_resources_dir):
    config_file = os.path.join(test_resources_dir, 'config.ini')
    config = Config(config_file=config_file, profile_name='org-B')
    assert config.get('api_token') == 'org-B-token'
    assert config.get('api_host') is None
