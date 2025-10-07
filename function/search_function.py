import requests
from config import url_api

r = requests.get(url_api)
all_heroes = r.json()

def find_tallest_char(search_gender, has_job):
    found_heroes = []
    for hero in all_heroes:
        if 'appearance' in hero and 'work' in hero:
            if 'gender' in hero['appearance'] and 'occupation' in hero['work']:
                job_exist = hero['work']['occupation'] != '-' and hero['work']['occupation'] != ''
                if hero['appearance']['gender'].lower() == search_gender.lower() and job_exist == has_job:
                    found_heroes.append(hero)

    tallest_hero = None
    current_max_hero_height = 0
    height = 0
    for hero in found_heroes:
        if hero['appearance']['height'][0] != '-' and hero['appearance']['height'][0] != '':
            parts = hero['appearance']['height'][0].replace('"', '').split("'")
            if len(parts) == 2:
                feet, inches = parts
                if inches != '':
                    height = int(feet) * 30.48 + int(inches) * 2.54
            else:
                height = int(parts[0]) * 30.48
            if height != 0:
                if height > current_max_hero_height:
                    current_max_hero_height = height
                    tallest_hero = hero
    if tallest_hero is not None:
        tallest_hero['appearance']['convert_height'] = current_max_hero_height
        return tallest_hero
    else:
        return None