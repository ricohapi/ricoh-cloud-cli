# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.
import pytest
from click.testing import CliRunner
import ricohcloudcli.vrs.commands as vrs
from . import util

TEST_IMAGE_BINARY_TIFF = 'tests/images/img_640x480.tiff'
TEST_IMAGE_BINARY_JPG = 'tests/images/test_1.jpg'
TEST_IMAGE_BINARY_PNG = 'tests/images/test_1.png'
TEST_BASE_URI = 'https://s3-ap-northeast-1.amazonaws.com/visualrecognition-test-images'
TEST_IMAGE_URI_TIFF = TEST_BASE_URI + '/04_blank/img_640x480.tiff'
TEST_IMAGE_URI_BLANK = TEST_BASE_URI + '/04_blank/img_640x480.jpg'
TEST_IMAGE_URI_JPG = TEST_BASE_URI + '/02_faces/resized/faces_1_640x480.jpg'
TEST_IMAGE_URI_PNG = TEST_BASE_URI + '/02_faces/resized/faces_1_640x480.png'


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
        result = runner.invoke(vrs.detect_faces, [option], obj=config)
        assert result.exit_code == 0
        assert 'Detect the faces of the requested image.' in result.output

    @pytest.mark.parametrize('image', [
        (TEST_IMAGE_BINARY_JPG),
        (TEST_IMAGE_BINARY_PNG),
        (TEST_IMAGE_URI_JPG),
        (TEST_IMAGE_URI_PNG),
        (TEST_IMAGE_URI_BLANK)
    ])
    def test_ok_detect_faces(self, config, image):
        runner = CliRunner()
        result = runner.invoke(
            vrs.detect_faces, ['--image', image], obj=config)
        assert result.exit_code == 0
        assert 'faces' in result.output


class TestCaseException(object):

    @pytest.fixture
    def config(self):
        obj = {}
        obj['profile'] = 'test'
        return obj

    @pytest.mark.parametrize('option', [
        ('test'),
        ('vrs'),
        ('False'),
        ('123'),
    ])
    def test_invalid_command(self, config, option):
        runner = CliRunner()
        result = runner.invoke(vrs.detect_faces, [option], obj=config)
        assert result.exit_code == 2
        assert 'Usage: detect_faces [OPTIONS]' in result.output
        assert 'Error: Missing option "-i" / "--image".' in result.output

    @pytest.mark.parametrize('option', [
        ('--test'),
        ('--vrs'),
        ('--False'),
        ('--123'),
    ])
    def test_invalid_option(self, config, option):
        runner = CliRunner()
        result = runner.invoke(vrs.detect_faces, [option], obj=config)
        assert result.exit_code == 2
        assert 'Error: no such option' in result.output

    @pytest.mark.parametrize(('option', 'missing_path'), [
        ('--image', 'test.jpg'),
        ('--image', './test.jpg'),
        ('--image', '~/test.jpg'),
        ('--image', '~/'),
        ('-i', 'test.jpg'),
        ('-i', './test.jpg'),
        ('-i', '~/test.jpg'),
        ('-i', '~/')
    ])
    def test_missing_path(self, config, option, missing_path):
        runner = CliRunner()
        result = runner.invoke(
            vrs.detect_faces, [option, missing_path], obj=config)
        assert util.INVALID_MESSAGE in result.output

    @pytest.mark.parametrize(('option', 'invalid_format'), [
        ('--image', TEST_IMAGE_BINARY_TIFF),
        ('-i', TEST_IMAGE_BINARY_TIFF)
    ])
    def test_invalid_format_binary(self, config, option, invalid_format):
        runner = CliRunner()
        result = runner.invoke(
            vrs.detect_faces, [option, invalid_format], obj=config)
        assert util.UNSUPPORTED_MESSAGE in result.output

    @pytest.mark.parametrize(('option', 'invalid_format'), [
        ('--image', TEST_IMAGE_URI_TIFF),
        ('-i', TEST_IMAGE_URI_TIFF)
    ])
    def test_invalid_format_url(self, config, option, invalid_format):
        runner = CliRunner()
        result = runner.invoke(
            vrs.detect_faces, [option, invalid_format], obj=config)
        assert util.UNPROCESSABLE_MESSAGE in result.output
