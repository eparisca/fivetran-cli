import typer
from typing_extensions import Annotated

from output import format_response_data
from private_link import get_private_link_by_name, list_all_private_links

app = typer.Typer()


@app.command()
def get(name: Annotated[str, typer.Argument(help="Private Link name")]):
    """Get a private link by name"""
    response = get_private_link_by_name(name)
    print(format_response_data(response))


@app.command()
def list():
    """List all private links"""
    response = list_all_private_links()
    print(format_response_data(response))
