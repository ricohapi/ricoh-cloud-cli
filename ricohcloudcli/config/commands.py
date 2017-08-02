# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

'''
Sub commands for configuration.
'''
import os
import json
import collections
from collections import OrderedDict
import click
from .util import (CLIENT_ID, CLIENT_SECRET,
                   CREDENTIALS_FILE_PATH, CREDENTIALS_DIR_PATH)


@click.command(help='Set your configuration with prompt')
@click.option('--profile', type=str, default='default', help='Additional configure')
def configure(profile):
    """This command configure the credentials."""
    rapi_client_id = click.prompt(
        'RAPI Client ID', type=str, hide_input=True, prompt_suffix=': ')
    rapi_client_secret = click.prompt(
        'RAPI Client Secret', type=str, hide_input=True,  prompt_suffix=': ')
    credentials_json = {}
    if os.path.isfile(CREDENTIALS_FILE_PATH):
        with open(CREDENTIALS_FILE_PATH, 'r') as f:
            decoder = json.JSONDecoder(
                object_pairs_hook=collections.OrderedDict)
            credentials_json = decoder.decode(f.read())
    if not os.path.exists(CREDENTIALS_DIR_PATH):
        os.mkdir(CREDENTIALS_DIR_PATH)
    os.chmod(CREDENTIALS_DIR_PATH, 0o700)
    credential = OrderedDict()
    credential[CLIENT_ID] = rapi_client_id
    credential[CLIENT_SECRET] = rapi_client_secret
    credentials_json[profile] = credential
    with open(CREDENTIALS_FILE_PATH, 'w') as f:
        json.dump(credentials_json, f, separators=(',', ': '), indent=2)
