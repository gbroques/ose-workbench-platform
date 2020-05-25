import os

from .check_for_executable_in_path import check_for_executable_in_path


def find_base_package() -> str:
    check_for_executable_in_path('git')
    pipe = os.popen('git rev-parse --show-toplevel')
    output = pipe.read().strip()
    if pipe.close() is not None:
        return None
    contents = os.listdir(output)
    directories = [c for c in contents if os.path.isdir(
        os.path.join(output, c)) and c.startswith('ose')]
    if len(directories) == 0:
        print('No base package starting with "ose" found in repository.')
        return None
    elif len(directories) > 1:
        print('Multiple potential base packages starting with "ose" found:\n')
        print('    {}\n'.format(', '.join(directories)))
        print('Choosing first "{}" as base package.'.format(directories[0]))
    return directories[0]
