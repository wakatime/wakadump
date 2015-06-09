# -*- coding: utf-8 -*-
"""
    wakadump.formats.keenio
    ~~~~~~~~~~~~~~~~~~~~~~~

    Exports logged time to a Keen.io project.

    :copyright: (c) 2015 Alan Hamlett.
    :license: BSD, see LICENSE for more details.
"""


import click
from datetime import datetime
from keen.client import KeenClient


class Formatter(object):

    def __init__(self, data, project_id=None, write_key=None):
        self.data = data
        self.project_id = project_id
        self.write_key = write_key

    def run(self):
        keen_client = KeenClient(
            project_id=self.project_id,
            write_key=self.write_key,
        )

        events = []
        with click.progressbar(self.data['days'],
                            label='Preparing keen.io events',
                            fill_char=click.style('#', fg='blue')) as days:
            for day in days:
                timestamp = (datetime.strptime(day['date'], '%m/%d/%Y')
                             .strftime('%Y-%m-%dT%H:%M:%S.000Z'))
                events.append({
                    'keen': {
                        'timestamp': timestamp,
                    },
                    'seconds': day['grand_total']['total_seconds'],
                    'type': 'total',
                })

                categories = [
                    'editor',
                    'language',
                    'operating_system',
                    'project',
                ]
                for category in categories:
                    for item in day.get(category + 's', []):
                        events.append({
                            'keen': {
                                'timestamp': timestamp,
                            },
                            'seconds': item['total_seconds'],
                            'name': item['name'],
                            'type': category,
                        })

                files = {}
                for project in day.get('projects', []):
                    for f in project.get('files', []):
                        if f['name'] not in files:
                            files[f['name']] = 0
                        files[f['name']] += f['total_seconds']

                for name, seconds in files.items():
                    events.append({
                        'keen': {
                            'timestamp': timestamp,
                        },
                        'seconds': seconds,
                        'name': name,
                        'type': 'file',
                    })

        if len(events) == 0:
            click.echo('No events available for exporting to keen.io')
            return

        click.echo('Uploading events to keen.io...')
        start = datetime.utcfromtimestamp(self.data['range']['start'])
        end = datetime.utcfromtimestamp(self.data['range']['end'])
        collection = 'WakaTime Data Dump from {start} until {end}'.format(
            start=start.strftime('%Y-%m-%d'),
            end=end.strftime('%Y-%m-%d'),
        )
        keen_client.add_events({
            collection: events,
        })
