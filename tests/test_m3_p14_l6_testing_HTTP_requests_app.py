from src.m3_p14_l6_testing_HTTP_requests_fake_client import FakeClient
# тут мне она не нужна
# from functions import get_function
# тут для теста IDE добавляю импорт
from src.m3_p14_l6_testing_HTTP_requests_app import get_user_main_language
# , _wrong1, _wrong2

# тут мне она не нужна
# get_user_main_language = get_function()


# BEGIN (write your solution here)


def test_get_user_main_language():
    data = [
        {"language": "php"},
        {"language": "javascript"},
        {"language": "python"},
        {"language": "python"},
        {"language": "php"},
        {"language": "python"},
        {"language": "javascript"},
        {"language": "python"},
        {"language": "php"},
        {"language": "python"},
    ]
    fake_default_client = FakeClient(data)
    max_count = get_user_main_language('hexlet', client=fake_default_client)
    assert max_count == "python"


def test_get_user_main_language_fail1():
    data = ''
    fake_default_client = FakeClient(data)
    fail1 = get_user_main_language('hexlet', client=fake_default_client)
    assert fail1 != ''

# END

# !tests / test_solution.py
# ?Протестируйте функцию get_user_main_language(user_name, client),
# ?которая определяет язык, на котором пользователь создал больше
# ?всего репозиториев.

# Для реализации этой задачи функция get_user_main_language() выполняет
# ?запрос к веб - сервису при помощи клиента client. Этот клиент извлекает
# все репозитории указанного пользователя по первому параметру user_name.
# *Каждый репозиторий в этом списке содержит указание основного языка
# *репозитория.
# Эта информация используется для поиска того языка,
# который используется чаще. Если список репозиториев пуст,
# функция возвращает None.
# ?Замените клиент тестовым двойником:

# # Запрос, который выполняет функция get_user_main_language()
# # Именно этот метод нужно будет подменить в фейковом клиенте
# *data = client.list_for_users(user_name)
# # Список репозиториев — data. У каждого репозитория может быть много полей,
# # но нас интересует ровно одно – language
# # Эти данные нужно подготовить в тестах для фейкового клиента
# *print(data)
# # [{ "language": "php", ... }, { "language": "javascript", ... }, ...]
# !src / FakeClient.py
# Реализуйте фейковый клиент и используйте этот клиент в тестах для подмены.


# !решение ментора
# from fake_client import FakeClient
# from functions import get_function
# get_user_main_language = get_function()


# ?# BEGIN
# *def test_get_user_main_language():
#     data = [
#         {"language": "ruby"},
#         {"language": "php"},
#         {"language": "java"},
#         {"language": "php"},
#         {"language": "js"},
#     ]

#     fake_client = FakeClient(data)
#     main_language = get_user_main_language("Ivan", fake_client)
#     assert main_language == "php"


# *def test_get_user_main_language_with_empty():
#     fake_client = FakeClient([])
#     main_language = get_user_main_language("Andrey", fake_client)
#     assert main_language is None
# ?# END
