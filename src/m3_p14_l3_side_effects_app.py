import os

from faker import Faker

faker = Faker()


def get_default_data():
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
    }


def _right(data={}):  # noqa: W0102
    default_data = get_default_data()
    return {**default_data, **data}


def _fail1(data={}):  # noqa: W0102
    data = data  # noqa: W0127
    return get_default_data()


def _fail2(data={}):  # noqa: W0102
    default_data = get_default_data()
    age_data = {"age": faker.random_int()}
    return {**default_data, **data, **age_data}


def _fail3(data={}):  # noqa: W0102
    faker.seed_instance(123)
    default_data = get_default_data()
    return {**default_data, **data}


functions = {
    "right": _right,
    "fail1": _fail1,
    "fail2": _fail2,
    "fail3": _fail3,
}


def get_function():
    name = os.environ['FUNCTION_VERSION']
    return functions[name]


# www = _fail1()
# print()
