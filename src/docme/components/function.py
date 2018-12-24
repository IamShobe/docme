from utils import indent
from base_component import BaseComponent


class Function(BaseComponent):
    def __init__(self, name, doc, args, is_method=False):
        super(Function, self).__init__()
        self.name = name
        self.doc = doc
        self.args = args
        self.is_method = is_method

    @property
    def content(self):
        documentation = indent(self.doc, count=2) if self.doc else ""
        if documentation:
            return """\
.. py:{type}:: {func_name}({args})
{doc}{sub_content}
""".format(type="function" if not self.is_method else "method", func_name=self.name,
           doc="\n{}\n\n".format(documentation) if documentation else "", args=", ".join(self.args),
           sub_content=self.sub_content)
