import os
from pathlib import Path

from .execute_command import execute_command


def handle_docs_command(base_package, root_of_git_repository) -> None:
    path_to_docs_dir = os.path.join(
        root_of_git_repository, 'docs')

    path_to_build_dir = os.path.join(
        path_to_docs_dir, '_build')
    remove_existing_directory_recursively(path_to_build_dir)

    path_to_library_package_sphinx_source_dir = os.path.join(
        path_to_docs_dir, base_package)
    remove_existing_directory_recursively(
        path_to_library_package_sphinx_source_dir)

    path_to_workbench_package_sphinx_source_dir = os.path.join(
        path_to_docs_dir, 'freecad')
    remove_existing_directory_recursively(
        path_to_workbench_package_sphinx_source_dir)

    execute_command(
        'cd {} && sphinx-build -W --keep-going --color . {}'.format(path_to_docs_dir, path_to_build_dir))

    print('To view, open docs/_build/index.html in a web browser, or run:\n')
    print('    osewb browse docs\n')


def remove_existing_directory_recursively(directory: str) -> None:
    if Path(directory).exists():
        execute_command('rm -rf {}'.format(directory))
