# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.
import pytest
from click.testing import CliRunner
from ricohcloudcli.vrs import commands as vrs
from . import util

TEST_IMAGE_BINARY_TIFF = 'tests/images/img_640x480.tiff'
TEST_IMAGE_BINARY_JPG = 'tests/images/test_2.jpg'
TEST_IMAGE_BINARY_PNG = 'tests/images/test_2.png'
TEST_BASE_URI = 'https://s3-ap-northeast-1.amazonaws.com/visualrecognition-test-images'
TEST_IMAGE_URI_TIFF = TEST_BASE_URI + '/04_blank/img_640x480.tiff'
TEST_IMAGE_URI_BLANK = TEST_BASE_URI + '/04_blank/img_640x480.jpg'
TEST_IMAGE_URI_JPG = TEST_BASE_URI + '/01_humans/resized/humans_1_640x480.jpg'
TEST_IMAGE_URI_PNG = TEST_BASE_URI + '/01_humans/resized/humans_1_640x480.png'


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
        result = runner.invoke(vrs.remove_face, [option], obj=config)
        assert result.exit_code == 0
        assert 'Remove face from face collection.' in result.output


class TestCaseException(object):

    @pytest.fixture
    def config(self):
        obj = {'profile': 'test'}
        return obj

    @pytest.mark.parametrize('option', [
        ('--test'),
        ('--vrs'),
        ('--False'),
        ('--123'),
    ])
    def test_invalid_option(self, config, option):
        runner = CliRunner()
        result = runner.invoke(vrs.remove_face, [option], obj=config)
        assert result.exit_code == 2
        assert 'Error: no such option' in result.output
