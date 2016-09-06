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

        self._get_column_names()
        w.writerow(self.columns)

        with click.progressbar(self.data['days'],
                               label='Exporting to CSV file...',
                               fill_char=click.style('#', fg='blue')) as days:
            for day in days:
                data = [
                    day['date'],
                    day['grand_total']['total_seconds'],
                ]
                self._add_data_for_columns(data, self.projects, day['projects'])
                self._add_data_for_columns(data, self.entities, day['entities'])
                self._add_data_for_columns(data, self.languages, day['languages'])
                self._add_data_for_columns(data, self.editors, day['editors'])
                self._add_data_for_columns(data, self.operating_systems, day['operating_systems'])
                w.writerow(data)

    def _get_column_names(self):
        self.projects = {}
        self.entities = {}
        self.languages = {}
        self.editors = {}
        self.operating_systems = {}

        with click.progressbar(self.data['days'],
                               label='Getting column names...',
                               fill_char=click.style('#', fg='blue')) as days:
            for day in days:
                self._find_columns(self.projects, day['projects'])
                self._find_columns(self.entities, day['entities'])
                self._find_columns(self.languages, day['languages'])
                self._find_columns(self.editors, day['editors'])
                self._find_columns(self.operating_systems, day['operating_systems'])

        self.projects = self.projects.keys()
        self.entities = self.entities.keys()
        self.languages = self.languages.keys()
        self.editors = self.editors.keys()
        self.operating_systems = self.operating_systems.keys()

        self.columns = [
            'DATE',
            'TOTAL LOGGED SECONDS',
        ]
        self._add_columns('PROJECTS', self.projects)
        self._add_columns('FILES', self.entities)
        self._add_columns('LANGUAGES', self.languages)
        self._add_columns('EDITORS', self.editors)
        self._add_columns('OPERATING SYSTEMS', self.operating_systems)

    def _find_columns(self, existing, items):
        for item in items:
            if item['name'] not in existing:
                existing[item['name']] = True

    def _add_columns(self, name, data):
        self.columns.append(name)
        self.columns.extend(data)

    def _add_data_for_columns(self, existing_data, column_names, column_data):
        data = {}
        for item in column_data:
            data[item['name']] = item['total_seconds']
        existing_data.append('')
        for name in column_names:
            existing_data.append(data.get(name, 0))
