from pathlib import Path

from .execute_command import execute_command


def handle_lint_command(root_of_git_repository: str) -> None:
    project_root = get_project_root()
    flake8_config = project_root.joinpath('.flake8').resolve()
    execute_command('flake8 --config {} {}'.format(flake8_config, root_of_git_repository))

    mypy_config = project_root.joinpath('.mypy.ini').resolve()
    execute_command('mypy --config-file {} {}'.format(mypy_config, root_of_git_repository), env={
        'MYPY_FORCE_COLOR': '1'
    })


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent
