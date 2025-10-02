from api_client import atlas, atlas_paginated_get


def list_all():
    """List all destinations"""
    endpoint = "destinations"
    return atlas_paginated_get(endpoint)


def get(id: str):
    """Get a destination"""
    endpoint = f"destinations/{id}"
    return atlas("GET", endpoint)


if __name__ == "__main__":
    destinations = list_all()
    print(destinations)
    # get("destination_id")
