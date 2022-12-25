import click

from .password import generate


def add(a: int, b: int) -> int:
    return a + b


@click.group()
def cli() -> None:
    """
    PM (Password Manager) CLI
    """
    pass


cli.add_command(generate)

if __name__ == "__main__":
    cli()
