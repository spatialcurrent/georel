georel
==============

.. image:: https://travis-ci.org/spatialcurrent/georel.png
    :target: https://travis-ci.org/spatialcurrent/georel

.. image:: https://img.shields.io/pypi/v/georel.svg
    :target: https://pypi.python.org/pypi/georel

.. image:: https://readthedocs.org/projects/georel/badge/?version=master
        :target: http://georel.readthedocs.org/en/latest/
        :alt: Master Documentation Status

Description
-----------------

A Python library for parsing geospatial relationships from natural language.

Installation
-----------------

Install via PyPI_ with:

.. _PyPI: https://pypi.python.org/pypi

.. code-block:: bash

    pip install georel

Or install directly from GitHub_ with:

.. _GitHub: https://github.com/

.. code-block:: bash

    pip install git+git://github.com/spatialcurrent/georel.git@master

Usage
-----------------

Below are some simple use cases.  See test.py for more use cases.

.. code:: python

   from georel import georel

   value = georel.parse("2", "m")
   # value == {"value": 2, "units": "meter"}

   value = georel.parse("2", "km")
   # value == {"value": 2, "units": "kilometer"}

   value = georel.parse("2", "miles")
   # value == {"value": 2, "units": "mile"}


By default, the original units are used, but georel can transform to another unit too.

.. code:: python

    value = georel.parse("1,000", "meters", "miles")
    # value == {"value": 0.621371, "units": "mile"}

Testing
-----------------

For unit tests, run the following command from the project root folder:

.. code:: shell

    python -m unittest -v georel.test

Contributing
-----------------

`Spatial Current, Inc.`_ is currently accepting pull requests for this repository.  We'd love to have your contributions!  Please see `Contributing.rst`_ for how to get started.

.. _`Spatial Current, Inc.`: https://spatialcurrent.io
.. _Contributing.rst: https://github.com/spatialcurrent/georel/blob/master/CONTRIBUTING.rst

License
-----------------

This work is distributed under the **MIT License**.  See **LICENSE** file.
