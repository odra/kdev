from kdev.cli import cli
from kdev import __version__ as kdev_version


def test_version(cli_runner):
    res = cli_runner.invoke(cli, ['version'])

    assert res.exit_code == 0
    assert res.output.strip() == f'v{kdev_version}'
