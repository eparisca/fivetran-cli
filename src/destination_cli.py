import typer
from typing_extensions import Annotated

import destination
import group
from output import format_response_data

app = typer.Typer()


@app.command()
def get(name: Annotated[str, typer.Argument(help="Destination name")]):
    """Get a destination by name"""
    response = group.get_by_name(name)
    response = destination.get(response.get("id"))
    print(format_response_data(response))


@app.command()
def list():
    """List all destinations"""
    response = destination.list_all()
    print(format_response_data(response))
