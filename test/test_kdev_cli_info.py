import errno

from kdev import cli, errors


def test_ok(runner):
    res = runner.invoke(cli.cli, ['info', 'config.yml'])

    assert res.exception == errors.NotImplementedError()
