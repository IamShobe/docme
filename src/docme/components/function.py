from property_manager import cached_property

from utils import indent
from base_component import BaseComponent


class Function(BaseComponent):
    def __init__(self, name, doc, args, is_method=False):
        super(Function, self).__init__(doc)
        self.name = name
        self.args = args
        self.is_method = is_method

    @cached_property
    def doc(self):
        doc = super(Function, self).doc
        return "\n{}\n\n".format(indent(doc, count=2)) if len(doc.strip()) > 0 else ""

    @property
    def type(self):
        return "function" if not self.is_method else "method"

    @property
    def content(self):
        return """\
.. py:{type}:: {func_name}({args})
{doc}{sub_content}
""".format(type=self.type, func_name=self.name, doc=self.doc,
           args=", ".join(self.args), sub_content=self.sub_content)
