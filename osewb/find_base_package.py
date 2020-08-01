import os
from typing import Optional, Union

from .check_for_executable_in_path import check_for_executable_in_path


def find_base_package() -> Optional[str]:
    """Find the base package in a workbench repository.

    Return None if not in a git repository,
    or no directory in the root of the repository starts with "ose".

    If multiple directories in the root of the repository start with "ose",
    then we return the first match.

    :return: Base package of workbench repository.
    """
    repo_root = find_root_of_git_repository()
    if repo_root is None:
        return None
    contents = os.listdir(repo_root)
    directories = [c for c in contents if os.path.isdir(
        os.path.join(repo_root, c)) and c.startswith('ose') and not c.endswith('egg-info')]
    if len(directories) == 0:
        print('No base package starting with "ose" found in repository.')
        return None
    elif len(directories) > 1:
        print('Multiple potential base packages starting with "ose" found:\n')
        print('    {}\n'.format(', '.join(directories)))
        print('Choosing first "{}" as base package.\n'.format(directories[0]))
    return directories[0]


def find_root_of_git_repository() -> Optional[str]:
    """Find the root of the current git repository.

    Returns None if there's an error, or not in a git repository.

    :return: path to root of git repository
    """
    return exec_git_command('git rev-parse --show-toplevel')


def find_git_user_name() -> Optional[str]:
    """Find the user name defined by git config.

    :return: Git user name
    """
    return exec_git_command('git config user.name')


def exec_git_command(git_command: str) -> Optional[str]:
    """Find the root of the current git repository.

    Returns None if there's an error, or not in a git repository.

    :param git_command: git command string
    :return: path to root of git repository
    """
    check_for_executable_in_path('git')
    pipe = os.popen(git_command)
    output = pipe.read().strip()
    if pipe.close() is not None:
        return None
    return output
