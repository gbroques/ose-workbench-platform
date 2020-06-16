from __future__ import print_function

import argparse
import os
import pathlib
import webbrowser

from cookiecutter.main import cookiecutter

from .find_base_package import (find_base_package, find_git_user_name,
                                find_root_of_git_repository)
from .version import __version__


def main() -> None:
    command, args = _parse_command()
    if command == 'init':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        machine_display_name = args['machine_display_name']
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
        repo_name = 'ose-{}-workbench'.format(slugified_machine_name)
        print('Workbench initialized in "{}" directory.\n'.format(repo_name))
        print('Next, change directories and initialize the git repository:\n'.format(
            repo_name))
        print('    cd {} && git init\n'.format(repo_name))
    elif command == 'test' or command == 'docs':
        root_of_git_repository = find_root_of_git_repository()
        if root_of_git_repository is None:
            return
        base_package = find_base_package()
        if base_package is None:
            return None
        if command == 'test':
            with_coverage = args['coverage']
            test_command = 'pytest'
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
        elif command == 'docs':
            path_to_docs_dir = os.path.join(
                root_of_git_repository, 'docs')
            path_to_build_dir = os.path.join(
                path_to_docs_dir, '_build')
            path_to_sphinx_source_dir = os.path.join(
                path_to_docs_dir, base_package)
            execute_command('rm -rf {}'.format(path_to_build_dir))
            execute_command('rm -rf {}'.format(path_to_sphinx_source_dir))
            execute_command(
                'cd {} && sphinx-build . {}'.format(path_to_docs_dir, path_to_build_dir))
            print('To view, open docs/_build/index.html in a web browser, or run:\n')
            print('    osewb browse docs\n')
    elif command == 'env':
        if args['env_command'] == 'bootstrap':
            conda_prefix = os.environ.get('CONDA_PREFIX', None)
            if not conda_prefix:
                print('Environment varibale "CONDA_PREFIX" not set.')
                print('Is your environment activated?')
                return
            conda_env_name = os.path.basename(conda_prefix)
            conda_lib = os.path.join(conda_prefix, 'lib')
            conda_etc_base_path = os.path.join(conda_prefix, 'etc', 'conda')

            activate_instructions = '#!/bin/sh\n' + \
                'export INITIAL_PYTHONPATH=${PYTHONPATH}\n' + \
                'export PYTHONPATH={}:${{PYTHONPATH}}\n'.format(conda_lib)
            setup_conda_environment_hook_directy(
                conda_etc_base_path, 'activate.d', activate_instructions)

            deactivate_instructions = '#!/bin/sh\n' + \
                'export PYTHONPATH=${INITIAL_PYTHONPATH}\n' + \
                'unset INITIAL_PYTHONPATH\n'
            setup_conda_environment_hook_directy(
                conda_etc_base_path, 'deactivate.d', deactivate_instructions)

            print('Environment bootstrapped.')
            print('To reactivate your environment, run:\n')
            print('    conda activate {}\n'.format(conda_env_name))
    elif command == 'browse':
        root_of_git_repository = find_root_of_git_repository()
        if root_of_git_repository is None:
            return
        if args['browse_command'] == 'docs':
            path_to_index_html = os.path.join(
                root_of_git_repository, 'docs/_build/index.html')
            if not os.path.isfile(path_to_index_html):
                print('No index.html found in {}'.format(path_to_index_html))
                print('To build the documentation, run:\n')
                print('    osewb docs\n')
            else:
                webbrowser.open(path_to_index_html)
        elif args['browse_command'] == 'coverage':
            path_to_index_html = os.path.join(
                root_of_git_repository, 'htmlcov/index.html')
            if not os.path.isfile(path_to_index_html):
                print('No index.html found in {}'.format(path_to_index_html))
                print('To build the coverage report, run:\n')
                print('    osewb test --coverage\n')
            else:
                webbrowser.open(path_to_index_html)


def setup_conda_environment_hook_directy(conda_etc_base_path, directory, text):
    directory_path = os.path.join(conda_etc_base_path, directory)
    pathlib.Path(directory_path).mkdir(parents=True, exist_ok=True)
    env_vars_path = os.path.join(directory_path, 'env_vars.sh')
    pathlib.Path(env_vars_path).touch(exist_ok=True)
    pathlib.Path(env_vars_path).write_text(text)


def execute_command(command: str) -> None:
    print('Executing the following command:\n')
    print('    {}\n'.format(command))
    os.system(command)


def _parse_command() -> str:
    parser = argparse.ArgumentParser(
        description='A collection commands for OSE workbench development.',
        usage='osewb <command> [<args>]\n')
    parser.add_argument('--version', action='version', version=__version__)
    subparsers = parser.add_subparsers(title='Commands',
                                       dest='command',
                                       required=True)
    env_parser = subparsers.add_parser('env',
                                       help='Commands for interacting with environments',
                                       usage='osewb env <command>')
    env_subparser = env_parser.add_subparsers(title='Commands',
                                              dest='env_command',
                                              required=True)
    env_subparser.add_parser('bootstrap',
                             help='Bootstrap environment',
                             usage='osewb env bootstrap')
    test_parser = subparsers.add_parser('test',
                                        help='Run tests in workbench',
                                        usage='osewb test')
    test_parser.add_argument('-c', '--coverage',
                             action='store_true',
                             help='Run tests with coverage, and generate report')
    docs_parser = subparsers.add_parser('docs',
                                        help='Make documentation',
                                        usage='osewb docs')
    init_parser = subparsers.add_parser('init',
                                        help='Initialize new workbench',
                                        usage='osewb init <machine_display_name>')
    init_parser.add_argument('machine_display_name',
                             type=str,
                             help='Name of machine in title-case. Surround in double-quotes if name contains spaces (e.g. "CEB Brick Press")')
    browse_parser = subparsers.add_parser('browse',
                                          help='Commands for opening documents in a web browser',
                                          usage='osewb browse <command>')
    browse_subparser = browse_parser.add_subparsers(title='Commands',
                                                    dest='browse_command',
                                                    required=True)
    browse_docs_parser = browse_subparser.add_parser('docs',
                                                     help='Opens docs in web browser',
                                                     usage='osewb browse docs')
    browse_coverage_parser = browse_subparser.add_parser('coverage',
                                                         help='Opens coverage report in web browser',
                                                         usage='osewb browse coverage')
    args = vars(parser.parse_args())
    command = args.pop('command')
    return command, args


if __name__ == '__main__':
    main()
