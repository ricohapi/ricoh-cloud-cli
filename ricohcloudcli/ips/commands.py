# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

'''
Sub commands for Image Processing Service.
'''
import click
from .filter.commands import filter

HELP_IPS = 'Image Processing Service'
HELP_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(help=HELP_IPS, context_settings=HELP_CONTEXT_SETTINGS)
@click.pass_context
def ips(ctx):
    """This command is the entry point for the Image Processing Service."""
    pass


ips.add_command(filter)
