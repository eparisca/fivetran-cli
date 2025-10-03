from api_client import atlas, atlas_paginated_get

# from logger import logger


def list_all_private_links():
    """List all Private Links"""
    endpoint = "private-links"
    return atlas_paginated_get(endpoint)


def get_private_link(id: str):
    """Get a Private Link"""
    endpoint = f"private-links/{id}"
    return atlas("GET", endpoint)


def get_private_link_by_name(name: str):
    """Get a Private Link by name"""
    private_links = list_all_private_links()
    for private_link in private_links:
        if private_link.get("name") == name:
            return private_link
    raise ValueError(f"Private Link with name {name} not found")
