from click.testing import CliRunner
import os
from peeringdb import cli
import pytest


def test_get_deps():
    has_django = 0
    for dep in cli.get_deps("sqlite3"):
        if dep.startswith("django_peeringdb"):
            has_django += 1
    assert 1 == has_django


def test_config():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["conf_dump"], catch_exceptions=False)
    assert result.exit_code == 0


def test_drop_tables():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["depcheck"], catch_exceptions=False)
    result = runner.invoke(cli.cli, ["drop_tables"], catch_exceptions=False)
    assert result.exit_code == 0
