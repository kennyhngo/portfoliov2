"""Main driver of the program - renders HTML using jinja."""
import json
import os
import pathlib
from jinja2 import Environment, FileSystemLoader, select_autoescape
from model import create_json  # pylint: disable=import-error


def parse_json():
    """Parse information from a JSON file."""
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
    """Prepare the templates and context."""
    input_dir = os.getcwd()
    input_dir = pathlib.Path(input_dir)
    template_list, context_list, env = parse_json()

    for template, context in zip(template_list, context_list):
        jinja_template = env.get_template(template)
        html_template = jinja_template.render(context)
        output_path = input_dir/'index.html'

        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(html_template)
