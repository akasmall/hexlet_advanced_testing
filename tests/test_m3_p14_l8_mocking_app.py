import os
from unittest.mock import Mock
# тут мне она не нужна
# from src.app import get_function
# тут для теста IDE добавляю импорт
# from src.app import _right, _fail1, _fail2
from src.m3_p14_l8_mocking_app import _right

# get_files_count = get_function()


def get_fixture_path(name):
    return os.path.join('.fixtures/m3_p14_l5', name)


# BEGIN (write your solution here)
def test_get_files_count():
    dir_path = get_fixture_path("nested")
    mock = Mock()
    files_count = _right(dir_path, mock)
    assert mock.call_args[0][0] == 'Go!'
    assert len(mock.mock_calls) == 1
# END

# !tests / test_solution.py
# ?Протестируйте функцию get_files_count(path, log), которая считает
# количество всех файлов в указанной директории и всех поддиректориях.
# В отличие от предыдущей версии задания, здесь нас интересует,
# что эта функция выполняет логирование с помощью функции log().
# *Мы хотим убедиться, что она один раз отправляет сообщение c текстом 'Go!'
# *в лог. Для этого придется воспользоваться моком.

# !Подсказки
# ?unittest.mock.call_count
# ?unittest.mock.call_args
# Обратите внимание в документации, где именно создается мок


# !решение ментора
# ?get_files_count = get_function()


# *def get_fixture_path(name):
#     return os.path.join('fixtures', name)


# ?# BEGIN
# *def test_get_files_count():
#     directory_path = get_fixture_path("nested")
#     mock = Mock()

#     get_files_count(directory_path, mock)
#     assert mock.call_count == 1
#     assert mock.call_args.args[0] == 'Go!'
# ?# END
