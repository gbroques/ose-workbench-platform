import importlib
import inspect
import os
import re
from pathlib import Path

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
        part_package_path = Path(os.path.join(
            root_of_git_repository,
            base_package,
            'part'
        ))
        part_package_path.mkdir(exist_ok=True)
        part_package_init_module_path = part_package_path.joinpath(
            '__init__.py')
        part_lower = name.lower()
        new_part_package = '_' + part_lower
        new_part_package_path = Path(
            part_package_path).joinpath(new_part_package)
        if(new_part_package_path.exists()):
            print('{} package already exists. Skipping creation.'.format(
                new_part_package))
            return None
        import_statement = 'from ._{} import {}\n'.format(part_lower, name)
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
                next_all_members = all_members + [name]
                sorted_next_all_members = sorted(next_all_members)
                next_all_members_with_indentation = [
                    "    '{}'".format(m) for m in sorted_next_all_members]
                next_all_members_string = ',\n'.join(
                    next_all_members_with_indentation)
                next_all_string = '__all__ = [\n{}\n]'.format(
                    next_all_members_string)
                ret = re.sub(all_pattern, next_all_string, text)
                ret += '\n' + import_statement
                f.seek(0)
                f.write(ret)
        SortImports(part_package_init_module_path.resolve())

        new_part_package_path.mkdir(exist_ok=True)
        init_module_path = new_part_package_path.joinpath('__init__.py')
        init_module_path.touch(exist_ok=True)
        import_statement = 'from .{} import {}\n'.format(part_lower, name)
        all_declaration = "__all__ = ['{}']".format(name)
        with init_module_path.open('a') as f:
            f.write('\n'.join([import_statement, all_declaration]))
        SortImports(init_module_path.resolve())
        module_name = '{}.py'.format(part_lower)
        part_module_path = new_part_package_path.joinpath(module_name)
        part_module_existed_before = part_module_path.exists()
        part_module_path.touch(exist_ok=True)
        if part_module_existed_before:
            print('{} already exists. Skipping part class creation.'.format(
                module_name))
            return None
        part_module_path.write_text(template.render(name=name) + '\n')
