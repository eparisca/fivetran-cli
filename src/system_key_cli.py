import typer
from typing_extensions import Annotated

import system_key
from output import format_response_data

app = typer.Typer()


@app.command()
def create(name: Annotated[str, typer.Argument(help="System key name")]):
    """Create a new system key"""
    system_key.validate_name(name)
    expiration_period = system_key.ExpirationPeriod.SIX_MONTHS.value
    key = system_key.create(name, expiration_period, system_key.DEFAULT_PERMISSIONS)
    print(format_response_data(key))


@app.command()
def get(name: Annotated[str, typer.Argument(help="System key name")]):
    """Get a system key by name"""
    system_key.validate_name(name)
    key = system_key.get(name)
    print(format_response_data(key))


@app.command()
def rotate(key_id: Annotated[str, typer.Argument(help="System key ID")]):
    """Rotate a system key"""
    key = system_key.rotate(key_id)
    print(format_response_data(key))


@app.command()
def update(
    key_id: Annotated[str, typer.Argument(help="System key ID")],
    name: Annotated[str, typer.Argument(help="System key name")] = None,
):
    """Update a system key"""
    system_key.validate_name(name)
    key = system_key.update(key_id, name, system_key.DEFAULT_PERMISSIONS)
    print(format_response_data(key))


@app.command()
def list():
    """List all system keys"""
    response = system_key.list_all()
    print(format_response_data(response))
