import typer
from typing_extensions import Annotated

from group_user import list_all_group_users
from output import format_response_data

app = typer.Typer()


@app.command()
def list(id: Annotated[str, typer.Argument(help="Group ID")]):
    """List all group users"""
    response = list_all_group_users(id)
    print(format_response_data(response))
