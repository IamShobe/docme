=================
base_component.py
=================

Location Path: 
    *src/docme/builders/components/base_component.py*

class :class:`BaseComponent<src.docme.builders.components.base_component.BaseComponent>`
----------------------------------------------------------------------------------------

.. py:class:: src.docme.builders.components.base_component.BaseComponent(object)
            
        | **Inherits From:** 
        |   :class:`object<__builtin__.object>`
    

        Base component of all components of rst format.

    .. py:method:: src.docme.builders.components.base_component.BaseComponent.__init__(self, doc)
    
    
    .. py:method:: src.docme.builders.components.base_component.BaseComponent.content(self)
    
            Fetch content of current component
    
    
    
    .. py:method:: src.docme.builders.components.base_component.BaseComponent.doc(self)
    
    
    .. py:method:: src.docme.builders.components.base_component.BaseComponent.sub_content(self)
    
    
    .. py:method:: src.docme.builders.components.base_component.BaseComponent.add_component(self, component)
    
            Add sub component to the current class.
            
            :param component: component to add as sub component.
            :type component: BaseComponent
            
    
    
    
    .. py:method:: src.docme.builders.components.base_component.BaseComponent.add_components(self, components)
    
            Add sub components to the current class.
            
            :param components: list of components to add.
            :type components: list
            
    
    
    

