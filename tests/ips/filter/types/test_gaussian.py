# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.
import tempfile
import imghdr
import pytest
from click.testing import CliRunner
from ricohcloudcli.ips.filter.types import gaussian as commands
from . import util

INVALID_KSIZE = 'Invalid value for "-k" / "--ksize": requires comma-separated 2 int values'
INVALID_SIGMA = 'Invalid value for "-s" / "--sigma": requires comma-separated 2 float values'


class TestCaseNormal(object):

    @pytest.fixture
    def config(self):
        obj = {'profile': 'test'}
        return obj

    @pytest.mark.parametrize('option', [
        ('-h'),
        ('--help')
    ])
    def test_ok_help(self, config, option):
        runner = CliRunner()
        result = runner.invoke(commands.gaussian, [option], obj=config)
        assert result.exit_code == 0
        assert 'Applies image filters to an image using a gaussian filter, to standard output.' in result.output

    @pytest.mark.parametrize(('key', 'value'), [
        ('--input', util.TEST_IMAGE_BINARY_JPG),
        ('--input', util.TEST_IMAGE_BINARY_PNG),
        ('--input', util.TEST_IMAGE_URI_JPG),
        ('--input', util.TEST_IMAGE_URI_PNG),
        ('--input', util.TEST_IMAGE_URI_BLANK),
        ('-i', util.TEST_IMAGE_BINARY_JPG),
    ])
    def test_ok_input(self, config, key, value):
        runner = CliRunner()
        options = [key, value, '-l', '0,0,10,10', '-k', '1,1']
        result = runner.invoke(commands.gaussian, options, obj=config)
        self.__assert_reslut(result)

    @pytest.mark.parametrize(('key', 'value'), [
        (None, None),
        ('--output', tempfile.NamedTemporaryFile(suffix='.jpg').name),
        ('-o', tempfile.NamedTemporaryFile(suffix='.jpg').name),
    ])
    def test_ok_output(self, config, key, value):
        runner = CliRunner()
        options = ['-i', util.TEST_IMAGE_BINARY_JPG, '-l', '0,0,10,10', '-k', '1,1']
        if key:
            options.extend([key, value])
        result = runner.invoke(commands.gaussian, options, obj=config)
        self.__assert_reslut(result, value)

    @pytest.mark.parametrize(('key', 'value'), [
        ('--ksize', '1,1'),
        ('--ksize', '3,1'),
        ('-k', '1,1'),
        ('-k', '3,1'),
    ])
    def test_ok_ksize(self, config, key, value):
        runner = CliRunner()
        options = ['-i', util.TEST_IMAGE_BINARY_JPG, '-l', '0,0,10,10', key, value]
        result = runner.invoke(commands.gaussian, options, obj=config)
        self.__assert_reslut(result)

    @pytest.mark.parametrize(('key', 'value'), [
        ('--sigma', '10,10'),
        ('--sigma', '10,0'),
        ('--sigma', '10,5'),
        ('-s', '10,10'),
        ('-s', '10,0'),
        ('-s', '10,5'),
    ])
    def test_ok_sigma(self, config, key, value):
        runner = CliRunner()
        options = ['-i', util.TEST_IMAGE_BINARY_JPG, '-l', '0,0,10,10', key, value]
        result = runner.invoke(commands.gaussian, options, obj=config)
        self.__assert_reslut(result)

    def __assert_reslut(self, result, output=None):
        assert result.exit_code == 0, result.output
        if output:
            with open(output, 'rb') as f:
                imagedata = f.read()
                imagetype = imghdr.what(None, h=imagedata)
        else:
            imagedata = result.output_bytes
            imagetype = imghdr.what(None, h=imagedata)
        assert imagetype == 'jpeg', imagetype


class TestCaseException(object):

    @pytest.fixture
    def config(self):
        obj = {}
        obj['profile'] = 'test'
        return obj

    @pytest.mark.parametrize('option', [
        ('test'),
        ('ips'),
        ('False'),
        ('123'),
    ])
    def test_invalid_command(self, config, option):
        runner = CliRunner()
        result = runner.invoke(commands.gaussian, [option], obj=config)
        assert result.exit_code == 2
        assert 'Usage: gaussian [OPTIONS]' in result.output
        assert 'Error: Missing option "-i" / "--input".' in result.output

    @pytest.mark.parametrize('option', [
        ('--test'),
        ('--ips'),
        ('--False'),
        ('--123'),
    ])
    def test_invalid_option(self, config, option):
        runner = CliRunner()
        result = runner.invoke(commands.gaussian, [option], obj=config)
        assert result.exit_code == 2
        assert 'Error: no such option' in result.output

    @pytest.mark.parametrize(('key', 'value'), [
        ('--input', 'test.jpg'),
        ('--input', './test.jpg'),
        ('--input', '~/test.jpg'),
        ('--input', '~/'),
        ('-i', 'test.jpg'),
        ('-i', './test.jpg'),
        ('-i', '~/test.jpg'),
        ('-i', '~/')
    ])
    def test_input_missing_path(self, config, key, value):
        runner = CliRunner()
        options = [key, value, '--location', '0,0,10,10', '-k', '1,1']
        result = runner.invoke(commands.gaussian, options, obj=config)
        assert result.exit_code == 1, result.output
        assert util.INVALID_MESSAGE in result.output

    @pytest.mark.parametrize(('key', 'value'), [
        ('--input', util.TEST_IMAGE_BINARY_TIFF),
        ('-i', util.TEST_IMAGE_BINARY_TIFF)
    ])
    def test_input_invalid_format_binary(self, config, key, value):
        runner = CliRunner()
        options = [key, value, '--location', '0,0,10,10', '-k', '1,1']
        result = runner.invoke(commands.gaussian, options, obj=config)
        assert result.exit_code == 1, result.output
        assert util.UNSUPPORTED_MESSAGE in result.output

    @pytest.mark.parametrize(('key', 'value'), [
        ('--input', util.TEST_IMAGE_URI_TIFF),
        ('-i', util.TEST_IMAGE_URI_TIFF)
    ])
    def test_input_invalid_format_url(self, config, key, value):
        runner = CliRunner()
        options = [key, value, '--location', '0,0,10,10', '-k', '1,1']
        result = runner.invoke(commands.gaussian, options, obj=config)
        assert result.exit_code == 1, result.output
        assert util.UNPROCESSABLE_MESSAGE in result.output

    @pytest.mark.parametrize(('key', 'value'), [
        ('--output', 'output'),
        ('--output', 'output.png'),
        ('-o', 'output'),
        ('-o', 'output.png'),
    ])
    def test_output_invalid_format(self, config, key, value):
        runner = CliRunner()
        options = ['-i', util.TEST_IMAGE_BINARY_JPG, '--location', '0,0,10,10', '-k', '1,1', key, value]
        result = runner.invoke(commands.gaussian, options, obj=config)
        assert result.exit_code == 2, result.output
        assert util.INVALID_OUTPUT in result.output

    @pytest.mark.parametrize(('key', 'value'), [
        ('--location', ''),
        ('--location', '1'),
        ('--location', '1,1'),
        ('--location', '1,1,1'),
        ('--location', '1,1,1,a'),
        ('--location', '1,1,1,1,1'),
        ('-l', ''),
        ('-l', '1'),
        ('-l', '1,1'),
        ('-l', '1,1,1'),
        ('-l', '1,1,1,a'),
        ('-l', '1,1,1,1,1'),
    ])
    def test_location_invalid_format(self, config, key, value):
        runner = CliRunner()
        options = ['-i', util.TEST_IMAGE_BINARY_JPG, key, value, '-k', '1,1']
        result = runner.invoke(commands.gaussian, options, obj=config)
        assert result.exit_code == 2, result.output
        assert util.INVALID_LOCATION in result.output

    @pytest.mark.parametrize(('key', 'value'), [
        ('--locations_shape', ''),
        ('--locations_shape', '1'),
        ('--locations_shape', 'abc'),
    ])
    def test_locations_shape_invalid_format(self, config, key, value):
        runner = CliRunner()
        options = ['-i', util.TEST_IMAGE_BINARY_JPG, '--location', '0,0,10,10', key, value]
        result = runner.invoke(commands.gaussian, options, obj=config)
        assert result.exit_code == 2, result.output
        assert util.INVALID_LOCATIONS_SHAPE in result.output

    @pytest.mark.parametrize(('key', 'value'), [
        ('--locations_edge', ''),
        ('--locations_edge', '1'),
        ('--locations_edge', 'abc'),
    ])
    def test_locations_edge_invalid_format(self, config, key, value):
        runner = CliRunner()
        options = ['-i', util.TEST_IMAGE_BINARY_JPG, '--location', '0,0,10,10', key, value]
        result = runner.invoke(commands.gaussian, options, obj=config)
        assert result.exit_code == 2, result.output
        assert util.INVALID_LOCATIONS_EDGE in result.output

    @pytest.mark.parametrize(('key', 'value'), [
        ('--ksize', ''),
        ('--ksize', '1'),
        ('--ksize', '1,a'),
        ('--ksize', '1,1,1'),
        ('-k', ''),
        ('-k', '1'),
        ('-k', '1,a'),
        ('-k', '1,1,'),
        ('-k', '1,1,1'),
    ])
    def test_ksize_invalid_format(self, config, key, value):
        runner = CliRunner()
        options = ['-i', util.TEST_IMAGE_BINARY_JPG, '--location', '0,0,10,10', key, value]
        result = runner.invoke(commands.gaussian, options, obj=config)
        assert result.exit_code == 2, result.output
        assert INVALID_KSIZE in result.output

    @pytest.mark.parametrize(('key', 'value'), [
        ('--sigma', ''),
        ('--sigma', '1'),
        ('--sigma', '1,a'),
        ('--sigma', '1,1,1'),
        ('-s', ''),
        ('-s', '1'),
        ('-s', '1,a'),
        ('-s', '1,1,'),
        ('-s', '1,1,1'),
    ])
    def test_sigma_invalid_format(self, config, key, value):
        runner = CliRunner()
        options = ['-i', util.TEST_IMAGE_BINARY_JPG, '--location', '0,0,10,10', key, value]
        result = runner.invoke(commands.gaussian, options, obj=config)
        assert result.exit_code == 2, result.output
        assert INVALID_SIGMA in result.output
