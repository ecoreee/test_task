from function.search_function import find_tallest_char

search_gender = input('Введите пол персонажа: ').lower()
while search_gender != 'male' and search_gender != 'female':
    print('Пожалуйста, введите \'male\' или \'female\'')
    search_gender = input('Введите пол персонажа: ').lower()
has_job = input('Имеет ли персонаж работу(true/false): ').lower()
while has_job != 'true' and has_job != 'false':
    print('Пожалуйста, введите \'true\' или \'false\'')
    has_job = input('Имеет ли персонаж работу(true/false): ').lower()
if has_job == 'true':
    has_job = True
elif has_job == 'false':
    has_job = False

tallest_hero = find_tallest_char(search_gender, has_job)
if tallest_hero is not None:
    print(f'''Самый высокий персонаж: {tallest_hero['name']}
Пол персонажа: {tallest_hero['appearance']['gender']}
Занятость персонажа: {tallest_hero['work']['occupation']}
Рост персонажа: {tallest_hero['appearance']['convert_height']} см''')
else:
    print('Герой с данными параметрами не был найден.')