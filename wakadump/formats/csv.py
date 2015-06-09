# -*- coding: utf-8 -*-
"""
    wakadump.formats.csv
    ~~~~~~~~~~~~~~~~~~~~

    Exports logged time to a CSV file.

    :copyright: (c) 2015 Alan Hamlett.
    :license: BSD, see LICENSE for more details.
"""


import click
import unicodecsv


class Formatter(object):

    def __init__(self, data, output_file=None):
        self.data = data
        self.output_file = output_file

    def run(self):
        w = unicodecsv.writer(self.output_file, encoding='utf-8')
        w.writerow(('Date', 'Total Logged Seconds'))
        with click.progressbar(self.data['days'],
                               label='Exporting to CSV',
                               fill_char=click.style('#', fg='blue')) as days:
            for day in days:
                w.writerow((day['date'], day['grand_total']['total_seconds']))
