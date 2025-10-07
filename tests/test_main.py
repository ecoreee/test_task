import pytest
import requests
from function.search_function import find_tallest_char
from config import url_api
import time


class TestCharCharacteristics:   
    def test_function_man_with_job(self):
        result = find_tallest_char('male', True)
        if result is not None:
            assert result['appearance']['gender'].lower() == 'male'
            assert result['work']['occupation'] not in ['-', '']
        else:
            pytest.skip("Не найдено персонажа с такими параметрами")

    def test_function_female_with_job(self):
        result = find_tallest_char('female', True)
        if result is not None:
            assert result['appearance']['gender'].lower() == 'female'
            assert result['work']['occupation'] not in ['', '-']
        else:
            pytest.skip("Не найдено персонажа с такими параметрами")
    
    def test_function_male_without_job(self):
        result = find_tallest_char('male', False)
        if result is not None:
            assert result['appearance']['gender'].lower() == 'male'
            assert result['work']['occupation'] in ['', '-']
        else:
            pytest.skip("Не найдено персонажа с такими параметрами")
    
    def test_function_female_without_job(self):
        result = find_tallest_char('female', False)
        if result is not None:
            assert result['appearance']['gender'].lower() == 'female'
            assert result['work']['occupation'] in ['', '-']
        else:
            pytest.skip("Не найдено персонажа с такими параметрами")


class TestAPIInvalidRequest:
    def test_unknown_gender(self):
        result = find_tallest_char('unknown_gender', True)
        assert result is None



class TestTallestChar:
    def test_find_tallest_char(self, get_heroes_data):
        result = find_tallest_char('male', True)
        if result is not None:
            assert result['name'] == 'Utgard-Loki'
            assert result['appearance']['gender'].lower() == 'male'
            assert result['work']['occupation'] not in ['', '-']