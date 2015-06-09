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

    wakadump --input <json data dump> --format <output format>
    

Output Formats
--------------

* csv
* keen.io
