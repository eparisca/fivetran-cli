import typer
from typing_extensions import Annotated

from group import get_group_by_name, list_all_groups
from output import format_response_data

app = typer.Typer()


@app.command()
def list():
    """List all groups"""
    response = list_all_groups()
    print(format_response_data(response))


@app.command()
def get(name: Annotated[str, typer.Argument(help="Group name")]):
    """Get a group by name"""
    response = get_group_by_name(name)
    print(format_response_data(response))
