import typer
from typing_extensions import Annotated

import group
from output import format_response_data

app = typer.Typer()


@app.command()
def list():
    """List all groups"""
    response = group.list_all()
    print(format_response_data(response))


@app.command()
def get(name: Annotated[str, typer.Argument(help="Group name")]):
    """Get a group by name"""
    response = group.get_by_name(name)
    print(format_response_data(response))
