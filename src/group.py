from api_client import atlas, atlas_paginated_get


def list_all_groups():
    """List all groups"""
    endpoint = "groups"
    return atlas_paginated_get(endpoint)


def get_group(id: str):
    """Get a group"""
    endpoint = f"groups/{id}"
    return atlas("GET", endpoint)


def get_group_by_name(name: str):
    """Get a group by name"""
    groups = list_all_groups()
    for group in groups:
        if group.get("name") == name:
            return group
    raise ValueError(f"Group with name {name} not found")
