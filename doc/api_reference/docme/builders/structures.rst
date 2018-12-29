=============
structures.py
=============

Location Path: 
    *docme/builders/structures.py*

def :func:`make_functions()<docme.builders.structures.make_functions>`
----------------------------------------------------------------------
.. py:function:: docme.builders.structures.make_functions(mod_node, mod)

        Make functions from the given module.
        
        :param mod_node: ast node of the module.
        :type mod_node: ast.Node
        :param mod: module object to add the functions to.
        :type mod: Module
        
        :returns: list. list of functions to add to the module.
        



def :func:`make_methods()<docme.builders.structures.make_methods>`
------------------------------------------------------------------
.. py:function:: docme.builders.structures.make_methods(cls_node, cls)

        Make methods from the given class.
        
        :param cls_node: ast node of the class.
        :type cls_node: ast.Node
        :param cls: class object to add the functions to.
        :type cls: Klass
        
        :returns: list. list of functions to add to the class.
        



def :func:`make_classes()<docme.builders.structures.make_classes>`
------------------------------------------------------------------
.. py:function:: docme.builders.structures.make_classes(mod_node, mod)

        Make classes from the given module.
        
        :param mod_node: ast node of the module.
        :type mod_node: ast.Node
        :param mod: module object to add the functions to.
        :type mod: Module
        
        :returns: list. list of classes to add to the module.
        



def :func:`make_module()<docme.builders.structures.make_module>`
----------------------------------------------------------------
.. py:function:: docme.builders.structures.make_module(path, doc_path)

        Create module object of the given path.
        
        :param path: path to create the module from.
        :type path: str
        :param doc_path: path to the module doc.
        :type doc_path: str
        
        :returns: Module. module object that represents the given path.
        



