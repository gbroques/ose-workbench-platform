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
                                  name: str) -> None:
    # 1. Construct component package
    component_package_path = Path(os.path.join(
        root_of_git_repository,
        base_package,
        component
    ))
    component_package_path.mkdir(exist_ok=True)

    # 2. Construct new component sub-package
    #    Stop if it exists
    new_component_sub_package = '_' + name.lower()
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
    component_name = map_name_to_component_name(name, component)
    with component_package_init_module_path.open('r+') as f:
        lines = f.readlines()
        text = ''.join(lines)
        white_space = '[\s\S]+'
        all_pattern = white_space.join(['__all__', '=', '(\[', '\])'])
        match = re.search(all_pattern, text)
        if not match:
            print('No __all__ found in {}'.format(
                component_package_init_module_path.resolve()))
            return None
        else:
            all_members = eval(match.group(1))
            next_all_string = build_next_all_string(
                all_members, component_name)
            new_contents = re.sub(all_pattern, next_all_string, text)
            import_statement = 'from ._{} import {}\n'.format(
                name.lower(), component_name)
            new_contents += '\n' + import_statement
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
    component_module_text = render_template(component, name)
    component_module_path.write_text(component_module_text)


def build_next_all_string(all_members: List[str], component_name: str) -> str:
    next_all_members = all_members + [component_name]
    sorted_next_all_members = sorted(next_all_members)
    next_all_members_with_indentation = [
        "    '{}'".format(m) for m in sorted_next_all_members]
    next_all_members_string = ',\n'.join(
        next_all_members_with_indentation)
    return '__all__ = [\n{}\n]'.format(
        next_all_members_string)


def render_template(component: str, name: str) -> str:
    env = Environment(
        loader=PackageLoader('osewb', 'templates'))
    template = env.get_template('{}.py'.format(component))
    return template.render(name=name) + '\n'


def map_name_to_component_name(name: str, component: str) -> str:
    try:
        return {
            'part': name,
            'model': '{}Model'.format(name)
        }[component]
    except KeyError:
        print('No component named "{}"'.format(component))
        exit(1)


def map_name_to_component_module_name(name: str, component: str) -> str:
    try:
        return {
            'part': name.lower(),
            'model': '{}_model'.format(name.lower())
        }[component]
    except KeyError:
        print('No component named "{}"'.format(component))
        exit(1)
