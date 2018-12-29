=====
docme
=====

-----
Intro
-----

| ``docme`` is a python application, which its goal is to reduce writing redundant rst documentations.
| it is similar to sphinx builtin ``autodoc`` module, but ``docme`` goal is to create more cleaner look,
| that ``autodoc`` doesn't provide.

------------
Installation
------------


Simply use pip installer:

.. code-block:: bash

    pip install docme

Or download src files from Github/Pypi and write:

.. code-block:: bash

    python setup.py install

for developers, use:

.. code-block:: bash

    python setup.py develop

--------------
Where To Begin
--------------

Simple Start
------------

lets say your project's tree is like so:

.. code-block:: bash

    .gitignore
    src/
    src/project/
    src/project/file.py

and you wish to create auto documentation of your project.

simply use ``docme`` command - which is an entry point which directs to :func:``docme.cli.main`` function:

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

.. code-block:: bash

    cd doc
    make html


Including External Doc
----------------------

| lets say you already got some doc to include to the api reference:

.. code-block:: bash

    .gitignore
    doc/
    doc/how_to_start/
    doc/how_to_start/advanced.rst
    doc/how_to_start/intro.rst
    doc/how_to_start/index.rst
    src/
    src/project/
    src/project/file.py

you can include ``how_to_start`` section like so:

.. code-block:: bash

    docme src/project doc --extra-doc how_to_start/index

| pay attention it is exactly the line you need to add to the main ``index.rst``.
| newly created tree:

.. code-block:: bash

    .gitignore
    doc/
    doc/how_to_start/
    doc/how_to_start/advanced.rst
    doc/how_to_start/intro.rst
    doc/how_to_start/index.rst
    doc/api_reference/
    doc/api_reference/project/
    doc/api_reference/project/file.rst
    doc/api_reference/project/index.rst
    doc/api_reference/index.rst
    doc/index.rst
    src/
    src/project/
    src/project/file.py

| In your doc you can reference classes and functions from your api!
| like so:

::

    :class:`example<path.to.Class>`
