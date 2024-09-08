from src.m3_p14_l7_monkey_patch_client import Client
# тут мне она не нужна
# from functions import get_function
# тут для теста IDE добавляю импорт
from src.m3_p14_l7_monkey_patch_app import get_user_main_language
# , _wrong1, _wrong2

# get_user_main_language = get_function()


# BEGIN (write your solution here)


def test_get_user_main_language(monkeypatch):
    data = [
        {"language": "ruby"},
        {"language": "php"},
        {"language": "java"},
        {"language": "php"},
        {"language": "js"},
    ]

    def mock_list_for_users(self, user_name):
        return data

    monkeypatch.setattr(Client, "list_for_users", mock_list_for_users)
    main_language = get_user_main_language("Ivan")
    assert main_language == "php"


def test_get_user_main_language_with_empty(monkeypatch):
    data = []

    def mock_list_for_users(self, user_name):
        return data

    monkeypatch.setattr(Client, "list_for_users", mock_list_for_users)
    main_language = get_user_main_language("Ivan")
    assert main_language is None
# END

# !tests / test_solution.py
# ?В этом задании нужно протестировать такую же функцию
# get_user_main_language(user), как и в предыдущем упражнении.
# Разница в том, что здесь нужно использовать манкипатчинг,
# а не инверсию зависимостей.

# ?Подмените атрибут list_for_users() в классе Client, который используется
# функцией get_user_main_language(user) для отправки запроса.

# *# Запрос, который выполняет функция get_user_main_language()
# # Именно этот метод нужно будет подменить в фейковом клиенте
# *data = client.list_for_users(user_name)
# # Список репозиториев — data. У каждого репозитория может быть много полей,
# # но нас интересует ровно одно – language
# # Эти данные нужно подготовить в тестах для фейкового клиента
# *print(data)
# *# [{ "language": "php", ... }, { "language": "javascript", ... }, ...]


# !# BEGIN
# *def test_get_user_main_language():

#     def patched_list_for_users(self, user_name):
#         return [
#             {"language": "ruby"},
#             {"language": "php"},
#             {"language": "java"},
#             {"language": "php"},
#             {"language": "js"},
#         ]

#     Client.list_for_users = patched_list_for_users
#     main_language = get_user_main_language("Ivan")
#     assert main_language == "php"


# *def test_get_user_main_language_with_empty():

#     def patched_list_for_users(self, user_name):
#         return []

#     Client.list_for_users = patched_list_for_users
#     main_language = get_user_main_language("Andrey")
#     assert main_language is None
# *# END
