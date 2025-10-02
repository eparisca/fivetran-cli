import json


def format_response_data(data) -> str:
    """Format the response"""
    return json.dumps(data, indent=2)
