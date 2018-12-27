import ast
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


def fetch_constant(node):
    if isinstance(node, ast.Assign):
        if len(node.targets) == 1:
            target = node.targets[0]
            value = node.value.n
            return target, value


File = namedtuple("File", ["module", "mount_path"])
