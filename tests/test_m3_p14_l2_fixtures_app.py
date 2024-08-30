import os   # надо использовать, а я не догадался как, см. ментора
import json
import yaml
from src.m3_p14_l2_fixtures_app import gen_solution


# добавлено для теста тут
parsers_right = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "csv": lambda data: data.strip().split(',')
}

# добавлено для теста тут
parsers_wrong1 = {
    "json": lambda data: [],
    "yaml": yaml.safe_load,
    "csv": lambda data: data.strip().split(',')
}

# добавлено для теста тут
parsers_wrong2 = {
    "json": json.loads,
    "yaml": lambda data: [],
    "csv": lambda data: data.strip().split(',')
}

# добавлено для теста тут
parsers_wrong3 = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "csv": lambda data: []
}

# to_html_list = get_function() # это должна быть рабочая строка
to_html_list = gen_solution(parsers_right)  # добавил для теста в реали
# строка выше

# BEGIN (write your solution here)


def test_get_function_csv():
    with open('./tests/fixtures/result.html', encoding='utf8') as f_res:
        data_html = f_res.read().strip('\n ')
    data_csv_html = to_html_list('./tests/fixtures/list.csv')
    data_json_html = to_html_list('./tests/fixtures/list.json')
    data_yaml_html = to_html_list('./tests/fixtures/list.yaml')
    assert data_csv_html == data_html
    assert data_json_html == data_html
    assert data_yaml_html == data_html


def test_get_function_csv_wrong1():
    data_csv_html = to_html_list('./tests/fixtures/list.csv')
    assert data_csv_html != []


def test_get_function_csv_wrong2():
    data_json_html = to_html_list('./tests/fixtures/list.json')
    assert data_json_html != []


def test_get_function_csv_wrong3():
    data_yaml_html = to_html_list('./tests/fixtures/list.yaml')
    assert data_yaml_html != []
# END

    # data_html = ''.join(line.rstrip(' ') for line in f_res)

# !tests / test_solution.py
# Протестируйте функцию, которая преобразует входные форматы в выходной HTML
# *. На вход она поддерживает форматы YML, JSON и CSV:

# *to_html_list = get_function()

# *html1 = to_html_list('/path/to/yaml/file')
# *html2 = to_html_list('/path/to/json/file')
# *html3 = to_html_list('/path/to/csv/file')
# Каждый из входных файлов для этой функции содержит список элементов,
# *из которых формируется элемент < ul > .
# Входные данные и выходной HTML можно подсмотреть в фикстурах.

# ?Ваша задача — пропустить через эту функцию входные файлы и сравнить результат
# работы функции с ожидаемым значением, находящимся
# *в файле fixtures / result.html.
# *Функция принимает на вход путь к файлу.

# ?Подсказки
# *strip() – позволяет удалять концевые пробелы


# !решение ментора
# ?import os
# ?from functions import get_function

# to_html_list = get_function()


# ?# BEGIN
# *def get_fixture_path(name):
# *    return os.path.join('fixtures', name)


# *f = open(get_fixture_path('result.html'))
# *expected = f.read().strip()


# *def test_with_json():
#     filepath = get_fixture_path('list.json')
#     actual = to_html_list(filepath)
#     assert actual == expected


# *def test_with_yaml():
#     filepath = get_fixture_path('list.yaml')
#     actual = to_html_list(filepath)
#     assert actual == expected


# *def test_with_csv():
#     filepath = get_fixture_path('list.csv')
#     actual = to_html_list(filepath)
#     assert actual == expected
# ?# END
