# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

'''
Utility functions for the vrs package.
'''
import click
from ricohcloudsdk.auth.client import AuthClient
from ricohcloudsdk.vrs.client import VisualRecognition
from ricohcloudsdk.vrs.util import get_type
from ..config.util import get_credential_info, CLIENT_ID, CLIENT_SECRET

HELP_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
HELP_COMPARE_FACES = 'Compare faces in two requested resources and returns how similar they are.'
HELP_DETECT_FACES = 'Detect the faces of the requested image.'
HELP_DETECT_HUMANS = 'Detect the humans of the requested image.'
HELP_LIST_COLLECTIONS = 'List face collections.'
HELP_CREATE_COLLECTION = 'Create face collection.'
HELP_DELETE_COLLECTION = 'Delete face collection.'
HELP_LIST_FACES = 'List faces in face collection.'
HELP_ADD_FACE = 'Add face in face collection.'
HELP_REMOVE_FACE = 'Remove face from face collection.'
HELP_IMAGE = 'Specify image URI or local file path.'

HELP_SOURCE = 'Specify source image URI or local file path.'
HELP_TARGET = 'Specify target image URI, local file path, or ID of the face collection.'
HELP_IMAGE = 'Specify image URI or local file path.'
HELP_MAX_RESULTS = 'The valid range is 1 ~ 1000. The default is 10.'

INDENT_SIZE = 4


def create_vr_client(profile):
    """This function create Visual Recognition Service object."""
    credential = get_credential_info(profile)
    auth_client = AuthClient(credential[CLIENT_ID], credential[CLIENT_SECRET])
    vr_client = VisualRecognition(auth_client)
    return vr_client
