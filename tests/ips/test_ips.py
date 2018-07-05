# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

import json
import pytest
import click
from click.testing import CliRunner
from ricohcloudcli.ips import commands


class TestCaseNormal(object):

    @pytest.mark.parametrize('option', [
        ('-h'),
        ('--help')
    ])
    def test_help_ips(self, option):
        runner = CliRunner()
        result = runner.invoke(commands.ips, [option])
        assert result.exit_code == 0
        assert 'Image Processing Service' in result.output


class TestCaseException(object):

    @pytest.mark.parametrize('option', [
        ('test'),
        ('ips'),
        ('False'),
        ('123'),
    ])
    def test_invalid_command(self, option):
        runner = CliRunner()
        result = runner.invoke(commands.ips, [option])
        assert result.exit_code == 2
        assert 'Usage: ips [OPTIONS] COMMAND [ARGS]' in result.output
        assert 'Error: No such command' in result.output

    @pytest.mark.parametrize('option', [
        ('--test'),
        ('--ips'),
        ('--False'),
        ('--123'),
    ])
    def test_invalid_option(self, option):
        runner = CliRunner()
        result = runner.invoke(commands.ips, [option])
        assert result.exit_code == 2
        assert 'Error: no such option' in result.output
