===========
Config File
===========

| Each directory can have a config file in it!
| before creating the doc ``docme`` will look for ``doc.yml`` files.
| The files will contain rules for creating the doc.

.. code-block:: yaml

    title: A Title
    toctree:
        maxdepth: 2
        ...

currently implemented:
 - ``title`` - title of the index file of current folder.
 - ``toctree`` - can have properties that will be added to the index files.
