from __future__ import absolute_import
import os
from collections import namedtuple

import yaml


DOC_YML = "doc.yml"


def fetch_folder_config(path):
    """Fetch config file of folder.

    Args:
        path (str): path to the wanted folder of the config.

    Returns:
        dict. the loaded config file.
    """
    config = {}
    config_path = os.path.join(path, DOC_YML)
    if os.path.exists(config_path):
        with open(config_path) as config_file:
            config = yaml.load(config_file)

    return config


def get_base_name(path):
    """Get the path's basename.

    Args:
        path (str): the path to extract the basename from.

    Returns:
        str. the basename of the given path.
    """
    base = os.path.basename(os.path.normpath(path))
    if base == "":
        base = path
    return base.strip("/")


File = namedtuple("File", ["module", "mount_path"])
