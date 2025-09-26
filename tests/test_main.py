import unittest
from function.search_function import find_tallest_char, all_heroes
import function.search_function as search_function

class testCharacteristic(unittest.TestCase):

    def test_find_tallest_male_hasjob(self):
        result = find_tallest_char('male', True)
        self.assertIsNotNone(result, 'Должен найтись хотя бы один персонаж с работой')
        self.assertEqual(result['appearance']['gender'].lower(), 'male')
        self.assertNotEqual(result['work']['occupation'], '-')

    def test_find_tallest_female_hasjob(self):
        result = find_tallest_char('female', True)
        self.assertIsNotNone(result, 'Должен найтись хотя бы один персонаж с работой')
        self.assertEqual(result['appearance']['gender'].lower(), 'female')
        self.assertNotEqual(result['work']['occupation'], '-')

    def test_find_tallest_male_hasnotjob(self):
        result = find_tallest_char('male', False)
        self.assertIsNotNone(result, 'Должен найтись хотя бы один персонаж без работы')
        self.assertEqual(result['appearance']['gender'].lower(), 'male')
        self.assertTrue(result['work']['occupation'] == '-' or result['work']['occupation'] == '')

    def test_find_tallest_female_hasnotjob(self):
        result = find_tallest_char('female', False)
        self.assertIsNotNone(result, 'Должен найтись хотя бы один персонаж без работы')
        self.assertEqual(result['appearance']['gender'].lower(), 'female')
        self.assertTrue(result['work']['occupation'] == '-' or result['work']['occupation'] == '')    

class testTallestChar(unittest.TestCase):
    
    def test_max_char_height(self):
        test_list = [
            {
                'name': 'Shadow Fiend',
                'appearance': {'gender': 'male', 'height': ["6'7"]},
                'work': {'occupation': 'Mid winner'}
            },
            {
                'name': 'Gerald of Rivia',
                'appearance': {'gender': 'male', 'height': ["6'0"]},
                'work': {'occupation': 'Witcher'}
            },
            {
                'name': 'Arthur Morgan',
                'appearance': {'gender': 'male', 'height': ["5'10"]},
                'work': {'occupation': 'Outlaw'}
            },
            {
                'name': 'Dallas',
                'appearance': {'gender': 'male', 'height': ["5'6"]},
                'work': {'occupation': 'Criminal, Member of PayDay Gang'}
            }
        ] 
        old_data = search_function.all_heroes
        search_function.all_heroes = test_list
        result = find_tallest_char('male', True)
        self.assertEqual(result['name'], 'Shadow Fiend')
        search_function.all_heroes = old_data

class testExistingChar(unittest.TestCase):
    
    def test_tallest_char_exist(self):
        test_list = [
            {
                'name': 'Shadow Fiend',
                'appearance': {'gender': 'male', 'height': ["-"]},
                'work': {'occupation': 'Mid winner'}
            },
            {
                'name': 'Gerald of Rivia',
                'appearance': {'gender': 'male', 'height': ["-"]},
                'work': {'occupation': 'Witcher'}
            },
            {
                'name': 'Arthur Morgan',
                'appearance': {'gender': 'male', 'height': ["-"]},
                'work': {'occupation': 'Outlaw'}
            },
            {
                'name': 'Dallas',
                'appearance': {'gender': 'male', 'height': ["-"]},
                'work': {'occupation': 'Criminal, Member of PayDay Gang'}
            }
        ] 
        old_data = search_function.all_heroes
        search_function.all_heroes = test_list
        result = find_tallest_char('male', True)
        self.assertEqual(result, None)
        search_function.all_heroes = old_data