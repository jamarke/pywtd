py-wtd
======

.. image:: https://img.shields.io/pypi/v/py-wtd.svg
    :target: https://pypi.python.org/pypi/py-wtd
    :alt: Latest PyPI version

A minimal python interface to the www.worldtradingdata.com API

Usage
-----

Register at https://www.worldtradingdata.com/register and get your API key.

`import py-wtd as wtd`
`wtd.ApiConfig.api_key = <key>`

Retrieve historical stock data, returns a pandas DataFrame:
`data = wtd.get('CBA.AX', date_from='2017-01-01', date_to='2018-01-01')`


Installation
------------
`git clone https://github.com/jamarke/py-wtd.git`
`pip install .`

Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`py-wtd` was written by `jamarke <tacocorporation@protonmail.com>`_.
