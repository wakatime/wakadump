# -*- coding: utf-8 -*-
"""
    wakadump.formats.csv
    ~~~~~~~~~~~~~~~~~~~~

    Exports logged time to a CSV file.

    :copyright: (c) 2015 Alan Hamlett.
    :license: BSD, see LICENSE for more details.
"""


import click
import io
from backports import csv


class Formatter(object):

    def __init__(self, data, output_file=None):
        self.data = data
        self.output_file = output_file

    def run(self):
        with io.open(self.output_file, 'w', newline='', encoding='utf8') as fh:
            w = csv.writer(fh)

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
                    entities = self._add_data_for_columns(
                        data,
                        self.projects,
                        day['projects'],
                        is_project=True,
                    )
                    self._add_data_for_columns(data,
                                               self.languages,
                                               day['languages'])
                    self._add_data_for_columns(data,
                                               self.editors,
                                               day['editors'])
                    self._add_data_for_columns(data,
                                               self.operating_systems,
                                               day['operating_systems'])
                    self._add_data_for_columns(data,
                                               self.categories,
                                               day['categories'])
                    self._add_data_for_columns(data,
                                               self.entities,
                                               entities)
                    w.writerow(data)

    def _get_column_names(self):
        self.projects = {}
        self.languages = {}
        self.editors = {}
        self.operating_systems = {}
        self.categories = {}
        self.entities = {}

        with click.progressbar(self.data['days'],
                               label='Getting column names...',
                               fill_char=click.style('#', fg='blue')) as days:
            for day in days:
                self._find_columns(self.projects, day['projects'],
                                   is_project=True)
                self._find_columns(self.languages, day['languages'])
                self._find_columns(self.editors, day['editors'])
                self._find_columns(self.operating_systems,
                                   day['operating_systems'])
                self._find_columns(self.categories, day['categories'])

        self.projects = sorted(self.projects.keys())
        self.languages = sorted(self.languages.keys())
        self.editors = sorted(self.editors.keys())
        self.operating_systems = sorted(self.operating_systems.keys())
        self.categories = sorted(self.categories.keys())
        self.entities = sorted(self.entities.keys())

        self.columns = [
            'DATE',
            'TOTAL LOGGED SECONDS',
        ]
        self._add_columns('PROJECTS', self.projects)
        self._add_columns('LANGUAGES', self.languages)
        self._add_columns('EDITORS', self.editors)
        self._add_columns('OPERATING SYSTEMS', self.operating_systems)
        self._add_columns('CATEGORIES', self.categories)
        self._add_columns('FILES', self.entities)

    def _find_columns(self, existing, items, is_project=False):
        for item in items:
            if item['name'] not in existing:
                existing[item['name']] = True
            if is_project:
                self._find_columns(self.entities, item['entities'])

    def _add_columns(self, name, data):
        self.columns.append(name)
        self.columns.extend(data)

    def _add_data_for_columns(self, existing_data, column_names, column_data,
                              is_project=False):
        entities = []
        data = {}
        for item in column_data:
            data[item['name']] = item.get('total_seconds',
                                          item.get('grand_total',
                                                   {}).get('total_seconds'))
            if is_project:
                entities.extend(item['entities'])
        existing_data.append('')
        for name in column_names:
            existing_data.append(data.get(name, 0))
        return entities
