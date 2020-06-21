import os
from pathlib import Path

from isort import SortImports
from jinja2 import Environment, PackageLoader


def handle_make_command(base_package: str,
                        root_of_git_repository: str,
                        make_subcommand: str,
                        name: str) -> None:
    if make_subcommand == 'part':
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
        import_statement = 'from .{} import {}\n'.format(part_lower, name)
        with part_package_init_module_path.open('a') as f:
            f.write(import_statement)
        SortImports(part_package_init_module_path.resolve())
        new_part_package_path = Path(
            part_package_path).joinpath(part_lower)
        new_part_package_path.mkdir(exist_ok=True)
        init_module_path = new_part_package_path.joinpath('__init__.py')
        init_module_path.touch(exist_ok=True)
        with init_module_path.open('a') as f:
            f.write(import_statement)
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
