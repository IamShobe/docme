from utils import indent
from base_component import BaseComponent


class ToCTree(BaseComponent):
    def __init__(self, files, properties):
        super(ToCTree, self).__init__()
        self.properties = properties
        self.files = files

    @property
    def content(self):
        return """\
.. toctree::
{properties}

{files}
""".format(properties=indent("\n".join([":{key}: {value}".format(key=key, value=value)
                                        for key, value in self.properties.items()])),
           files=indent("\n".join(self.files)))
