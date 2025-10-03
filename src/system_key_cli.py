import typer
from typing_extensions import Annotated

from output import format_response_data
from system_key import (
    DEFAULT_PERMISSIONS,
    ExpirationPeriod,
    create_system_key,
    get_system_key,
    list_all_system_keys,
    rotate_system_key,
    update_system_key,
    validate_system_key_name,
)

app = typer.Typer()


@app.command()
def create(name: Annotated[str, typer.Argument(help="System key name")]):
    """Create a new system key"""
    validate_system_key_name(name)
    expiration_period = ExpirationPeriod.SIX_MONTHS.value
    key = create_system_key(name, expiration_period, DEFAULT_PERMISSIONS)
    print(format_response_data(key))


@app.command()
def get(name: Annotated[str, typer.Argument(help="System key name")]):
    """Get a system key by name"""
    validate_system_key_name(name)
    key = get_system_key(name)
    print(format_response_data(key))


@app.command()
def rotate(key_id: Annotated[str, typer.Argument(help="System key ID")]):
    """Rotate a system key"""
    key = rotate_system_key(key_id)
    print(format_response_data(key))


@app.command()
def update(
    key_id: Annotated[str, typer.Argument(help="System key ID")],
    name: Annotated[str, typer.Argument(help="System key name")] = None,
):
    """Update a system key"""
    validate_system_key_name(name)
    key = update_system_key(key_id, name, DEFAULT_PERMISSIONS)
    print(format_response_data(key))


@app.command()
def list():
    """List all system keys"""
    response = list_all_system_keys()
    print(format_response_data(response))
