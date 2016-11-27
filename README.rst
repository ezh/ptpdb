ptpdb
=====

(Still experimental) PDB replacement, build on top of `prompt_toolkit
<http://github.com/jonathanslenders/python-prompt-toolkit/>`_ and `ptpython
<https://github.com/jonathanslenders/ptpython/>`_.


Installation
************

::

    pip install ptpdb

Usage
*****

.. code:: python

    from ptpdb import set_trace
    set_trace()


See `the official PDB documentation
<https://docs.python.org/3/library/pdb.html>`_ to learn how it works.

Configuration
*************

You may extends it functionality via ~/.pdbrc or via configuration file at ~/.ptpython/dbconfig.py

See `<tree/master/examples/dbconfig.py>_ example configuration file`. Argument of configuration method is PtPdb class.

Please create an empty ~/.ptpython/dbconfig.py to suppress the warning message.

Adjust the source code window height
------------------------------------

.. code:: python

    height = LayoutDimension(preferred=20)
    dbrepl._source_code_window._height = (lambda cli: height)
