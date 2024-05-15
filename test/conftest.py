import os

import pytest
from click.testing import CliRunner


@pytest.fixture
def testdir() -> str:
    return os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def fixdir(testdir) -> str:
    return f'{testdir}/fixtures'


@pytest.fixture
def runner():
    return CliRunner()
