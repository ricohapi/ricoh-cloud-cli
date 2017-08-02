# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

import pytest
from click.testing import CliRunner
from ricohcloudcli.vrs import commands as vrs
from . import util

TEST_IMAGE_BINARY_TIFF = 'tests/images/img_640x480.tiff'
TEST_SOURCE_BINARY_JPG = 'tests/images/test_3a.jpg'
TEST_TARGET_BINARY_JPG = 'tests/images/test_3b.jpg'
TEST_SOURCE_BINARY_PNG = 'tests/images/test_3a.png'
TEST_TARGET_BINARY_PNG = 'tests/images/test_3b.png'
TEST_BASE_URI = 'https://s3-ap-northeast-1.amazonaws.com/visualrecognition-test-images'
TEST_IMAGE_URI_TIFF = TEST_BASE_URI + '/04_blank/img_640x480.tiff'
TEST_IMAGE_URI_BLANK = TEST_BASE_URI + '/04_blank/img_640x480.jpg'
TEST_SOURCE_URI_JPG = TEST_BASE_URI + '/03_face/resized/face_2a_720x480.jpg'
TEST_TARGET_URI_JPG = TEST_BASE_URI + '/03_face/resized/face_2b_720x480.jpg'
TEST_SOURCE_URI_PNG = TEST_BASE_URI + '/03_face/resized/face_2a_720x480.png'
TEST_TARGET_URI_PNG = TEST_BASE_URI + '/03_face/resized/face_2b_720x480.png'


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
        result = runner.invoke(vrs.compare_faces, [option], obj=config)
        assert result.exit_code == 0
        assert 'Compare faces' in result.output

    @pytest.mark.parametrize(('s_option', 't_option', 'source', 'target'), [
        ('-s', '-t', TEST_SOURCE_BINARY_JPG, TEST_TARGET_BINARY_JPG),
        ('-s', '-t', TEST_SOURCE_BINARY_PNG, TEST_TARGET_BINARY_PNG),
        ('-s', '-t', TEST_SOURCE_BINARY_JPG, TEST_TARGET_BINARY_PNG),
        ('-s', '-t', TEST_SOURCE_BINARY_PNG, TEST_TARGET_BINARY_JPG),
        ('--source-image', '--target-image', TEST_SOURCE_BINARY_JPG, TEST_TARGET_BINARY_JPG),
        ('--source-image', '--target-image', TEST_SOURCE_BINARY_PNG, TEST_TARGET_BINARY_PNG),
        ('--source-image', '--target-image', TEST_SOURCE_BINARY_JPG, TEST_TARGET_BINARY_PNG),
        ('--source-image', '--target-image', TEST_SOURCE_BINARY_PNG, TEST_TARGET_BINARY_JPG),
    ])
    def test_ok_compare_faces(self, config, s_option, t_option, source, target):
        runner = CliRunner()
        obj = {}
        obj['profile'] = 'test'
        result = runner.invoke(vrs.compare_faces, [
                               s_option, source, t_option, target], obj=config)
        assert result.exit_code == 0
        assert 'score' in result.output
        assert 'source' in result.output
        assert 'target' in result.output


class TestCaseException(object):

    @pytest.fixture
    def config(self):
        obj = {'profile': 'test'}
        return obj

    @pytest.mark.parametrize('option', [
        ('test'),
        ('vrs'),
        ('False'),
        ('123'),
    ])
    def test_invalid_command(self, config, option):
        runner = CliRunner()
        result = runner.invoke(vrs.compare_faces, [option], obj=config)
        assert result.exit_code == 2
        assert 'Usage: compare_faces [OPTIONS]' in result.output
        assert 'Error: Missing option "-s" / "--source-image".' in result.output

    @pytest.mark.parametrize('option', [
        ('--test'),
        ('--vrs'),
        ('--False'),
        ('--123'),
    ])
    def test_invalid_option(self, config, option):
        runner = CliRunner()
        result = runner.invoke(vrs.compare_faces, [option], obj=config)
        assert result.exit_code == 2
        assert 'Error: no such option' in result.output

    @pytest.mark.parametrize(('option', 'missing_path'), [
        ('--source-image', 'test.jpg'),
        ('-s', 'test.jpg'),
    ])
    def test_missing_target_path(self, config, option, missing_path):
        runner = CliRunner()
        result = runner.invoke(vrs.compare_faces, [option, missing_path], obj=config)
        assert result.exit_code == 2
        assert 'Usage: compare_faces [OPTIONS]' in result.output
        assert 'Error: Missing option "-t" / "--target-image".' in result.output


    @pytest.mark.parametrize(('opt_s', 'source_img', 'opt_t', 'target_img'), [
        ('--source-image', TEST_IMAGE_BINARY_TIFF, '--target-image', TEST_IMAGE_BINARY_TIFF),
        ('-s', TEST_IMAGE_BINARY_TIFF, '-t', TEST_IMAGE_BINARY_TIFF)
    ])
    def test_invalid_format_binary(self, config, opt_s, source_img, opt_t, target_img):
        runner = CliRunner()
        result = runner.invoke(vrs.compare_faces, [opt_s, source_img, opt_t, target_img], obj=config)
        assert util.UNSUPPORTED_MESSAGE in result.output

    @pytest.mark.parametrize(('source', 'target'), [
        (TEST_IMAGE_URI_TIFF, TEST_IMAGE_URI_TIFF),
    ])
    def test_invalid_format_url(self, config, source, target):
        runner = CliRunner()
        result = runner.invoke(
            vrs.compare_faces, ['-s', source, '-t', target], obj=config)
        assert util.UNPROCESSABLE_MESSAGE in result.output
