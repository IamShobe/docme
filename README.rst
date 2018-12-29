=====
docme
=====

| ``docme`` is a python application, which its goal is to reduce writing redundant rst documentations.
| it is similar to sphinx builtin ``autodoc`` module, but ``docme`` goal is to create more cleaner look,
| that ``autodoc`` doesn't provide.

============
Installation
============


Simply use pip installer:

.. code-block:: bash

    pip install docme

Or download src files from Github/Pypi and write:

.. code-block:: bash

    python setup.py install

for developers, use:

.. code-block:: bash

    python setup.py develop

===========
Quick Start
===========


lets say your project's tree is like so:

.. code-block:: bash

    .gitignore
    src/
    src/project/
    src/project/file.py

and you wish to create auto documentation of your project.

simply use ``docme`` command - which is an entry point which directs to :func:`main<docme.cli.main>` function:

.. code-block:: bash

    docme src/project doc

| where ``src/project`` is the path to your main project files,
| and ``doc`` is the directory of docs that will be created.

| The result is that a new folder will be created named ``doc``, and in it all relevant rst files,
| new tree will look like:

.. code-block:: bash

    .gitignore
    doc/
    doc/api_reference/
    doc/api_reference/project/
    doc/api_reference/project/file.rst
    doc/api_reference/project/index.rst
    doc/api_reference/index.rst
    doc/index.rst
    src/
    src/project/
    src/project/file.py


now you can simply add ``make`` file and ``conf.py`` for sphinx to compile the doc to html!
