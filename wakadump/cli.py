# -*- coding: utf-8 -*-
"""
    wakadump.cli
    ~~~~~~~~~~~~

    Command-line entry point.

    :copyright: (c) 2015 Alan Hamlett.
    :license: BSD, see LICENSE for more details.
"""


import click
import simplejson as json
import traceback

from .__about__ import __version__
from .compat import import_module


def check_output(ctx, param, value):
    if value == 'keen.io':
        ctx.params['project_id'] = click.prompt('keen.io Project ID',
                                                type=click.STRING)
        ctx.params['write_key'] = click.prompt('keen.io project Write Key',
                                               type=click.STRING,
                                               hide_input=True)
    elif value == 'csv':
        ctx.params['output_file'] = click.prompt('Output csv file',
                                                type=click.File('w'))
    return value


def make_module_name(module_name):
    return module_name.replace('.', '').replace('-', '')


@click.command()
@click.option('--input', help='path to json data dump from wakatime.com',
              type=click.File('r'), required=True)
@click.option('--output', type=click.Choice(['keen.io', 'csv']), required=True,
              help='export format', callback=check_output)
@click.version_option(__version__)
def main(input, output, **kwargs):
    data = json.loads(input.read())
    try:
        data['days']
    except KeyError:
        click.echo(traceback.format_exc(), err=True)
        click.echo('Wrong input file format. Is it a valid WakaTime Data Dump from your Settings page?', err=True)
        return

    module_name = make_module_name(output)
    module = import_module('.formats.%s' % module_name, package=__package__)
    formatter = getattr(module, 'Formatter')(data, **kwargs)
    formatter.run()
    click.echo('Complete.')
