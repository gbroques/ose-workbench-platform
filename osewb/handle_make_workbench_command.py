import os

from cookiecutter.main import cookiecutter

from ._version import __version__
from .find_base_package import find_git_user_name


def handle_make_workbench_command(machine_display_name: str) -> None:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    git_user_name = find_git_user_name()
    if not git_user_name:
        print('Must configure your git user name:\n')
        print('    git config --global user.name "FIRST_NAME LAST_NAME"\n')
        print('This is used for the owner name throughout the workbench.')
        return
    cookiecutter(os.path.join(dir_path, 'cookiecutter_ose_workbench'),
                 no_input=True,
                 extra_context={
        'machine_display_name': machine_display_name,
        'owner_name': git_user_name,
        'ose_workbench_platform_version': __version__})
    slugified_machine_name = machine_display_name.lower().replace(' ', '-')
    conda_env_name = 'ose' + machine_display_name.lower().replace(' ', '')
    repo_name = 'ose-{}-workbench'.format(slugified_machine_name)
    print('Workbench initialized in "{}" directory.\n'.format(repo_name))
    print('Perform the following commands to get started:\n')
    print('1. Change directories and initialize the git repository:\n')
    print('    cd {} && git init\n'.format(repo_name))
    print('2. Create a conda environment and activate it:\n')
    print('    conda env create --file environment.yml && conda activate {}\n'.format(conda_env_name))
    print('3. Verify your installation:\n')
    print('    osewb -h\n')
