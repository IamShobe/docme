from __future__ import absolute_import
from .utils import indent
from .base_component import BaseComponent


class ToCTree(BaseComponent):
    """This class represents toctree of rst format."""
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
    def content(self):
        return """\
.. toctree::
{properties}
{files}
""".format(properties=indent(self.props), files=indent("\n".join(self.files)))
