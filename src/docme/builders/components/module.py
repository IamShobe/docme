from __future__ import absolute_import
from property_manager import cached_property

from .base_component import BaseComponent


class Module(BaseComponent):
    """This class represents a rst file."""
    def __init__(self, title, doc, path):
        super(Module, self).__init__(doc)
        self.title = title
        self.path = path

    @cached_property
    def doc(self):
        doc = super(Module, self).doc
        return "\n{}\n\n".format(doc) if len(doc.strip()) > 0 else ""

    @property
    def content(self):
        return """\
{title_decore}
{title}
{title_decore}

Location Path: 
    *{path}*

{doc}{sub_content}
""".format(title=self.title, title_decore="=" * max(len(self.title), 6),
           path=self.path, doc=self.doc, sub_content=self.sub_content)
