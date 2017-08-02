# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

import json
import pytest
import click
from click.testing import CliRunner
from ricohcloudcli import cli


class TestCaseNormal(object):

    @pytest.mark.parametrize('option', [
        ('-h'),
        ('--help')
    ])
    def test_rapi(self, option):
        runner = CliRunner()
        result = runner.invoke(cli.rapi, [option])
        assert result.exit_code == 0
        assert 'RICOH Cloud CLI' in result.output


class TestCaseException(object):

    @pytest.mark.parametrize('option', [
        ('test'),
        ('rapi'),
        ('False'),
        ('123'),
    ])
    def test_invalid_command(self, option):
        runner = CliRunner()
        result = runner.invoke(cli.rapi, [option])
        assert result.exit_code == 2
        assert 'Usage: rapi [OPTIONS] COMMAND [ARGS]' in result.output
        assert 'Error: No such command' in result.output

    @pytest.mark.parametrize('option', [
        ('--test'),
        ('--rapi'),
        ('--False'),
        ('--123'),
        ('-test'),
        ('-rapi'),
        ('-False'),
        ('-123'),
    ])
    def test_invalid_option(self, option):
        runner = CliRunner()
        result = runner.invoke(cli.rapi, [option])
        assert result.exit_code == 2
        assert 'Error: no such option' in result.output

    @pytest.mark.parametrize('option', [
        ('--profile')
    ])
    def test_profile_without_args(self, option):
        runner = CliRunner()
        result = runner.invoke(cli.rapi, [option])
        assert result.exit_code == 2
        assert 'Error: --profile option requires an argument' in result.output
