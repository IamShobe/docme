from __future__ import absolute_import
from property_manager import cached_property

from .utils import indent
from .base_component import BaseComponent


class Function(BaseComponent):
    """This class represents Function type of rst format."""
    def __init__(self, name, doc, args, is_method=False, path=""):
        super(Function, self).__init__(doc)
        self.name = name
        self.args = args
        self.is_method = is_method
        self.path = path + "." + self.name

    @cached_property
    def doc(self):
        doc = super(Function, self).doc
        return "\n{}\n\n".format(indent(doc, count=2)) if len(doc.strip()) > 0 else ""

    @property
    def type(self):
        return "function" if not self.is_method else "method"

    @property
    def header(self):
        if self.is_method:
            return ""

        string = "def :func:`{}()<{}>`".format(self.name, self.path)
        return """\
{header}
{decore}
""".format(header=string, decore="-" * len(string))

    @property
    def content(self):
        return """\
{header}.. py:{type}:: {func_name}({args})
{doc}{sub_content}
""".format(header=self.header, type=self.type, func_name=self.path, doc=self.doc,
           args=", ".join(self.args), sub_content=self.sub_content)
