from click.testing import CliRunner

import pytest


@pytest.fixture
def cli_runner():
    """
    Click cli runner to be used in other tests
    as a pytest fixture.
    """
    return CliRunner()
