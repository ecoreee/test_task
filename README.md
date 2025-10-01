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
+ Перед запуском тестов необходимо перейти в каталог test_task
#### Аргументы запуска:
+ pytest -v - запуск тестового фреймворка Pytest
+ -v - verbose, режим, чтобы видеть, какие тесты были запущены
#### Запуск API-тестов: 
```
pytest -v
```
#### Результат выполнения
```
============================ test session starts ============================
platform linux -- Python 3.12.3, pytest-8.4.2, pluggy-1.6.0 -- /home/ecoree/test_task/venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/ecoree/test_task
collected 7 items                                                                                                                 

tests/test_main.py::TestResponseAPI::test_API_status_and_response_time PASSED                                               [ 14%]
tests/test_main.py::TestCharCharacteristics::test_function_man_with_job PASSED                                              [ 28%]
tests/test_main.py::TestCharCharacteristics::test_function_female_with_job PASSED                                           [ 42%]
tests/test_main.py::TestCharCharacteristics::test_function_male_without_job PASSED                                          [ 57%]
tests/test_main.py::TestCharCharacteristics::test_function_female_without_job PASSED                                        [ 71%]
tests/test_main.py::TestAPIInvalidRequest::test_unknown_gender PASSED                                                       [ 85%]
tests/test_main.py::TestTallestChar::test_find_tallest_char PASSED                                                          [100%]

============================= 7 passed in 0.64s =============================
```