from __future__ import absolute_import
from property_manager import cached_property

from .utils import indent
from .base_component import BaseComponent


class Klass(BaseComponent):
    """This class represents rst Class type."""
    def __init__(self, name, doc, inheritance, import_path):
        super(Klass, self).__init__(doc)
        self.name = name
        self.inheritance = inheritance
        self.import_path = import_path + "." + name

    @cached_property
    def doc(self):
        doc = super(Klass, self).doc
        return "\n{}\n\n".format(indent(doc, count=2)) if len(doc.strip()) > 0 else ""

    @property
    def header(self):
        return "class {}".format(self.link)

    @property
    def link(self):
        return ":class:`{class_name}<{path}>`".format(class_name=self.name, path=self.import_path)

    @property
    def content(self):
        return """\
{header}
{header_decore}

.. py:class:: {path}({inheritance})
            
        | **Inherits From:** 
        |   {inheritance_links}
    
{doc}{sub_content}
""".format(class_name=self.name, header=self.header, path=self.import_path,
           header_decore="-"*max(len(self.header), 6),
           inheritance=", ".join([base.__name__ for base in self.inheritance]),
           inheritance_links=", ".join([":class:`{kls}<{mod}.{kls}>`".format(
               kls=kls.__name__, mod=kls.__module__) for kls in self.inheritance]),
           doc=self.doc, sub_content=indent(self.sub_content))
