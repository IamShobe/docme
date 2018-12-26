from property_manager import cached_property
from sphinx.ext.napoleon.docstring import GoogleDocstring


class BaseComponent(object):
    def __init__(self, doc):
        self.sub_components = []
        self._doc = doc

    @property
    def content(self):
        return

    @cached_property
    def doc(self):
        return "" if self._doc is None else str(GoogleDocstring(self._doc))

    @property
    def sub_content(self):
        return "\n".join(component.content for component in self.sub_components)

    def add_component(self, component):
        self.sub_components.append(component)

    def add_components(self, components):
        self.sub_components.extend(components)
