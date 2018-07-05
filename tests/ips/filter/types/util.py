# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

# Image path
TEST_IMAGE_BINARY_TIFF = 'tests/images/img_640x480.tiff'
TEST_IMAGE_BINARY_JPG = 'tests/images/test_1.jpg'
TEST_IMAGE_BINARY_PNG = 'tests/images/test_1.png'
TEST_BASE_URI = 'https://s3-ap-northeast-1.amazonaws.com/visualrecognition-test-images'
TEST_IMAGE_URI_TIFF = TEST_BASE_URI + '/04_blank/img_640x480.tiff'
TEST_IMAGE_URI_BLANK = TEST_BASE_URI + '/04_blank/img_640x480.jpg'
TEST_IMAGE_URI_JPG = TEST_BASE_URI + '/02_faces/resized/faces_1_640x480.jpg'
TEST_IMAGE_URI_PNG = TEST_BASE_URI + '/02_faces/resized/faces_1_640x480.png'

# Invoke result output
INVALID_MESSAGE = 'Error: An invalid value was specified for one of the image resource parameters.'
UNSUPPORTED_MESSAGE = 'Error: One of the image resource was unsupported format.'
UNPROCESSABLE_MESSAGE = 'The operation contained in the request cannot processed.'
INVALID_OUTPUT = 'Error: Invalid value for "-o" / "--output": requires jpeg file path'
INVALID_LOCATION = 'Invalid value for "-l" / "--location": requires comma-separated 4 int values'
INVALID_LOCATIONS_SHAPE = 'Invalid value for "--locations_shape": invalid choice:'
INVALID_LOCATIONS_EDGE = 'Invalid value for "--locations_edge": invalid choice:'
INVALID_KSIZE = 'Invalid value for "-k" / "--ksize": requires comma-separated 2 int values'
