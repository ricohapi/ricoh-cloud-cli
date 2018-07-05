# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

'''
filter commands for Image Processing Service.
'''
import click
from . import util
from .types.blur import blur
from .types.gaussian import gaussian
from .types.median import median


@click.group(help=util.HELP_FILTER, context_settings=util.CONTEXT_SETTINGS)
@click.pass_context
def filter(ctx):
    """This command is the entry point for filter."""
    pass


filter.add_command(blur)
filter.add_command(gaussian)
filter.add_command(median)
