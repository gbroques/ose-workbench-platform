import json
import os
import sys
from pathlib import Path
from typing import Optional


def handle_editor_config_command(root_of_git_repository: str,
                                 merge_workspace_settings: bool = False,
                                 overwrite_workspace_settings: bool = False) -> None:
    config = get_editor_config()
    workspace_settings = None
    if merge_workspace_settings or overwrite_workspace_settings:
        workspace_settings = get_vs_code_workspace_settings(
            root_of_git_repository)
        if merge_workspace_settings:
            if workspace_settings is None:
                print('No workspace settings found. Skipping merge.')
                workspace_settings = {}
            workspace_settings.update(config)
            config = workspace_settings

    # By default, VS Code uses 4 spaces for indentation
    # https://code.visualstudio.com/docs/editor/codebasics#_indentation
    stringified_config = json.dumps(config, indent=4, sort_keys=False)

    if overwrite_workspace_settings:
        workspace_settings_path = get_vs_code_workspace_settings_path(
            root_of_git_repository)
        question = 'Do you want to overwrite "{}"?'.format(
            workspace_settings_path)
        answer = query_yes_no(question, stringified_config)
        if answer is True:
            workspace_settings_path.parent.mkdir(exist_ok=True)
            with open(workspace_settings_path, 'w') as f:
                f.write(stringified_config)
            print('Successfully overwrote "{}".'.format(workspace_settings_path))
        else:
            print('Aborted overwriting "{}".'.format(workspace_settings_path))
    else:
        print(stringified_config)


def get_editor_config() -> dict:
    return {
        # Python Extension
        # https://marketplace.visualstudio.com/items?itemName=ms-python.python
        # ==============================================================================

        # General Settings
        # https://code.visualstudio.com/docs/python/settings-reference#_general-settings
        # ------------------------------------------------------------------------------
        # For FreeCAD auto-completion to pick-up .env file
        'python.envFile': '${workspaceFolder}/.env',

        # Formatting
        # https://code.visualstudio.com/docs/python/editing#_formatting
        # ------------------------------------------------------------------------------
        'python.formatting.provider': 'autopep8',

        # Linting
        # https://code.visualstudio.com/docs/python/linting
        # ------------------------------------------------------------------------------
        'python.linting.enabled': True,
        'python.linting.lintOnSave': True,
        'python.linting.pylintEnabled': False,
        'python.linting.flake8Enabled': True,
        'python.linting.flake8Args': [
            '--config {}'.format(path('.flake8'))
        ],
        # display flake8 warnings as errors
        'python.linting.flake8CategorySeverity.W': 'Error',
        'python.linting.mypyEnabled': True,
        # ------------------------------------------------------------------------------

        # Python Docstring Generator Extension
        # https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring
        # ==============================================================================
        'autoDocstring.docstringFormat': 'sphinx',
        'autoDocstring.customTemplatePath': path('.mustache')
        # ------------------------------------------------------------------------------
    }


def path(filename: str) -> str:
    current_dir = Path(os.path.dirname(os.path.realpath(__file__)))
    return str(current_dir.joinpath(filename).resolve())


def get_vs_code_workspace_settings(root_of_git_repository: str) -> Optional[dict]:
    path = get_vs_code_workspace_settings_path(root_of_git_repository)
    if not path.exists():
        return None
    with path.open() as f:
        settings = json.load(f)
    return settings


def get_vs_code_workspace_settings_path(root_of_git_repository: str) -> Path:
    """Get the path to VS Code workspace settings.

    See Also:
        https://code.visualstudio.com/docs/getstarted/settings#_settings-file-locations
    """
    return Path(root_of_git_repository) / '.vscode' / 'settings.json'


def query_yes_no(question, additional_pre_information: str = None, default: str = 'yes'):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
    It must be "yes" (the default), "no" or None (meaning
    an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {'yes': True, 'y': True, 'ye': True,
             'no': False, 'n': False}
    if default is None:
        prompt = ' [y/n] '
    elif default == 'yes':
        prompt = ' [Y/n] '
    elif default == 'no':
        prompt = ' [y/N] '
    else:
        raise ValueError('Invalid default answer "%s".' % default)

    while True:
        if additional_pre_information:
            print(additional_pre_information)
        print(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print('Please respond with "yes" or "no" (or "y" or "n").\n')
