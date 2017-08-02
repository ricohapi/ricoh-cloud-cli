# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

'''
RICOH Cloud CLI entry point.
'''
import click
import ricohcloudcli
from .config.commands import configure
from .vrs.commands import vrs

HELP_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
HELP_PROFILE = 'Use a specific profile from your credential file.'

@click.group(help='RICOH Cloud CLI', context_settings=HELP_CONTEXT_SETTINGS)
@click.option('--profile', type=str, default='default', help=HELP_PROFILE)
@click.version_option(version=ricohcloudcli.__version__, message='%(version)s')
@click.pass_context
def rapi(ctx, profile):
    """This command is the entry point of the RICOH Cloud CLI."""
    ctx.obj['profile'] = profile


rapi.add_command(configure)
rapi.add_command(vrs)


def main():
    rapi(obj={})

if __name__ == '__main__':
    main()
