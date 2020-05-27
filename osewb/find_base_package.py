import os

from .check_for_executable_in_path import check_for_executable_in_path


def find_base_package() -> str:
    repo_root = find_root_of_git_repository()
    contents = os.listdir(repo_root)
    directories = [c for c in contents if os.path.isdir(
        os.path.join(repo_root, c)) and c.startswith('ose')]
    if len(directories) == 0:
        print('No base package starting with "ose" found in repository.')
        return None
    elif len(directories) > 1:
        print('Multiple potential base packages starting with "ose" found:\n')
        print('    {}\n'.format(', '.join(directories)))
        print('Choosing first "{}" as base package.\n'.format(directories[0]))
    return directories[0]


def find_root_of_git_repository():
    check_for_executable_in_path('git')
    pipe = os.popen('git rev-parse --show-toplevel')
    output = pipe.read().strip()
    if pipe.close() is not None:
        return None
    return output
