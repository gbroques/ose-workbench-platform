import os
from pathlib import Path

from .execute_command import execute_command


def handle_lint_command(root_of_git_repository: str,
                        should_fix: bool = False) -> None:
    current_dir = Path(os.path.dirname(os.path.realpath(__file__)))
    pycodestyle_config = current_dir.joinpath('.pycodestyle').resolve()
    if should_fix:
        execute_command('isort --recursive {}'.format(root_of_git_repository))
        execute_command('autopep8 ' +
                        '--global-config {} '.format(pycodestyle_config) +
                        '--in-place ' +
                        '--aggressive ' +
                        '--recursive {}'.format(root_of_git_repository))
        return None
    flake8_config = current_dir.joinpath('.flake8').resolve()
    flake8_code = execute_command(
        'flake8 --config {} {}'.format(flake8_config, root_of_git_repository), exit_on_non_zero_code=False)
    mypy_config = current_dir.joinpath('.mypy.ini').resolve()
    mypy_code = execute_command('mypy --config-file {} {}'.format(mypy_config, root_of_git_repository), env={
        'MYPY_FORCE_COLOR': '1'
    }, exit_on_non_zero_code=False)
    return_code_pairs = [('flake8', flake8_code), ('mypy', mypy_code)]
    was_lint_error = any([pair[1] for pair in return_code_pairs])
    if was_lint_error:
        # TODO: There's some duplication between this and the build command.
        #       see handle_build_command.py
        print('\nLint errors detected from the following command(s):')
        commands_with_errors = [pair[0]
                                for pair in return_code_pairs if pair[1]]
        print('    {}\n'.format(', '.join(commands_with_errors)))
        print('Try fixing them by running:\n')
        print('    osewb lint --fix\n')
        exit(1)
    print('No lint warnings or errors detected!')
