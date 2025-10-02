import typer
from typing_extensions import Annotated

import private_link
from output import format_response_data

app = typer.Typer()


# @app.command()
# def create(name: Annotated[str, typer.Argument(help="System key name")]):
#     system_key.validate_name(name)
#     expiration_period = system_key.ExpirationPeriod.SIX_MONTHS.value
#     key = system_key.create(
#         name, expiration_period, system_key.DEFAULT_PERMISSIONS
#     )
#     print(format_response_data(key))


@app.command()
def get(name: Annotated[str, typer.Argument(help="Private Link name")]):
    """Get a private link by name"""
    response = private_link.get_by_name(name)
    print(format_response_data(response))


@app.command()
def list():
    """List all private links"""
    response = private_link.list_all()
    print(format_response_data(response))
