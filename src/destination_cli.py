import typer
from typing_extensions import Annotated

from destination import (
    get_destination,
    list_all_destinations,
    run_destination_setup_tests,
)
from group import get_group_by_name
from output import format_response_data

app = typer.Typer()


@app.command()
def get(name: Annotated[str, typer.Argument(help="Destination name")]):
    """Get a destination by name"""
    response = get_group_by_name(name)
    response = get_destination(response.get("id"))
    print(format_response_data(response))


@app.command()
def list():
    """List all destinations"""
    response = list_all_destinations()
    print(format_response_data(response))


@app.command()
def test(id: Annotated[str, typer.Argument(help="Destination ID")]):
    """Run destination setup tests"""
    response = run_destination_setup_tests(id)
    print(format_response_data(response))
