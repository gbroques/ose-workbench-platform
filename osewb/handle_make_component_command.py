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
    if component == 'part':
        env = Environment(
            loader=PackageLoader('osewb', 'templates'))
        template = env.get_template('part.py')

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
        part_package_init_module_path = component_package_path.joinpath(
            '__init__.py')
        with part_package_init_module_path.open('r+') as f:
            lines = f.readlines()
            text = ''.join(lines)
            white_space = '[\s\S]+'
            all_pattern = white_space.join(['__all__', '=', '(\[', '\])'])
            match = re.search(all_pattern, text)
            if not match:
                print('No __all__ found in {}'.format(
                    part_package_init_module_path.resolve()))
                return None
            else:
                all_members = eval(match.group(1))
                next_all_string = build_next_all_string(all_members, name)
                new_contents = re.sub(all_pattern, next_all_string, text)
                import_statement = 'from ._{} import {}\n'.format(
                    name.lower(), name)
                new_contents += '\n' + import_statement
                f.seek(0)
                f.write(new_contents)
        SortImports(part_package_init_module_path.resolve())

        # 4. Setup init module in component sub-package
        init_module_path = new_component_sub_package_path.joinpath(
            '__init__.py')
        init_module_path.touch(exist_ok=True)
        with init_module_path.open('a') as f:
            import_statement = 'from .{} import {}\n'.format(
                name.lower(), name)
            all_declaration = "__all__ = ['{}']".format(name)
            f.write('\n'.join([import_statement, all_declaration]))
        SortImports(init_module_path.resolve())

        # 5. Create new component module using template
        module_name = '{}.py'.format(name.lower())
        part_module_path = new_component_sub_package_path.joinpath(module_name)
        part_module_existed_before = part_module_path.exists()
        part_module_path.touch(exist_ok=True)
        if part_module_existed_before:
            print('{} already exists. Skipping part class creation.'.format(
                module_name))
            return None
        part_module_path.write_text(template.render(name=name) + '\n')


def build_next_all_string(all_members: List[str], name: str) -> str:
    next_all_members = all_members + [name]
    sorted_next_all_members = sorted(next_all_members)
    next_all_members_with_indentation = [
        "    '{}'".format(m) for m in sorted_next_all_members]
    next_all_members_string = ',\n'.join(
        next_all_members_with_indentation)
    return '__all__ = [\n{}\n]'.format(
        next_all_members_string)
