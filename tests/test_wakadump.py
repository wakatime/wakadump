# -*- coding: utf-8 -*-


from wakadump.cli import main

from . import utils
from click.testing import CliRunner


class BaseTestCase(utils.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_help_contents(self):
        args = ['--help']
        result = self.runner.invoke(main, args)
        self.assertEquals(result.exit_code, 0)
