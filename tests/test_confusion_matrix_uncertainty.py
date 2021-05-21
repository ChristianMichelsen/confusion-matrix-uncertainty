from typer.testing import CliRunner

from confusion_matrix_uncertainty.main import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "--install-completion" in result.stdout
