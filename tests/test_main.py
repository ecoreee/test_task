import pytest
import requests
from function.search_function import find_tallest_char
import time


class TestResponseAPI:
    def test_API_status_and_response_time(self):
        start_time = time.time()
        r = requests.get('https://akabab.github.io/superhero-api/api/all.json')
        all_heroes_list = r.json()
        end_time = time.time()
        response_time = end_time - start_time
        assert r.status_code == 200
        assert response_time < 10


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
    def test_find_tallest_char(self, get_api):
        heroes_list = []
        for hero in get_api:
            if 'appearance' in hero and 'work' in hero:
                if 'gender' in hero['appearance'] and 'occupation' in hero['work']:
                    job_exist = hero['work']['occupation'] != '-' and hero['work']['occupation'] != ''
                    if hero['appearance']['gender'].lower() == 'male' and job_exist == True:
                        heroes_list.append(hero)
        result = find_tallest_char('male', True)
        if result is not None and heroes_list is not None:
            tallest_char_cm = None
            current_max_height_cm = 0
            for hero in heroes_list:
                if (hero['appearance']['height'][1] != '0 cm' and hero['appearance']['height'][1] != ''):
                    if 'cm' in hero['appearance']['height'][1]:
                        height = float(hero['appearance']['height'][1].replace(' cm', ''))
                    if 'meter' in hero['appearance']['height'][1]:
                        height = float(hero['appearance']['height'][1].replace(' meters', ''))
                        height *= 100
                    if height > current_max_height_cm:
                        current_max_height_cm = height
                        tallest_char_cm = hero
            if tallest_char_cm is not None:
                assert result['name'] == tallest_char_cm['name']