# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

import click
from .. import util
from ...util import create_ips_client

HELP_COMMAND_SHORT = 'Applies image filters to an image using a gaussian filter'
HELP_KSIZE = 'Specify the gaussian kernel size with comma-separated int values.'
HELP_SIGMA = 'Specify the Gaussian kernel standard deviation with comma-separated float values.'


def split_ksize(ctx, param, value):
    width, height = util.split_option(value, int, ',', 2)
    return {'ksize_width': width, 'ksize_height': height}


def split_sigma(ctx, param, value):
    x, y = util.split_option(value, float, ',', 2)
    return {'sigma_x': x, 'sigma_y': y}


@click.command(short_help=HELP_COMMAND_SHORT, context_settings=util.CONTEXT_SETTINGS)
@util.common_params
@click.option('-k', '--ksize', type=click.STRING, default='1,1', help=HELP_KSIZE, metavar='<width,height>', callback=split_ksize)
@click.option('-s', '--sigma', type=click.STRING, default='0,0', help=HELP_SIGMA, metavar='<x,y>', callback=split_sigma)
@click.pass_context
def gaussian(ctx, input, output, location, locations_shape, locations_edge, ksize, sigma):
    """
    \b
    Applies image filters to an image using a gaussian filter, to standard output.
    Filter result is in JPEG format.
    """
    try:
        ips_client = create_ips_client(ctx.obj['profile'])
        options = {
            'locations': {
                'shape': locations_shape,
                'edge': locations_edge
            }
        }
        options.update(ksize)
        options.update(sigma)
        parameters = {
            'locations': location,
            'type': 'gaussian',
            'options': options
        }
        res = ips_client.filter(input, parameters)
        output.write(res)
    except Exception as error:
        raise click.ClickException(error.args[0])
