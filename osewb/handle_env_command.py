import os
from pathlib import Path


def handle_env_command(env_subcommand: str) -> None:
    if env_subcommand == 'bootstrap':
        conda_prefix = os.environ.get('CONDA_PREFIX', None)
        if not conda_prefix:
            print('Environment variable "CONDA_PREFIX" not set.')
            print('Is your environment activated?')
            return None
        conda_env_name = os.path.basename(conda_prefix)
        conda_lib = os.path.join(conda_prefix, 'lib')
        conda_etc_base_path = os.path.join(conda_prefix, 'etc', 'conda')

        activate_instructions = '#!/bin/sh\n' + \
            'export INITIAL_PYTHONPATH=${PYTHONPATH}\n' + \
            'export PYTHONPATH={}:${{PYTHONPATH}}\n'.format(conda_lib)
        setup_conda_environment_hook_directory(
            conda_etc_base_path, 'activate.d', activate_instructions)

        deactivate_instructions = '#!/bin/sh\n' + \
            'export PYTHONPATH=${INITIAL_PYTHONPATH}\n' + \
            'unset INITIAL_PYTHONPATH\n'
        setup_conda_environment_hook_directory(
            conda_etc_base_path, 'deactivate.d', deactivate_instructions)

        print('Environment bootstrapped.')
        print('To reactivate your environment, run:\n')
        print('    conda activate {}\n'.format(conda_env_name))


def setup_conda_environment_hook_directory(conda_etc_base_path,
                                           directory,
                                           text):
    directory_path = os.path.join(conda_etc_base_path, directory)
    Path(directory_path).mkdir(parents=True, exist_ok=True)
    env_vars_path = os.path.join(directory_path, 'env_vars.sh')
    Path(env_vars_path).touch(exist_ok=True)
    Path(env_vars_path).write_text(text)
