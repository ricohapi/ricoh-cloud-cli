# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

import click
from .. import util
from ...util import create_ips_client

HELP_COMMAND_SHORT = 'Applies image filters to an image using a median filter'
HELP_KSIZE = 'Specify the kernel size with int value.'


@click.command(short_help=HELP_COMMAND_SHORT, context_settings=util.CONTEXT_SETTINGS)
@util.common_params
@click.option('-k', '--ksize', type=click.INT, default=3, help=HELP_KSIZE, metavar='<size>')
@click.pass_context
def median(ctx, input, output, location, locations_shape, locations_edge, ksize):
    """
    \b
    Applies image filters to an image using a median filter, to standard output.
    Filter result is in JPEG format.
    """
    try:
        ips_client = create_ips_client(ctx.obj['profile'])
        options = {
            'locations': {
                'shape': locations_shape,
                'edge': locations_edge
            },
            'ksize': ksize
        }
        parameters = {
            'locations': location,
            'type': 'median',
            'options': options
        }
        res = ips_client.filter(input, parameters)
        output.write(res)
    except Exception as error:
        raise click.ClickException(error.args[0])
