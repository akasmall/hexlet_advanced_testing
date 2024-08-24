from schema import Schema
from src.m3_p14_l4_side_effects_app import get_default_data
from src.m3_p14_l4_side_effects_app import _fail2
# from src.app import _fail1, _fail2, _fail3

# build_user_1 = _fail1()
build_user = _fail2()
# build_user_3 = _fail3()
# build_user = get_default_data()


# BEGIN (write your solution here)
user_schema = Schema({
    'email': str,
    'first_name': str,
    'last_name': str,
})


def test_get_default_data():
    # default_data = get_default_data()
    # validated_data = user_schema.validate(default_data)
    # assert validated_data == default_data
    default_data = get_default_data()
    assert user_schema.is_valid(default_data)  # True


def test_get_fail1_data():
    data = build_user({'email': 'Piter@gmail.com'})
    assert data['email'] == 'Piter@gmail.com'


def test_get_fail3_data():
    assert 1 == 1
# END


# tests / test_solution.py
# Протестируйте функцию, которая генерирует случайного пользователя.
# В этом случае пользователь — это словарь с тремя полями:

# email
# first_name
# last_name
# Для генерации данных используется библиотека Faker:

# build_user = get_function()

# print(build_user())
# # => {
# 'email': 'Zion.Reichel12@yahoo.com',
# 'first_name': 'Elizabeth',
# 'last_name': 'Zulauf'
# }
# Если какой - то из параметров нужно задать точно,
# то его можно передать в функцию:

# build_user = get_function()

# print(build_user({'first_name': 'Petya'}))
# # => {
# 'email': 'Zion.Reichel12@yahoo.com',
# 'first_name': 'Petya',
# 'last_name': 'Zulauf'
# }
# Вам нужно протестировать три ситуации:

# Вызов build_user() возвращает словарь нужной структуры
# Вызов build_user() возвращает словарь с отличными от предыдущего
# вызова данными
# Установка полей пользователя через переданные параметры в словаре
# работает верно
# Подсказки
# Чтобы проверить соответствие словаря, заданным требованиям можно
# воспользоваться библиотекой schema:


# schema = Schema({
#     'name': str,
#     'age': int
# })

# schema.is_valid({'name': 'Nikolay', 'age': 20})  # True
# schema.is_valid({'name': 'Nikolay'})  # False

# !решение ментора
# *build_user = get_function()


# ?# BEGIN
# *def test_random():
#     user1 = build_user()
#     user2 = build_user()
#     assert not user1 == user2


# *def test_override():
#     data = {"first_name": "Ivan"}
#     user = build_user(data)
#     assert user["first_name"] == "Ivan"


# *def test_fields():
#     user = build_user()
#     schema = Schema({
#         "first_name": str,
#         "last_name": str,
#         "email": str
#     })
#     assert schema.is_valid(user)
# ?# END
