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
@click.option('-s', '--source', required=True, help=util.HELP_SOURCE)
@click.option('-t', '--target', required=True, help=util.HELP_TARGET)
@click.option('--max_results', required=False, type=click.IntRange(1, 1000), help=util.HELP_MAX_RESULTS)
@click.pass_context
def compare_faces(ctx, source, target, max_results):
    """Compare faces."""
    try:
        vrs_client = util.create_vr_client(ctx.obj['profile'])
        results = vrs_client.compare_faces(source, target, max_results)
    except Exception as error:
        raise click.ClickException(error.args[0])
    if results.get('error'):
        raise click.ClickException(results['error']['message'])
    click.echo(json.dumps(results, indent=util.INDENT_SIZE))


@vrs.command(help=util.HELP_DETECT_FACES, context_settings=util.HELP_CONTEXT_SETTINGS)
@click.option('-i', '--image', required=True, help=util.HELP_IMAGE)
@click.pass_context
def detect_faces(ctx, image):
    """Detect faces."""
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
    """Detect humans."""
    try:
        vrs_client = util.create_vr_client(ctx.obj['profile'])
        results = vrs_client.detect_humans(image)
    except Exception as error:
        raise click.ClickException(error.args[0])
    if results.get('error'):
        raise click.ClickException(results['error']['message'])
    click.echo(json.dumps(results, indent=util.INDENT_SIZE))


@vrs.command(help=util.HELP_LIST_COLLECTIONS, context_settings=util.HELP_CONTEXT_SETTINGS)
@click.pass_context
def list_collections(ctx):
    """List face collections."""
    try:
        vrs_client = util.create_vr_client(ctx.obj['profile'])
        results = vrs_client.list_collections()
    except Exception as error:
        raise click.ClickException(error.args[0])
    if results.get('error'):
        raise click.ClickException(results['error']['message'])
    click.echo(json.dumps(results, indent=util.INDENT_SIZE))


@vrs.command(help=util.HELP_CREATE_COLLECTION, context_settings=util.HELP_CONTEXT_SETTINGS)
@click.pass_context
def create_collection(ctx):
    """Create face collection."""
    try:
        vrs_client = util.create_vr_client(ctx.obj['profile'])
        results = vrs_client.create_collection()
    except Exception as error:
        raise click.ClickException(error.args[0])
    if results.get('error'):
        raise click.ClickException(results['error']['message'])
    click.echo(json.dumps(results, indent=util.INDENT_SIZE))


@vrs.command(help=util.HELP_DELETE_COLLECTION, context_settings=util.HELP_CONTEXT_SETTINGS)
@click.argument('collection_id')
@click.pass_context
def delete_collection(ctx, collection_id):
    """Delete face collection."""
    try:
        vrs_client = util.create_vr_client(ctx.obj['profile'])
        results = vrs_client.delete_collection(collection_id)
    except Exception as error:
        raise click.ClickException(error.args[0])
    if isinstance(results, dict) and results.get('error'):
        raise click.ClickException(results['error']['message'])


@vrs.command(help=util.HELP_LIST_FACES, context_settings=util.HELP_CONTEXT_SETTINGS)
@click.argument('collection_id')
@click.pass_context
def list_faces(ctx, collection_id):
    """List faces in face collection."""
    try:
        vrs_client = util.create_vr_client(ctx.obj['profile'])
        results = vrs_client.list_faces(collection_id)
    except Exception as error:
        raise click.ClickException(error.args[0])
    if results.get('error'):
        raise click.ClickException(results['error']['message'])
    click.echo(json.dumps(results, indent=util.INDENT_SIZE))


@vrs.command(help=util.HELP_ADD_FACE, context_settings=util.HELP_CONTEXT_SETTINGS)
@click.option('-i', '--image', required=True, help=util.HELP_IMAGE)
@click.argument('collection_id')
@click.pass_context
def add_face(ctx, collection_id, image):
    """Add face to face collection."""
    try:
        vrs_client = util.create_vr_client(ctx.obj['profile'])
        results = vrs_client.add_face(image, collection_id)
    except Exception as error:
        raise click.ClickException(error.args[0])
    if results.get('error'):
        raise click.ClickException(results['error']['message'])
    click.echo(json.dumps(results, indent=util.INDENT_SIZE))


@vrs.command(help=util.HELP_REMOVE_FACE, context_settings=util.HELP_CONTEXT_SETTINGS)
@click.option('--face_id', required=True, help=util.HELP_IMAGE)
@click.argument('collection_id')
@click.pass_context
def remove_face(ctx, collection_id, face_id):
    """Remove face from face collection."""
    try:
        vrs_client = util.create_vr_client(ctx.obj['profile'])
        results = vrs_client.remove_face(collection_id, face_id)
    except Exception as error:
        raise click.ClickException(error.args[0])
    if isinstance(results, dict) and results.get('error'):
        raise click.ClickException(results['error']['message'])
