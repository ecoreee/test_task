import pytest
import requests
from config import url_api


@pytest.fixture
def get_heroes_data():
    request = requests.get(url_api)
    request.raise_for_status()
    all_heroes_tests = request.json()
    return all_heroes_tests