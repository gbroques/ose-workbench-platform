
import os
from pathlib import Path

from .execute_command import execute_command


def handle_test_command(base_package: str,
                        root_of_git_repository: str,
                        with_coverage: bool = False) -> None:
    test_command = 'pytest --color=yes'
    if with_coverage:
        cov_pkg = find_coverage_package(root_of_git_repository, base_package)
        test_command += ' --cov {}'.format(cov_pkg)
    test_dir = os.path.join(root_of_git_repository, 'tests')
    test_command += ' ' + test_dir
    execute_command(test_command)
    if with_coverage:
        execute_command('coverage html')
        print('Coverage report generated in htmlcov/ directory.')
        print('To view, open htmlcov/index.html in a web browser, or run:\n')
        print('    osewb browse coverage\n')


def find_coverage_package(root_of_git_repository: str, base_package: str) -> str:
    if is_workbench(root_of_git_repository):
        library_pkg = os.path.join(root_of_git_repository, base_package)
        if not Path(library_pkg).exists():
            print('library package not found')
            exit(1)
        return os.path.join(root_of_git_repository, base_package)
    else:  # Assume library with base package -> app / gui sub-packages
           # this assumption currently only holds true for ose-workbench-core
        app_pkg = os.path.join(root_of_git_repository, base_package, 'app')
        if not Path(app_pkg).exists():
            print('app package not found')
            exit(1)
        return app_pkg


def is_workbench(root_of_git_repository: str) -> bool:
    return Path(root_of_git_repository).joinpath('freecad').exists()
