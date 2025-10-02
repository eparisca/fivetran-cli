import re
from enum import Enum

from api_client import API_MAX_RESULT_LIMIT, atlas
from logger import logger


class ExpirationPeriod(Enum):
    ONE_WEEK = "ONE_WEEK"
    ONE_MONTH = "ONE_MONTH"
    THREE_MONTHS = "THREE_MONTHS"
    SIX_MONTHS = "SIX_MONTHS"
    INFINITE = "INFINITE"


DEFAULT_PERMISSIONS = [{"access_level": "READ", "resource_type": "DESTINATION"}]


def validate_name(name: str):
    """Validate the system key name"""
    # key name must start with a letter or underscore, and only contain letters, numbers or underscores
    pattern = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*$")
    if not pattern.match(name):
        raise ValueError("Invalid system key name")


def create(name: str, expiration_period: str, permissions: list):
    """Create a new system key"""
    endpoint = "system-keys"
    payload = {
        "name": name,
        "expiration_period": expiration_period,
        "permissions": permissions,
    }
    logger.info(f"Creating system key with payload: {payload}")
    return atlas("POST", endpoint, payload=payload)


def get(name: str):
    """Get a system key"""
    system_keys = list_all()
    # filter items by name
    system_key = next((item for item in system_keys if item["name"] == name), None)
    return system_key


def update(key_id: str, name: str, permissions: list):
    """Update a system key"""
    endpoint = f"system-keys/{key_id}"
    payload = {"name": name, "permissions": permissions}
    logger.info(f"Updating system key with payload: {payload}")
    return atlas("PATCH", endpoint, payload=payload)


def rotate(key_id: str):
    """Rotate a system key"""
    endpoint = f"system-keys/{key_id}/rotate"
    payload = {"expiration_period": "SIX_MONTHS"}
    logger.info(f"Rotating system key with payload: {payload}")
    return atlas("POST", endpoint, payload=payload)


def list_all():
    """List all system keys"""
    endpoint = f"system-keys/?limit={API_MAX_RESULT_LIMIT}"
    response = atlas("GET", endpoint)["data"]
    return response["items"]
