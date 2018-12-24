from base_component import BaseComponent


class Module(BaseComponent):
    def __init__(self, title, description):
        super(Module, self).__init__()
        self.title = title
        self.description = description

    @property
    def doc(self):
        return self.description if self.description is not None else ""

    @property
    def content(self):
        return """\
{title_decore}
{title}
{title_decore}
{doc}
{sub_content}
""".format(title=self.title, title_decore="=" * max(len(self.title), 6),
           doc="\n{}\n\n".format(self.doc) if self.doc else "", sub_content=self.sub_content)
