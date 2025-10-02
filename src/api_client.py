import os
from typing import Dict, List, Optional

import requests
from requests.auth import HTTPBasicAuth

from logger import logger

API_MAX_RESULT_LIMIT = 1000


def get_basic_auth() -> HTTPBasicAuth:
    """Encode the credentials to base64"""
    api_key = os.environ.get("FIVETRAN_APIKEY")
    api_secret = os.environ.get("FIVETRAN_APISECRET")
    return HTTPBasicAuth(api_key, api_secret)


def atlas(method: str, endpoint: str, payload: dict = None) -> dict:
    """Make a request to the Fivetran REST API"""
    basic_auth = get_basic_auth()
    base_url = "https://api.fivetran.com/v1"
    url = f"{base_url}/{endpoint}"
    headers = {
        "Accept": "application/json",
        "content-type": "application/json",
    }
    try:
        response = requests.request(method, url, json=payload, headers=headers, auth=basic_auth)
        response.raise_for_status()
        logger.info(f"{method} {url}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(e)
        raise e


def atlas_paginated_get(endpoint: str):
    """Make a paginated GET request to the Fivetran REST API"""
    items: List[Dict] = []
    next_cursor: Optional[str] = None
    while True:
        # build query params
        params = "?limit=100"
        if next_cursor:
            params += f"&cursor={next_cursor}"
        # fetch one page
        response = atlas("GET", f"{endpoint}/{params}")
        data = response.get("data", {})
        items.extend(data.get("items", []))
        # prepare for next page (or break)
        next_cursor = data.get("next_cursor")
        if not next_cursor:
            break
    return items
