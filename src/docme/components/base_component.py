
class BaseComponent(object):
    def __init__(self):
        self.sub_components = []

    @property
    def content(self):
        return

    @property
    def sub_content(self):
        return "\n".join(component.content for component in self.sub_components)

    def add_component(self, component):
        self.sub_components.append(component)

