"""
Usage:
    cli.py <doc_dir> [<out_dir>]

<doc_dir> - Directory of the docs.
<out_dir> - Output directory [Default: doc].
"""
import os
import sys

import ast
import yaml
import docopt

from components.function import Function
from components.klass import Klass
from components.module import Module
from components.toctree import ToCTree

PYTHON_EXT = '.py'
RST_EXT = '.rst'


def handle_cls(cls_node, cls):
    for elem in cls_node.body:
        if isinstance(elem, ast.FunctionDef):
            func_name = elem.name
            if func_name.startswith("_"):
                continue

            func_doc = ast.get_docstring(elem)
            fn = Function(func_name, func_doc, [arg.id for arg in elem.args.args], is_method=True)
            cls.add_component(fn)


def handle_class(mod_node, mod):
    for elem in mod_node.body:
        if isinstance(elem, ast.ClassDef):
            cls_name = elem.name
            cls_doc = ast.get_docstring(elem)
            cls = Klass(cls_name, cls_doc, [base.id for base in elem.bases])
            handle_cls(elem, cls)
            mod.add_component(cls)


def handle_file(path):
    with open(path) as module:
        node = ast.parse(module.read())

    doc = ast.get_docstring(node)

    mod = Module(os.path.basename(path), doc)

    handle_class(node, mod)

    return mod.content


def generate_api_ref(path, out_dir):
    sys.stdout.write(".")
    entities = os.listdir(path)
    current_folder = os.path.join(out_dir, path)
    if not os.path.exists(current_folder):
        os.makedirs(current_folder)

    config = {}
    files = []
    for entity in entities:
        current_path = os.path.join(path, entity)
        if os.path.isdir(current_path):
            files.append(generate_api_ref(current_path, out_dir))

    for entity in entities:
        current_path = os.path.join(path, entity)
        if os.path.isfile(current_path):
            if os.path.basename(current_path) == "doc.yml":
                with open(current_path) as config_file:
                    config = yaml.load(config_file)

            file_name, ext = os.path.splitext(os.path.basename(current_path))
            if ext != PYTHON_EXT or file_name.startswith("_"):
                continue

            with open(os.path.join(current_folder, "{}.rst".format(file_name)), "w") as doc_file:
                doc_file.write(handle_file(current_path))

            files.append(file_name)

    index_title = config.get("title", os.path.basename(path))
    index = Module(index_title, "")
    index.add_component(ToCTree(files, config.get("toctree", {})))

    with open(os.path.join(current_folder, "index.rst"), "w") as index_file:
        index_file.write(index.content)

    return os.path.join(os.path.basename(path), "index")


def make_doc(doc_dir, out_dir="doc", doc_files=[]):
    if out_dir is None:
        out_dir = "doc"

    api_ref = generate_api_ref(doc_dir, out_dir)
    config = {}
    config_file_path = os.path.join(doc_dir, "doc.yml")
    if os.path.exists(config_file_path):
        with open(config_file_path) as config_file:
            config = yaml.load(config_file)

    index_title = config.get("title", out_dir)
    index = Module(index_title, "")
    index.add_component(ToCTree(doc_files + [api_ref], config.get("toctree", {})))
    with open(os.path.join(out_dir, "index.rst"), "w") as index_file:
        index_file.write(index.content)


def main():
    args = docopt.docopt(__doc__)
    doc_dir = args["<doc_dir>"]
    out_dir = args["<out_dir>"]
    make_doc(doc_dir, out_dir)

if __name__ == '__main__':
    main()
