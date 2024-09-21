import click

from . import __version__ as kdev_version


@click.group
def cli() -> None:
    """
    Kdev cli
    """


@cli.command
def version() -> None:
    """Shows program version"""
    click.echo(f'v{kdev_version}')


def run() -> None:
    """
    Run the kdev cli.
    """
    cli()
