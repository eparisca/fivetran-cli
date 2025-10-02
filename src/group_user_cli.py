import typer
from typing_extensions import Annotated

import group_user
from output import format_response_data

app = typer.Typer()


@app.command()
def list(id: Annotated[str, typer.Argument(help="Group ID")]):
    """List all group users"""
    response = group_user.list_all(id)
    print(format_response_data(response))
