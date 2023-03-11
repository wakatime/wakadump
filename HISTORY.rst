
History
-------


5.0.0 (2023-03-11)
++++++++++++++++++

- Drop support for Python 2.
  `#11 <https://github.com/wakatime/wakadump/issues/11>`_


4.0.0 (2018-06-06)
++++++++++++++++++

- Update csv formatter to new data dump schema.
  `#9 <https://github.com/wakatime/wakadump/issues/9>`_


3.0.1 (2017-09-06)
++++++++++++++++++

- Fix bug with unicode strings in CSV output.
  `#8 <https://github.com/wakatime/wakadump/issues/8>`_


3.0.0 (2017-09-06)
++++++++++++++++++

- Improved Python3 and Unicode CSV support.


2.0.6 (2017-01-22)
++++++++++++++++++

- Use new data dump format where projects has total_seconds nested under grand_total.
  `#7 <https://github.com/wakatime/wakadump/issues/7>`_


2.0.5 (2017-01-16)
++++++++++++++++++

- Use new data dump format without projects.dump subkey.


2.0.4 (2016-09-17)
++++++++++++++++++

- Check input file for valid format before processing
  `#6 <https://github.com/wakatime/wakadump/issues/6>`_


2.0.3 (2016-09-07)
++++++++++++++++++

- Include data about projects, files, languages, editors, and operating systems in CSV output file.


2.0.2 (2015-11-23)
++++++++++++++++++

- Support for Python3.


2.0.1 (2015-09-08)
++++++++++++++++++

- Support date formats YYYY-MM-DD and MM-DD-YYYY.


2.0.0 (2015-06-09)
++++++++++++++++++

- Rename argument --filter to --output.
- Include date parts in KeenIO output.


1.0.3 (2015-06-08)
++++++++++++++++++

- Correctly format files for keen.io events.


1.0.2 (2015-06-08)
++++++++++++++++++

- Fix pypi distribution.


1.0.1 (2015-06-08)
++++++++++++++++++

- Don't import python dependencies from setup.py.


1.0.0 (2015-06-08)
++++++++++++++++++

- Birth.
