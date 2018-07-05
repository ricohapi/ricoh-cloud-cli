# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

'''
Utility functions for the config package.
'''
import os
import json

CLIENT_ID = 'RAPI_CLIENT_ID'
CLIENT_SECRET = 'RAPI_CLIENT_SECRET'
CREDENTIALS_DIR_PATH = os.path.expanduser('~/.rapi')
CREDENTIALS_FILE_PATH = os.path.join(CREDENTIALS_DIR_PATH, 'credentials.json')
CREDENTIALS_ERROR_STR = 'Your credentials are not set or invalid.\nYou can configure credentials by running "rapi configure".'


def get_credential_info(profile):
    """This function get the credential information from environment args or json file."""
    credentials = {}
    client_id = os.getenv(CLIENT_ID, None)
    client_secret = os.getenv(CLIENT_SECRET, None)
    if None in [client_id, client_secret]:
        if not os.path.isfile(CREDENTIALS_FILE_PATH):
            raise ValueError(CREDENTIALS_ERROR_STR)
        with open(CREDENTIALS_FILE_PATH) as f:
            credentials_json = json.load(f)
            if profile not in credentials_json:
                raise ValueError(CREDENTIALS_ERROR_STR)
            credentials = credentials_json[profile]
    else:
        credentials[CLIENT_ID] = client_id
        credentials[CLIENT_SECRET] = client_secret
    return credentials
