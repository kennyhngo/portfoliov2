from distutils.dir_util import copy_tree
import json
import os
import pathlib
import sys
from model import create_json
from jinja2 import Environment, FileSystemLoader, select_autoescape


def parse_json():
    input_dir = os.getcwd()
    input_dir = pathlib.Path(input_dir)
    template_dir = input_dir/'templates'

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template_list, context_list = ([] for i in range(2))
    create_json()

    with open(input_dir/'render'/'context.json', encoding='utf-8') as file:
        json_data = json.load(file)
        template_list.append(json_data['template'])
        context_list.append(json_data['context'])
    return template_list, context_list, env


def setup():
    input_dir = os.getcwd()
    input_dir = pathlib.Path(input_dir)
    template_list, context_list, env = parse_json()

    for template, context in zip(template_list, context_list):
        jinja_template = env.get_template(template)
        html_template = jinja_template.render(context)
        output_path = input_dir/'index.html'

        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(html_template)


def main():
    setup()


if __name__ == "__main__":
    main()
