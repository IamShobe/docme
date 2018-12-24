from utils import indent
from base_component import BaseComponent


class Klass(BaseComponent):
    def __init__(self, name, doc, inheritance):
        super(Klass, self).__init__()
        self.name = name
        self.doc = doc
        self.inheritance = inheritance

    @property
    def header(self):
        return "Class: {}".format(self.link)

    @property
    def link(self):
        return ":class:`{}`".format(self.name)

    @property
    def content(self):
        documentation = indent(self.doc, count=2) if self.doc else ""
        return """\

{header}
{header_decore}

.. py:class:: {class_name}({inheritance})
{doc}{sub_content}
""".format(class_name=self.name, header=self.header, header_decore="-"*max(len(self.header), 6),
           inheritance=", ".join(self.inheritance),
           doc="\n{}\n\n".format(documentation) if documentation else "", sub_content=indent(self.sub_content))
