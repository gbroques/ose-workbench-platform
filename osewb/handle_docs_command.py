import os

from .execute_command import execute_command


def handle_docs_command(base_package, root_of_git_repository) -> None:
    path_to_docs_dir = os.path.join(
        root_of_git_repository, 'docs')
    path_to_build_dir = os.path.join(
        path_to_docs_dir, '_build')
    path_to_sphinx_source_dir = os.path.join(
        path_to_docs_dir, base_package)
    execute_command('rm -rf {}'.format(path_to_build_dir))
    execute_command('rm -rf {}'.format(path_to_sphinx_source_dir))
    execute_command(
        'cd {} && sphinx-build -W --keep-going --color . {}'.format(path_to_docs_dir, path_to_build_dir))
    print('To view, open docs/_build/index.html in a web browser, or run:\n')
    print('    osewb browse docs\n')
