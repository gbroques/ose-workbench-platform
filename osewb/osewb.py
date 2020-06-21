import argparse
import os
import webbrowser
from pathlib import Path

from isort import SortImports
from jinja2 import Environment, PackageLoader

from ._version import __version__
from .find_base_package import find_base_package, find_root_of_git_repository
from .handle_docs_command import handle_docs_command
from .handle_env_command import handle_env_command
from .handle_init_command import handle_init_command
from .handle_test_command import handle_test_command


def main() -> None:
    command, args = _parse_command()
    if command == 'init':
        machine_display_name = args['machine_display_name']
        handle_init_command(machine_display_name)
    elif command == 'test' or command == 'docs':
        root_of_git_repository = find_root_of_git_repository()
        if root_of_git_repository is None:
            return
        base_package = find_base_package()
        if base_package is None:
            return None
        if command == 'test':
            handle_test_command(base_package,
                                root_of_git_repository,
                                with_coverage=args['coverage'])
        elif command == 'docs':
            handle_docs_command(base_package, root_of_git_repository)
    elif command == 'env':
        env_subcommand = args['env_command']
        handle_env_command(env_subcommand)
    elif command == 'make':
        root_of_git_repository = find_root_of_git_repository()
        if root_of_git_repository is None:
            return None
        base_package = find_base_package()
        if base_package is None:
            return None
        if args['make_command'] == 'part':
            print("base package", base_package)
            name = args['name']
            env = Environment(
                loader=PackageLoader('osewb', 'templates'),
            )
            template = env.get_template('part.py')
            part_package_path = Path(os.path.join(
                root_of_git_repository,
                base_package,
                'part'
            ))
            part_package_path.mkdir(exist_ok=True)
            part_package_init_module_path = part_package_path.joinpath(
                '__init__.py')
            part_lower = name.lower()
            import_statement = 'from .{} import {}\n'.format(part_lower, name)
            with part_package_init_module_path.open('a') as f:
                f.write(import_statement)
            SortImports(part_package_init_module_path.resolve())
            new_part_package_path = Path(
                part_package_path).joinpath(part_lower)
            new_part_package_path.mkdir(exist_ok=True)
            init_module_path = new_part_package_path.joinpath('__init__.py')
            init_module_path.touch(exist_ok=True)
            with init_module_path.open('a') as f:
                f.write(import_statement)
            SortImports(init_module_path.resolve())
            module_name = '{}.py'.format(part_lower)
            part_module_path = new_part_package_path.joinpath(module_name)
            part_module_existed_before = part_module_path.exists()
            part_module_path.touch(exist_ok=True)
            if part_module_existed_before:
                print('{} already exists. Skipping part class creation.'.format(
                    module_name))
                return None
            part_module_path.write_text(template.render(name=name) + '\n')
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


def _parse_command() -> str:
    parser = argparse.ArgumentParser(
        description='A collection commands for OSE workbench development.',
        usage='osewb <command> [<args>]\n')
    parser.add_argument('--version', action='version', version=__version__)
    subparsers = parser.add_subparsers(title='Commands',
                                       dest='command',
                                       required=True)
    make_parser = subparsers.add_parser('make',
                                        help='Commands for making new code',
                                        usage='osewb make <command>')
    make_subparser = make_parser.add_subparsers(title='Commands',
                                                dest='make_command',
                                                required=True)
    part_subparser = make_subparser.add_parser('part',
                                               help='Make Part class',
                                               usage='osewb make part <name>')
    part_subparser.add_argument('name', help='Name for the part class')
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
