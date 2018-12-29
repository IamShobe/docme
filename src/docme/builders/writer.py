from __future__ import absolute_import
import os

from six import print_

from .structures import make_module
from .components.module import Module
from .components.toctree import ToCTree
from .utils import File, get_base_name, fetch_folder_config


INDEX = "index"
INDEX_FILE = "index.rst"
PYTHON_EXT = '.py'
RST_EXT = '.rst'


class DocWriter(object):
    DEFAULT_DOC_DIR = "doc"

    def __init__(self, to_doc_dirs, external_docs=None):
        self.to_doc_dirs = to_doc_dirs
        self.external_docs = external_docs if external_docs is not None else []

    @classmethod
    def generate_path_modules(cls, path):
        """Generate given path module objects - only py files are watched.

        Args:
            path (str): the path to generate doc from.

        Returns:
            list. list of File objects.
        """
        files = []
        for entity in os.listdir(path):
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

    @classmethod
    def create_rst_files(cls, current_folder, files):
        """Make rst files from the files parameter.

        Note:
            Creates missing directories.

        Args:
            current_folder (str): path of the current folder to write the doc into.
            files (list): list of File objects - contains the modules to write into the folder.
        """
        if not os.path.exists(current_folder):
            os.makedirs(current_folder)

        for file in files:
            file_path = os.path.join(current_folder, "{}.rst".format(file.mount_path))
            print_("Writing file {!r}".format(file_path))
            with open(file_path, "w") as doc_file:
                doc_file.write(file.module.content)

    @classmethod
    def make_index(cls, path, out_dir, default_title, config, files):
        """Generate index file to the given path.

        Args:
            path (str): the path of the related folder to make the index of.
            out_dir (str): the path of the out dir to make the index to.
            default_title (str): incase there is no doc.yml file in the folder, this title will be chosen.
            config (dict): doc.yml file the configures the doc output.
            files (list): list of file mount points to add to current index.

        Returns:
            File. namedtuple contains `module` which is Module object that has the doc in it,
                and `mount_path` where to mount the current doc relative to `path` root.
        """
        index_title = config.get("title", default_title)
        index = Module(index_title, "", path)
        index.add_component(ToCTree(files, config.get("toctree", {})))

        with open(os.path.join(out_dir, INDEX_FILE), "w") as index_file:
            index_file.write(index.content)

        base = get_base_name(out_dir)

        return File(module=index, mount_path=os.path.join(base, INDEX))

    def write_files(self, path, files, out_dir, default_title, config):
        """Write the given files into the given out_dir and create index of them.

        Args:
            path (str): the path of the related folder to make the index of.
            out_dir (str): the path of the out dir to make the index to and doc files.
            default_title (str): incase there is no doc.yml file in the folder, this title will be chosen.
            config (dict): doc.yml file the configures the doc output.
            files (list): list of File objects to add to write.

        Returns:
            File. namedtuple contains `module` which is Module object that has the doc in it,
                and `mount_path` where to mount the current doc relative to `path` root.
        """
        files = [file for file in files if file is not None]
        if len(files) == 0:
            print_("Skipping {!r} no files found!".format(out_dir))
            return

        self.create_rst_files(out_dir, files)
        return self.make_index(path, out_dir, default_title=default_title, config=config,
                               files=[file.mount_path for file in files])

    def generate_root_path_reference(self, root, out_dir):
        """Generate given path sub modules - only folders are watched.

        Note:
            this function calls in recursion to `generate_root_path_reference` method.

        Args:
            root (str): the path to generate doc from.
            out_dir (str): the path to generate doc into.

        Returns:
            list. list of File objects.
        """
        def generate_nested_modules(path):
            current_files = []
            for entity in os.listdir(path):
                current_path = os.path.join(path, entity)
                if os.path.isdir(current_path):
                    current_files.append(self.generate_root_path_reference(current_path, out_dir))

            return current_files

        print_("Scanning folder {!r}".format(root))
        files = generate_nested_modules(root)
        files.extend(self.generate_path_modules(root))

        current_folder = os.path.join(out_dir, root)
        config = fetch_folder_config(current_folder)
        print_("Creating folder content {!r}".format(current_folder))
        return self.write_files(root, files, current_folder,
                                default_title=get_base_name(root), config=config)

    def generate_full_api_reference(self, out_dir):
        """Generate full api reference from the given doc dirs.

        Args:
            out_dir (str): the path to generate doc into.

        Returns:
            list. list of File objects.
        """
        files = []
        out_dir = os.path.join(out_dir, "api_reference")
        for path in self.to_doc_dirs:
            files.append(self.generate_root_path_reference(path, out_dir))

        return self.write_files("<root>", files, out_dir,
                                default_title="Api Reference", config={"title": "Api Reference"})

    def generate(self, out_dir):
        """Generate full doc.

        Args:
            out_dir (str): the path to generate doc into.

        Returns:
            list. list of File objects.
        """
        out_dir = out_dir if out_dir is not None else self.DEFAULT_DOC_DIR

        api_ref = self.generate_full_api_reference(out_dir)
        config = fetch_folder_config(".")

        self.make_index("<root>", out_dir, default_title=out_dir, config=config,
                        files=self.external_docs + [api_ref.mount_path])
        print_("Done!")
