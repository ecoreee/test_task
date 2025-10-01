import pytest
import requests


@pytest.fixture
def get_api():
    request = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    all_heroes_tests = request.json()
    return all_heroes_tests