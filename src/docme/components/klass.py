from property_manager import cached_property

from utils import indent
from base_component import BaseComponent


class Klass(BaseComponent):
    def __init__(self, name, doc, inheritance):
        super(Klass, self).__init__(doc)
        self.name = name
        self.inheritance = inheritance

    @cached_property
    def doc(self):
        doc = super(Klass, self).doc
        return "\n{}\n\n".format(indent(doc, count=2)) if len(doc.strip()) > 0 else ""

    @property
    def header(self):
        return "Class: {}".format(self.link)

    @property
    def link(self):
        return ":class:`{}`".format(self.name)

    @property
    def content(self):
        return """\

{header}
{header_decore}

.. py:class:: {class_name}({inheritance})
{doc}{sub_content}
""".format(class_name=self.name, header=self.header, header_decore="-"*max(len(self.header), 6),
           inheritance=", ".join(self.inheritance), doc=self.doc, sub_content=indent(self.sub_content))
