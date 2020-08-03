import importlib
import inspect
import os
import re
from pathlib import Path
from typing import List

from isort import SortImports
from jinja2 import Environment, PackageLoader


def handle_make_component_command(base_package: str,
                                  root_of_git_repository: str,
                                  component: str,
                                  name: str,
                                  args: dict) -> None:
    # 1. Construct component package
    component_package_path = Path(os.path.join(
        root_of_git_repository,
        map_base_package_to_library_or_workbench_package(
            base_package, component),
        component
    ))
    component_package_path.mkdir(exist_ok=True)

    # 2. Construct new component sub-package
    #    Stop if it exists
    new_component_sub_package = '_' + camel_case_to_snake_case(name)
    new_component_sub_package_path = Path(
        component_package_path).joinpath(new_component_sub_package)
    if(new_component_sub_package_path.exists()):
        print('{} package already exists. Skipping creation.'.format(
            new_component_sub_package))
        return None
    new_component_sub_package_path.mkdir(exist_ok=True)

    # 3. Update init module of component package
    component_package_init_module_path = component_package_path.joinpath(
        '__init__.py')
    component_package_init_module_path.touch(exist_ok=True)
    component_name = map_name_to_component_name(name, component)
    with component_package_init_module_path.open('r+') as f:
        lines = f.readlines()
        text = ''.join(lines)
        white_space = '[\s\S]+'
        all_pattern = white_space.join(['__all__', '=', '(\[', '\])'])
        match = re.search(all_pattern, text)
        all_members = []
        if match:
            all_members = eval(match.group(1))
        next_all_string = build_next_all_string(
            all_members, component_name)
        if not match:
            text = next_all_string
        new_contents = re.sub(all_pattern, next_all_string, text)
        import_statement = 'from .{} import {}\n'.format(
            new_component_sub_package, component_name)
        new_contents = import_statement + '\n' + new_contents
        f.seek(0)
        f.write(new_contents)
    SortImports(component_package_init_module_path.resolve())

    # 4. Setup init module in component sub-package
    component_module_name = map_name_to_component_module_name(name, component)
    init_module_path = new_component_sub_package_path.joinpath(
        '__init__.py')
    init_module_path.touch(exist_ok=True)
    with init_module_path.open('a') as f:
        import_statement = 'from .{} import {}\n'.format(
            component_module_name, component_name)
        all_declaration = "__all__ = ['{}']".format(component_name)
        f.write('\n'.join([import_statement, all_declaration]))
    SortImports(init_module_path.resolve())

    # 5. Create new component module using template
    module_name = '{}.py'.format(component_module_name)
    component_module_path = new_component_sub_package_path.joinpath(
        module_name)
    component_module_existed_before = component_module_path.exists()
    component_module_path.touch(exist_ok=True)
    if component_module_existed_before:
        print('{} already exists. Skipping {} class creation.'.format(
            module_name, component))
        return None
    component_module_text = render_template(
        component, name, base_package, args)
    component_module_path.write_text(component_module_text)
    if component == 'model' and args['part']:
        del args['part']
        handle_make_component_command(base_package,
                                      root_of_git_repository,
                                      'part',
                                      name,
                                      args)


def build_next_all_string(all_members: List[str], component_name: str) -> str:
    next_all_members = all_members + [component_name]
    sorted_next_all_members = sorted(next_all_members)
    next_all_members_with_indentation = [
        "    '{}'".format(m) for m in sorted_next_all_members]
    next_all_members_string = ',\n'.join(
        next_all_members_with_indentation)
    return '__all__ = [\n{}\n]'.format(
        next_all_members_string)


def render_template(component: str, name: str, base_package: str, args: dict) -> str:
    env = Environment(
        loader=PackageLoader('osewb', 'templates'))
    template = env.get_template('{}.py'.format(component))
    template_args = get_component_template_args(component, name, args)
    return template.render(name=name, base_package=base_package, **template_args) + '\n'


def map_name_to_component_name(name: str, component: str) -> str:
    try:
        return {
            'part': name,
            'model': '{}Model'.format(name),
            'command': '{}Command'.format(name),
            'part_feature': 'create_{}'.format(name)
        }[component]
    except KeyError:
        print('No component named "{}"'.format(component))
        exit(1)


def map_name_to_component_module_name(name: str, component: str) -> str:
    try:
        return {
            'part': camel_case_to_snake_case(name),
            'model': '{}_model'.format(camel_case_to_snake_case(name)),
            'command': '{}_command'.format(camel_case_to_snake_case(name)),
            'part_feature': 'create_{}'.format(camel_case_to_snake_case(name))
        }[component]
    except KeyError:
        print('No component named "{}"'.format(component))
        exit(1)


def get_component_template_args(component: str, name: str, args: dict) -> dict:
    if component == 'model' and args['part']:
        return {
            'part': map_name_to_component_name(name, 'part')
        }
    if component == 'part_feature':
        return {
            'model': map_name_to_component_name(
                snake_case_to_camel_case(name), 'model')
        }
    return {}


def map_base_package_to_library_or_workbench_package(base_package: str,
                                                     component: str) -> str:
    library_package_components = ['part', 'model']
    workbench_package_components = ['command', 'part_feature']
    if component in library_package_components:
        return base_package
    elif component in workbench_package_components:
        return os.path.join('freecad', base_package)
    else:
        raise ValueError(
            'Component "{}" not in a library or workbench package.'.format(component))


def camel_case_to_snake_case(string: str) -> str:
    result = [string[0].lower()]
    for c in string[1:]:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            result.append('_')
            result.append(c.lower())
        else:
            result.append(c)

    return ''.join(result)


def snake_case_to_camel_case(string: str) -> str:
    return string.replace('_', ' ').title().replace(' ', '')
