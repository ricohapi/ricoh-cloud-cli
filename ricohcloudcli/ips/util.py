# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

'''
Utility functions for the ips package.
'''
import click
from ricohcloudsdk.auth.client import AuthClient
from ricohcloudsdk.ips.client import ImageProcessing
from ..config.util import get_credential_info, CLIENT_ID, CLIENT_SECRET


def create_ips_client(profile):
    """This function create Image Processing Service object."""
    credential = get_credential_info(profile)
    auth_client = AuthClient(credential[CLIENT_ID], credential[CLIENT_SECRET])
    return ImageProcessing(auth_client)
