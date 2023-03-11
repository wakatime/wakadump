.. image:: https://img.shields.io/github/actions/workflow/status/wakatime/wakadump/tests.yml?branch=master
    :target: https://github.com/wakatime/wakadump/actions
    :alt: Tests

.. image:: https://codecov.io/gh/wakatime/wakadump/branch/master/graph/badge.svg?token=Ob1I7eMhiS
    :target: https://codecov.io/gh/wakatime/wakadump
    :alt: Coverage

.. image:: https://img.shields.io/pypi/v/wakadump.svg
    :target: https://pypi.python.org/pypi/wakadump
    :alt: Version

.. image:: https://img.shields.io/pypi/pyversions/wakadump.svg
    :target: https://pypi.python.org/pypi/wakadump
    :alt: Supported Python Versions

.. image:: https://wakatime.com/badge/github/wakatime/wakadump.svg
    :target: https://wakatime.com/badge/github/wakatime/wakadump

wakadump
========

Command line tool for converting WakaTime data dump files into various formats.


Installation
------------

Install using pip::

    pip install wakadump


Usage
-----

After exporting your WakaTime data as JSON from your `settings page <https://wakatime.com/settings>`_, you can convert the JSON file into various formats::

    wakadump --input <json data dump> --output <format>


Output Formats
--------------

* csv
* keen.io
