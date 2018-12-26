from property_manager import cached_property

from docme.components.utils import indent
from docme.components.base_component import BaseComponent


class Klass(BaseComponent):
    def __init__(self, name, doc, inheritance, path):
        super(Klass, self).__init__(doc)
        self.name = name
        self.inheritance = inheritance
        self.import_path = path.replace(".py", "").replace("/", ".") + "." + name

    @cached_property
    def doc(self):
        doc = super(Klass, self).doc
        return "\n{}\n\n".format(indent(doc, count=2)) if len(doc.strip()) > 0 else ""

    @property
    def header(self):
        return "class {}".format(self.link)

    @property
    def link(self):
        return ":class:`{}`".format(self.name)

    @property
    def content(self):
        return """\
{header}
{header_decore}

.. py:class:: {class_name}({inheritance})
        
        | **Inherits From:** 
        |   {inheritance_links}
        | **Import Path:**
        |   *{path}* 
    
{doc}{sub_content}
""".format(class_name=self.name, header=self.header, path=self.import_path,
           header_decore="-"*max(len(self.header), 6), inheritance=", ".join(self.inheritance),
           inheritance_links=", ".join([":class:`{kls}`".format(kls=kls) for kls in self.inheritance]),
           doc=self.doc, sub_content=indent(self.sub_content))
