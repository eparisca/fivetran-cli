from api_client import API_MAX_RESULT_LIMIT, atlas


def list_all_group_users(id: str):
    """List all users in a group"""
    endpoint = f"groups/{id}/users/?limit={API_MAX_RESULT_LIMIT}"
    return atlas("GET", endpoint)
