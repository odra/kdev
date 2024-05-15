import os

import pytest


@pytest.fixture
def testdir() -> str:
    return os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def fixdir(testdir) -> str:
    return f'{testdir}/fixtures'
