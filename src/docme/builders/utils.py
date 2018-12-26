import os
from collections import namedtuple

import yaml


DOC_YML = "doc.yml"


def fetch_folder_config(path):
    config = {}
    if os.path.exists(os.path.join(path, DOC_YML)):
        with open(path) as config_file:
            config = yaml.load(config_file)

    return config


def get_base_name(path):
    base = os.path.basename(os.path.normpath(path))
    if base == "":
        base = path
    return base.strip("/")


File = namedtuple("File", ["module", "mount_path"])
