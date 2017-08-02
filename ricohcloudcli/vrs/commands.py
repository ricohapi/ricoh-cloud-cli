# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

'''
Sub commands for Visual Recognition Service.
'''
import json
import click
from . import util


@click.group(help='Visual Recognition Service', context_settings=util.HELP_CONTEXT_SETTINGS)
@click.pass_context
def vrs(ctx):
    """This command is the entry point for the Visual Recognition Service."""
    pass


@vrs.command(help=util.HELP_COMPARE_FACES, context_settings=util.HELP_CONTEXT_SETTINGS)
@click.option('-s', '--source-image', required=True, help=util.HELP_SOURCE_IMAGE)
@click.option('-t', '--target-image', required=True, help=util.HELP_TARGET_IMAGE)
@click.pass_context
def compare_faces(ctx, source_image, target_image):
    """Compare faces command."""
    try:
        vrs_client = util.create_vr_client(ctx.obj['profile'])
        results = vrs_client.compare_faces(source_image, target_image)
    except Exception as error:
        raise click.ClickException(error.args[0])
    if results.get('error'):
        raise click.ClickException(results['error']['message'])
    click.echo(json.dumps(results, indent=util.INDENT_SIZE))


@vrs.command(help=util.HELP_DETECT_FACES, context_settings=util.HELP_CONTEXT_SETTINGS)
@click.option('-i', '--image', required=True, help=util.HELP_IMAGE)
@click.pass_context
def detect_faces(ctx, image):
    """Detect faces command."""
    try:
        vrs_client = util.create_vr_client(ctx.obj['profile'])
        results = vrs_client.detect_faces(image)
    except Exception as error:
        raise click.ClickException(error.args[0])
    if results.get('error'):
        raise click.ClickException(results['error']['message'])
    click.echo(json.dumps(results, indent=util.INDENT_SIZE))


@vrs.command(help=util.HELP_DETECT_HUMANS, context_settings=util.HELP_CONTEXT_SETTINGS)
@click.option('-i', '--image', required=True, help=util.HELP_IMAGE)
@click.pass_context
def detect_humans(ctx, image):
    """Detect humans command."""
    try:
        vrs_client = util.create_vr_client(ctx.obj['profile'])
        results = vrs_client.detect_humans(image)
    except Exception as error:
        raise click.ClickException(error.args[0])
    if results.get('error'):
        raise click.ClickException(results['error']['message'])
    click.echo(json.dumps(results, indent=util.INDENT_SIZE))
