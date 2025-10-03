from api_client import atlas, atlas_paginated_get


def list_all_destinations():
    """List all destinations"""
    endpoint = "destinations"
    return atlas_paginated_get(endpoint)


def get_destination(id: str):
    """Get a destination"""
    endpoint = f"destinations/{id}"
    return atlas("GET", endpoint)


def run_destination_setup_tests(id: str):
    """Run Destination Setup Tests"""
    endpoint = f"destinations/{id}/test"
    payload = {
        "trust_certificates": True,
        "trust_fingerprints": True,
    }
    return atlas("POST", endpoint, payload)


if __name__ == "__main__":
    destinations = list_all_destinations()
    print(destinations)
    # get("destination_id")
