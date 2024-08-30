import os
import shutil
import pytest
# from functions import get_function
from src.m3_p14_l4_app import _right, _wrong

CONTENT_CONTENT = "content"

# prettify_html_file = get_function()


# BEGIN (write your solution here)
def get_fixture_path(path_dir, name):
    return os.path.join(path_dir, name)


path_file_before = get_fixture_path('./tests/fixtures', 'before.html')
path_file_after = get_fixture_path('./tests/fixtures', 'after.html')

with open(path_file_before, encoding='utf8') as fr:
    expected_read = fr.read()

with open(path_file_after, encoding='utf8') as fw:
    expected_write = fw.read()


def test_read_write_right(tmp_path):
    # создаю путь с файлом в tmp
    dir_path = tmp_path / "tests"
    dir_path.mkdir()
    dir_path = dir_path / "fuxture"
    dir_path.mkdir()
    tmp_full_file_after = dir_path / "after.html"
    # копирую конечный файл
    shutil.copy(path_file_after, tmp_full_file_after)
    # обрабатываю файл из tmp
    # prettify_html_file(tmp_full_file_after) это в практике надо использовать
    _right(tmp_full_file_after)
    # читаю из обработанного файла
    with open(path_file_after, encoding='utf8') as f_html:
        expected_html = f_html.read()
    assert expected_html == expected_write


def test_read_write_wrong(tmp_path):
    dir_path = tmp_path / "tests"
    dir_path.mkdir()
    dir_path = dir_path / "fuxture"
    dir_path.mkdir()
    tmp_full_file_before = dir_path / "before.html"
    shutil.copy(path_file_before, tmp_full_file_before)
    # обрабатываю файл из tmp
    # prettify_html_file(tmp_full_file_before)
    _wrong(tmp_full_file_before)

    with open(tmp_full_file_before, encoding='utf8') as f_html:
        expected_html = f_html.read()
    # тест должен падать поэтому при '==' он проходит,
    # а по логике в задании должно быть '!=' чтобы он прошел
    assert expected_html == expected_read

# END

# *FUNCTION_VERSION = right suppressor pass pytest tests
# *FUNCTION_VERSION =wrong suppressor fail pytest tests

# !tests / test_solution.py
# ?Протестируйте функцию, которая форматирует и изменяет указанный HTML - файл:

# *    # Содержимое файла до форматирования:
# *    # <div><p>Hello, <a href="https://hexlet.io">Hexlet</a></p></div>

# *prettify_html_file('/path/to/file')

# ?# Содержимое форматирования:
# # <div>
# #  <p>
# #   Hello,
# #   <a href="https://hexlet.io">
# #    Hexlet
# #   </a>
# #  </p>
# # </div>
# ?Подсказки
# *В директории fixtures лежат готовые фикстуры для тестов
# *Для копирования файлов воспользуйтесь модулем shutil
# *tmp_path


# !решение ментора
# import os
# import pytest
# import shutil
# from functions import get_function

# prettify_html_file = get_function()


# # BEGIN
# def read(file_path):
#     with open(file_path, 'r') as f:
#         result = f.read()
#     return result


# def get_fixture_path(name):
#     return os.path.join('fixtures', name)


# file_name = 'before.html'
# src = get_fixture_path(file_name)


# @pytest.fixture(scope='module')
# def expected():
#     return read(get_fixture_path('after.html'))


# @pytest.fixture
# def dest_file(tmp_path):
#     dest = tmp_path / file_name
#     shutil.copyfile(src, dest)
#     return dest


# def test_prettify(dest_file, expected):
#     prettify_html_file(dest_file)
#     actual = read(dest_file)
#     assert actual == expected
# # END

# !Фикстуры:

# *expected(): Эта фикстура определена с аргументом scope = 'module'.
# Это означает, что экземпляр этой фикстуры будет создан один раз для всего
# модуля и будет использоваться во всех тестах, которые зависят от нее.
# Это полезно, когда фикстура выполняет ресурсоемкие операции, такие
# как чтение файла, и Вы хотите избежать повторного выполнения этой
# операции для каждого теста.
# *dest_file(): Эта фикстура не имеет явно указанного scope,
# поэтому по умолчанию она будет иметь scope = 'function'. Это означает,
# что экземпляр этой фикстуры будет создан для каждого теста,
# который зависит от нее. Это полезно, когда Вы хотите,
# чтобы каждый тест работал с независимым экземпляром данных.

# *Аргумент scope = 'module':

# *Этот аргумент определяет, как долго будет существовать экземпляр фикстуры.
# В данном случае, scope = 'module' означает, что экземпляр будет
# существовать в течение всего времени выполнения модуля.
# Это позволяет избежать повторного выполнения ресурсоемких операций,
# таких как чтение файла, для каждого теста, который использует эту фикстуру.

# !Использование фикстур:

# ?В тесте test_prettify() используются две фикстуры: dest_file и expected.
# Фикстура dest_file создает временный файл, копируя содержимое файла before.
# html из директории fixtures. Фикстура expected читает содержимое файла after.
# html из директории fixtures и возвращает его.
# Затем тест вызывает функцию prettify_html_file() с временным файлом
# в качестве аргумента и сравнивает результат с ожидаемым содержимым,
# прочитанным из файла after.html.

# ?Общая идея состоит в том, чтобы использовать фикстуры для подготовки
# тестовых данных и ресурсов, которые могут быть повторно использованы
# в нескольких тестах. Это помогает сделать тесты более эффективными и
# поддерживаемыми.
