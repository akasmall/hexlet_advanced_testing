import os
# тут мне она не нужна
# from functions import get_function
# тут для теста IDE добавляю импорт
from src.m3_p14_l5_dependency_inversion_app import _right, _fail1

# тут мне она не нужна
# get_files_count = get_function()


# BEGIN (write your solution here)
# @pytest.fixture
# def get_path_dir(path_dir):
#     pass


def test_get_files_count_right():
    get_files_count_right = _right("./tests/fixtures/m3_p14_l5", os.getpid)
    assert get_files_count_right == 6


def test_get_files_count_fail():
    get_files_count_fail1 = _fail1("./tests/fixtures/m3_p14_l5", os.getpid)
    assert get_files_count_fail1 == 3

# END

# !tests / test_solution.py
# *Протестируйте функцию get_files_count(), которая считает количество всех
# файлов в указанной директории и всех поддиректориях:

# *get_files_count = get_function()

# *get_files_count("/path/to/directory")  # 4
# У этой функции есть дополнительное поведение. Во время обхода файлов она
# записывает информацию о задействованных файлах в специальный файл — журнал
# действий(лог).

# Все, что мы хотим – чтобы функция считала количество файлов.
# При этом запись в файл является нежелательным побочным
# эффектом — каждый запуск будет заполнять какой - то файл,
# который мы никак не используем. Попробуем избавиться от этого эффекта.
# *Для записи в файл функция get_files_count(), использует другую функцию,
# которую можно подменить:


# *def get_files_count(filepath, log=write_data_to_file):
#     # Где-то внутри во время работы
#     write_data_to_file(f"File {name} has been processed")


# Для подмены нужно передать вторым параметром функцию - пустышку,
# которая не будет ничего делать. В таком случае ее вызов внутри
# *get_files_count() хоть и отработает, но не породит побочного эффекта.

# ?Подсказки
# *Передайте этой функции путь до директории внутри fixtures и убедитесь в том,
# *что она правильно посчитала количество файлов внутри

# !решение ментора
# ?import os
# ?from functions import get_function

# ?get_files_count = get_function()

# ?# BEGIN
# *def get_fixture_path(name):
#     return os.path.join('fixtures', name)


# *def test_get_files_count():
# ?    # flat можно не тестировать так как nested покрывает и flat тоже
#     directory_path = get_fixture_path("nested")
#     files_count = get_files_count(directory_path, lambda: None)
#     assert files_count == 4
# ?# END
