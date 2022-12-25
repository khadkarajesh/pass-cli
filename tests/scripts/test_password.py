from click.testing import CliRunner

from pm import generate


def test_generate():
    runner = CliRunner()
    result = runner.invoke(generate)
    assert result.exit_code == 0
    assert len(result.output.rstrip()) == 8

    result = runner.invoke(generate, ["--length", 10])
    assert result.exit_code == 0
    assert len(result.output.rstrip()) == 10

    result = runner.invoke(generate, ["-l", 10])
    assert result.exit_code == 0
    assert len(result.output.rstrip()) == 10
