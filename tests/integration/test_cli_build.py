import sys
from unittest import mock

from click import Group
from click.testing import CliRunner


class TestBuildCommand:
    def test_calls_build(self, runner: CliRunner, cli: Group) -> None:
        with mock.patch("subprocess.run") as mocked_run:
            runner.invoke(cli, ["build"])

        mocked_run.assert_has_calls(
            [mock.call([sys.executable, "-m", "build"], check=True)]
        )
