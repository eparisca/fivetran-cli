from api_client import atlas, atlas_paginated_get

# from logger import logger


def list_all():
    """List all private links"""
    endpoint = "private-links"
    return atlas_paginated_get(endpoint)


def get(id: str):
    """Get a groups"""
    endpoint = f"private-links/{id}"
    return atlas("GET", endpoint)


def get_by_name(name: str):
    """Get a private link by name"""
    private_links = list_all()
    for private_link in private_links:
        if private_link.get("name") == name:
            return private_link
    raise ValueError(f"Private Link with name {name} not found")
