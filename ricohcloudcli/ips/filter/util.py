# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

'''
Utility functions for the filter package.
'''
import click
import functools

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'], max_content_width=256)

HELP_FILTER = 'Image Filtering'
HELP_INPUT = 'Specify the image URI or local file path.'
HELP_OUTPUT = 'Write to file instead stdout.'
HELP_LOCATION = """
Specify the location to filter with comma-separated integer values.
You can specify up to 100 locations, but be sure to specify at least one location.
Example:
\t-l 452,310,535,419 -l 1081,389,1202,508
"""
HELP_LOCATIONS_SHAPE = 'Specify the shape of locations.'
HELP_LOCATIONS_EDGE = 'Specify the edge of locations.'


class DefaultOutput(object):
    def write(self, message):
        click.echo(message, nl=False)


def common_params(func):
    @click.option('-i', '--input', required=True, help=HELP_INPUT, metavar='<uri_or_filepath>')
    @click.option('-o', '--output', type=click.File('wb'), help=HELP_OUTPUT, metavar='<filepath>', callback=validate_output)
    @click.option('-l', '--location', required=True, type=click.STRING, multiple=True, help=HELP_LOCATION, metavar='<left,top,right,bottom>', callback=split_location)
    @click.option('--locations_shape', type=click.Choice(['rectangle', 'min_enclosing_circle']), default='min_enclosing_circle', help=HELP_LOCATIONS_SHAPE)
    @click.option('--locations_edge', type=click.Choice(['none', 'blur']), default='blur', help=HELP_LOCATIONS_EDGE)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def validate_output(ctx, param, value):
    if not value:
        return DefaultOutput()
    if not value.name.lower().endswith(('.jpg', '.jpeg')):
        raise click.BadParameter('requires jpeg file path')
    return value


def split_option(value, to_type, sep, maxsplit):
    try:
        splitted = list(map(to_type, value.split(sep, maxsplit)))
        if len(splitted) != maxsplit:
            raise ValueError('over %d' % maxsplit)
        return splitted
    except ValueError:
        raise click.BadParameter('requires comma-separated %d %s values' % (maxsplit, to_type.__name__))


def split_location(ctx, param, value):
    ret = []
    for location in value:
        left, top, right, bottom = split_option(location, int, ',', 4)
        ret.append({'left': left, 'top': top, 'right': right, 'bottom': bottom})
    return ret
