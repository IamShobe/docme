from __future__ import absolute_import
from property_manager import cached_property
from sphinx.ext.napoleon.docstring import GoogleDocstring


class BaseComponent(object):
    """Base component of all components of rst format."""
    def __init__(self, doc):
        self.sub_components = []
        self._doc = doc

    @property
    def content(self):
        """Fetch content of current component"""
        return

    @cached_property
    def doc(self):
        return "" if self._doc is None else str(GoogleDocstring(self._doc))

    @property
    def sub_content(self):
        return "\n".join(component.content for component in self.sub_components)

    def add_component(self, component):
        """Add sub component to the current class.

        Args:
            component (BaseComponent): component to add as sub component.
        """
        self.sub_components.append(component)

    def add_components(self, components):
        """Add sub components to the current class.

        Args:
            components (list): list of components to add.
        """
        self.sub_components.extend(components)
