import os
import json
import yaml


parsers_right = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "csv": lambda data: data.strip().split(',')
}

parsers_wrong1 = {
    "json": lambda data: [],
    "yaml": yaml.safe_load,
    "csv": lambda data: data.strip().split(',')
}

parsers_wrong2 = {
    "json": json.loads,
    "yaml": lambda data: [],
    "csv": lambda data: data.strip().split(',')
}

parsers_wrong3 = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "csv": lambda data: []
}


def gen_solution(parsers):
    def to_html_list(filepath):
        f = open(filepath, encoding="utf-8")
        content = f.read()
        ext = os.path.splitext(filepath)[1][1:]
        items = parsers[ext](content)
        lis = map(lambda item: f"    <li>{item}</li>", items)
        list_ = "\n".join(lis)
        return f"<ul>\n{list_}\n</ul>"
    return to_html_list


functions = {
    "right": gen_solution(parsers_right),
    "fail1": gen_solution(parsers_wrong1),
    "fail2": gen_solution(parsers_wrong2),
    "fail3": gen_solution(parsers_wrong3)
}


def get_function():
    name = os.environ['FUNCTION_VERSION']
    return functions[name]


# to_html_list_ = gen_solution(functions)
# html1 = to_html_list_('./tests/fixtures/list.csv')
# html2 = to_html_list_('./tests/fixtures/list.json')
# html3 = to_html_list_('./tests/fixtures/list.yaml')
