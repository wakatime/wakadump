# -*- coding: utf-8 -*-

import os

from wakadump.cli import main

from . import utils
from click.testing import CliRunner


class BaseTestCase(utils.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_help_contents(self):
        args = ['--help']
        result = self.runner.invoke(main, args)
        self.assertEqual(result.exit_code, 0)

    def test_csv(self):
        with utils.NamedTemporaryFile() as fh:
            output = os.path.realpath(fh.name)
            args = ['--input', 'tests/samples/input.json', '--output', 'csv']
            result = self.runner.invoke(main, args, input='{0}\n'.format(output))
            self.assertEqual(result.exit_code, 0)

            actual = open(output).read()
            expected = open('tests/samples/output.csv').read()
            self.assertEqual(actual, expected)
