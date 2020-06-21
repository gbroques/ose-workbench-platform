
import os

from .execute_command import execute_command


def handle_test_command(base_package: str,
                        root_of_git_repository: str,
                        with_coverage: bool = False) -> None:
    test_command = 'pytest --color=yes'
    if with_coverage:
        test_command += ' --cov {}'.format(base_package)
    test_dir = os.path.join(root_of_git_repository, 'tests')
    test_command += ' ' + test_dir
    execute_command(test_command)
    if with_coverage:
        execute_command('coverage html')
        print('Coverage report generated in htmlcov/ directory.')
        print('To view, open htmlcov/index.html in a web browser, or run:\n')
        print('    osewb browse coverage\n')
