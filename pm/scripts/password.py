import random
import string

import click


@click.command(help="generates password of given length")
@click.option(
    "--length", "-l", default=8, help="length of password", show_default=True
)  # noqa: E501
def generate(length: int) -> None:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    click.echo(password)
