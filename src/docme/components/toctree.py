from docme.components.utils import indent
from docme.components.base_component import BaseComponent


class ToCTree(BaseComponent):
    def __init__(self, files, properties):
        super(ToCTree, self).__init__(doc=None)
        self.properties = properties
        self.files = files

    @property
    def props(self):
        string = "\n".join([":{key}: {value}".format(key=key, value=value)
                            for key, value in self.properties.items()])
        return string + "\n" if string else ""

    @property
    def file_names(self):
        return [file.mount_path for file in self.files]

    @property
    def content(self):
        return """\
.. toctree::
{properties}
{files}
""".format(properties=indent(self.props), files=indent("\n".join(self.file_names)))
