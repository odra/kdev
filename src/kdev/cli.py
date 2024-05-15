import sys

import click

from . import errors


@click.group
def cli() -> None:
    pass


@cli.command
def version() -> None:
    """
    Shows the program version.
    """
    raise errors.NotImplementedError()


@cli.command
@click.argument('config_path', type=click.Path())
def info(config_path: click.Path) -> None:
    """
    Inspects a config file and prints its info, including default variables in use.
    """
    raise errors.NotImplementedError()


@cli.command
@click.argument('config_path', type=click.Path())
def run(config_path: click.Path) -> None:
    """
    Run kdev based on a config definition.
    """
    raise errors.NotImplementedError()


def entrypoint() -> None:
    try:
        cli()
    except errors.KdevError as e:
        click.echo(str(e))
        sys.exit(e.errno)
