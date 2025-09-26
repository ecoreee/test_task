## Тестовое задание на должность стажер QA Automation Engineer в Ozon Bank
Задание - https://github.com/akabab/superhero-api.git
### Требования к ПО
+ Python 3.10 и выше
### Копирование репозитория и установка зависимостей
```
git clone https://github.com/ecoreee/test_task.git
cd test_task
python3 -m venv venv
pip install -r requirements.txt
```
### Запуск тестов
+ Перед запуском тестов необходимо перейти в католог test_task
#### Аргументы запуска:
+ python -m unittest - запуск модуля unittest, как скрипт
+ -v - verbose, режим, чтобы видеть, какие тесты были запущены
#### Запуск API-тестов: 
```
python -m unittest tests/test_main.py -v
```
#### Результат выполнения
```
test_find_tallest_female_hasjob (tests.test_main.testCharacteristic.test_find_tallest_female_hasjob) ... ok
test_find_tallest_female_hasnotjob (tests.test_main.testCharacteristic.test_find_tallest_female_hasnotjob) ... ok
test_find_tallest_male_hasjob (tests.test_main.testCharacteristic.test_find_tallest_male_hasjob) ... ok
test_find_tallest_male_hasnotjob (tests.test_main.testCharacteristic.test_find_tallest_male_hasnotjob) ... ok
test_tallest_char_exist (tests.test_main.testExistingChar.test_tallest_char_exist) ... ok
test_max_char_height (tests.test_main.testTallestChar.test_max_char_height) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```