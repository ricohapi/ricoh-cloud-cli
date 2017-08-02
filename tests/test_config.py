# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

import pytest
from mock import patch, mock_open
from click.testing import CliRunner
from ricohcloudcli.config import commands as config


class TestNormalCase(object):

    @patch('click.prompt')
    def test_ok_configure(self, prompt):
        prompt.side_effect = ['test_id', 'test_secret']
        runner = CliRunner()
        result = runner.invoke(config.configure, ['--profile', 'test_config'])
        prompt.assert_any_call(
            'RAPI Client ID', hide_input=True, type=str, prompt_suffix=': ')
        prompt.assert_any_call('RAPI Client Secret',
                               hide_input=True, type=str, prompt_suffix=': ')
        assert result.exit_code == 0


class TestCaseException(object):

    @pytest.mark.parametrize('argument', [
        ('test'),
        ('configure'),
        ('False'),
        ('123'),
    ])
    def test_invalid_arg(self, argument):
        runner = CliRunner()
        result = runner.invoke(config.configure, [argument])
        assert result.exit_code == 2
        assert 'Error: Got unexpected extra argument' in result.output

    @pytest.mark.parametrize('option', [
        ('--test'),
        ('--configure'),
        ('--False'),
        ('--123'),
    ])
    def test_invalid_option(self, option):
        runner = CliRunner()
        result = runner.invoke(config.configure, [option])
        assert result.exit_code == 2
        assert 'Error: no such option' in result.output
