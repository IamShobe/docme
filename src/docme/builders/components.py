import ast
import importlib
import inspect
import os

from docme.components.function import Function
from docme.components.klass import Klass
from docme.components.module import Module


def make_functions(mod_node, mod):
    import_path = mod.path.replace(".py", "").replace("/", ".")
    methods = []
    for elem in mod_node.body:
        if isinstance(elem, ast.FunctionDef):
            func_name = elem.name
            func_doc = ast.get_docstring(elem)
            fn = Function(func_name, func_doc, [arg.id for arg in elem.args.args], is_method=False,
                          path=import_path)
            methods.append(fn)

    return methods


def make_methods(cls_node, cls):
    methods = []
    for elem in cls_node.body:
        if isinstance(elem, ast.FunctionDef):
            func_name = elem.name
            func_doc = ast.get_docstring(elem)
            fn = Function(func_name, func_doc, [arg.id for arg in elem.args.args], is_method=True,
                          path=cls.import_path)
            methods.append(fn)

    return methods


def make_classes(mod_node, mod):
    import_path = mod.path.replace(".py", "").replace("/", ".")
    actual_mod = importlib.import_module(import_path)
    classes = []
    for elem in mod_node.body:
        if isinstance(elem, ast.ClassDef):
            cls_name = elem.name
            cls_doc = ast.get_docstring(elem)
            bases = getattr(actual_mod, cls_name).__bases__
            cls = Klass(cls_name, cls_doc, bases, import_path)
            cls.add_components(make_methods(elem, cls))
            classes.append(cls)

    return classes


def make_module(path):
    with open(path) as module:
        node = ast.parse(module.read())

    doc = ast.get_docstring(node)

    mod = Module(os.path.basename(path), doc, path)
    mod.add_components(make_classes(node, mod))
    mod.add_components(make_functions(node, mod))

    return mod
