"""
pennsieve2.direct.config

Reading Pennsieve configuration file

"""
import configparser
import os
from pathlib import Path


class Config:
    """
    Lazily reads configuration file the first time a client requests a value.
    """

    _GLOBAL_SECTION = "global"

    def __init__(self, config_file=None, profile_name=None):
        self.config_file = (
            os.path.join(Path.home(), ".pennsieve", "config.ini")
            if config_file is None
            else config_file
        )
        self.profile_name = profile_name
        self.profile_section = None

    def get(self, key):
        if self.profile_section is None:
            self.profile_section = self._resolve_profile()
        return self.profile_section.get(key)

    def _parse_config(self):
        config = configparser.ConfigParser(
            default_section="__pennsieve-config-has-no-default-section__"
        )
        config.read_file(open(self.config_file))
        return config

    def _resolve_profile(self):
        """Reads config file and returns the correct section for the requested profile if possible"""

        full_config = self._parse_config()
        if self.profile_name is not None:
            if self.profile_name not in full_config:
                raise KeyError(f"{self.config_file} does not contain section {self.profile_name}")
            return full_config[self.profile_name]

        if (
            self._GLOBAL_SECTION in full_config
            and "default_profile" in full_config[self._GLOBAL_SECTION]
        ):
            default_profile_name = full_config[self._GLOBAL_SECTION]["default_profile"]
            if default_profile_name not in full_config:
                raise KeyError(
                    f"{self.config_file} does not contain default profile {default_profile_name}"
                )
            return full_config[default_profile_name]

        raise RuntimeError(
            f"No profile requested and {self.config_file} does not contain a default_profile "
        )
