# -*- coding: utf-8 -*-
"""
    wakadump.formats.keenio
    ~~~~~~~~~~~~~~~~~~~~~~~

    Exports logged time to a Keen.io project.

    :copyright: (c) 2015 Alan Hamlett.
    :license: BSD, see LICENSE for more details.
"""


import click
import pytz
from datetime import datetime
from keen.client import KeenClient


class Formatter(object):

    def __init__(self, data, project_id=None, write_key=None):
        self.data = data
        self.project_id = project_id
        self.write_key = write_key

    def append_event(self, dt, event_type, values):
        timestamp = dt.astimezone(pytz.utc)
        event = {
            'keen': {
                'timestamp': timestamp.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            },
            'type': event_type,
            'weekday': dt.strftime('%A'),
            'weekday_number': dt.strftime('%w'),
            'day': dt.strftime('%d'),
            'month': dt.strftime('%m'),
            'year': dt.strftime('%Y'),
        }
        event.update(values)
        self.events.append(event)

    def run(self):
        keen_client = KeenClient(
            project_id=self.project_id,
            write_key=self.write_key,
        )

        timezone = pytz.timezone(self.data['user']['timezone'])

        self.events = []
        with click.progressbar(self.data['days'],
                            label='Preparing keen.io events',
                            fill_char=click.style('#', fg='blue')) as days:

            for day in days:
                dt = self._parse_date(day['date'], timezone)

                self.append_event(dt, 'total', {
                    'seconds': day['grand_total']['total_seconds'],
                })

                categories = [
                    'editor',
                    'language',
                    'operating_system',
                    'project',
                ]
                for category in categories:
                    for item in day.get(category + 's', []):
                        self.append_event(dt, category, {
                            'seconds': item['total_seconds'],
                            'name': item['name'],
                        })

                files = {}
                for project in day.get('projects', []):
                    for f in project.get('entities', []):
                        if f['name'] not in files:
                            files[f['name']] = 0
                        files[f['name']] += f['total_seconds']

                for name, seconds in files.items():
                    self.append_event(dt, 'file', {
                        'seconds': seconds,
                        'name': name,
                    })

        if len(self.events) == 0:
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
            collection: self.events,
        })

    def _parse_date(self, date_str, timezone):
        dt = None
        date_str = date_str.replace('/', '-')
        try:
            dt = datetime.strptime(date_str, '%m-%d-%Y')
        except ValueError:
            dt = datetime.strptime(date_str, '%Y-%m-%d')
        dt = dt.replace(tzinfo=timezone).replace(hour=12)
        return dt
