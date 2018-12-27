"""
Usage:
    cli.py <doc_dir>... [<out_dir>]

<doc_dir> - Directory of the docs.
<out_dir> - Output directory [Default: doc].
"""
import os
import sys
import argparse

from docme.components.module import Module
from docme.components.toctree import ToCTree
from docme.builders.components import make_module
from docme.builders.utils import fetch_folder_config, get_base_name, File

INDEX = "index"

INDEX_FILE = "index.rst"

PYTHON_EXT = '.py'
RST_EXT = '.rst'


def get_sub_indexes(path, out_dir, folder_entities):
    files = []
    for entity in folder_entities:
        current_path = os.path.join(path, entity)
        if os.path.isdir(current_path):
            files.append(generate_api_ref(current_path, out_dir))

    return files


def get_path_doc(path, folder_entities):
    files = []
    for entity in folder_entities:
        current_path = os.path.join(path, entity)
        if os.path.isfile(current_path):
            file_name, ext = os.path.splitext(os.path.basename(current_path))
            if ext != PYTHON_EXT or file_name.startswith("_"):
                continue

            mod = make_module(current_path)
            if len(mod.sub_components) == 0:
                continue

            files.append(File(module=mod, mount_path=file_name))

    return files


def create_rst_files(current_folder, files):
    if not os.path.exists(current_folder):
        os.makedirs(current_folder)
    for file in files:
        with open(os.path.join(current_folder, "{}.rst".format(file.mount_path)), "w") as doc_file:
            doc_file.write(file.module.content)


def make_index(path, current_folder, default_title, config, files):
    index_title = config.get("title", default_title)
    index = Module(index_title, "", path)
    index.add_component(ToCTree(files, config.get("toctree", {})))

    with open(os.path.join(current_folder, INDEX_FILE), "w") as index_file:
        index_file.write(index.content)

    base = get_base_name(current_folder)

    return File(module=index, mount_path=os.path.join(base, INDEX))


def create_files(path, files, out_dir, title, config):
    files = [file for file in files if file is not None]
    if len(files) == 0:
        print "Skipping {!r} no files found!".format(out_dir)
        return
    create_rst_files(out_dir, files)
    return make_index(path, out_dir, default_title=title, config=config, files=[file.mount_path for file in files])


def generate_api_ref(path, out_dir):
    sys.stdout.write(".")
    folder_entities = os.listdir(path)

    files = get_sub_indexes(path, out_dir, folder_entities)
    files.extend(get_path_doc(path, folder_entities))

    current_folder = os.path.join(out_dir, path)
    config = fetch_folder_config(current_folder)

    return create_files(path, files, current_folder, title=get_base_name(path), config=config)


def api_reference(out_dir, paths):
    files = []
    out_dir = os.path.join(out_dir, "api_reference")

    for path in paths:
        files.append(generate_api_ref(path, out_dir))

    return create_files("<root>", files, out_dir, title="Api Reference", config={"title": "Api Reference"})


def make_doc(doc_dirs, out_dir="doc", doc_files=None):
    if doc_files is None:
        doc_files = []

    if out_dir is None:
        out_dir = "doc"

    api_ref = api_reference(out_dir, doc_dirs)
    config = fetch_folder_config(".")
    make_index("<root>", out_dir, default_title=out_dir, config=config,
               files=doc_files + [api_ref.mount_path])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('doc_dirs', type=str, nargs='+',
                        help='Directories of the docs')
    parser.add_argument('out_dir', type=str)
    parser.add_argument('--extra-doc', type=str, nargs='+')
    args = parser.parse_args()
    make_doc(args.doc_dirs, args.out_dir, args.extra_doc)

if __name__ == '__main__':
    main()
