import argparse
from typing import Tuple

from ._version import __version__
from .find_base_package import find_base_package, find_root_of_git_repository
from .handle_browse_command import handle_browse_command
from .handle_docs_command import handle_docs_command
from .handle_env_command import handle_env_command
from .handle_init_command import handle_init_command
from .handle_lint_command import handle_lint_command
from .handle_make_command import handle_make_command
from .handle_test_command import handle_test_command


def main() -> None:
    command, args = _parse_command()
    if command == 'init':
        machine_display_name = args['machine_display_name']
        handle_init_command(machine_display_name)
    elif command == 'test' or command == 'docs' or command == 'make':
        root_of_git_repository = find_root_of_git_repository()
        if root_of_git_repository is None:
            return None
        base_package = find_base_package()
        if base_package is None:
            return None
        if command == 'test':
            handle_test_command(base_package,
                                root_of_git_repository,
                                with_coverage=args['coverage'])
        elif command == 'docs':
            handle_docs_command(base_package, root_of_git_repository)
        elif command == 'make':
            make_subcommand = args['make_command']
            name = args['name']
            handle_make_command(base_package,
                                root_of_git_repository,
                                make_subcommand,
                                name)
    elif command == 'env':
        env_subcommand = args['env_command']
        handle_env_command(env_subcommand)
    elif command == 'browse' or command == 'lint':
        root_of_git_repository = find_root_of_git_repository()
        if root_of_git_repository is None:
            return None
        if command == 'browse':
            browse_subcommand = args['browse_command']
            handle_browse_command(root_of_git_repository, browse_subcommand)
        elif command == 'lint':
            should_fix = args['fix']
            handle_lint_command(root_of_git_repository, should_fix)


def _parse_command() -> Tuple[str, dict]:
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
    subparsers.add_parser('docs',
                          help='Make documentation',
                          usage='osewb docs')
    lint_parser = subparsers.add_parser('lint',
                                        help='Lint code',
                                        usage='osewb lint')
    lint_parser.add_argument('-f', '--fix',
                             action='store_true',
                             help='Attempt to automatically fix linter issues')
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
    browse_subparser.add_parser('docs',
                                help='Opens docs in web browser',
                                usage='osewb browse docs')
    browse_subparser.add_parser('coverage',
                                help='Opens coverage report in web browser',
                                usage='osewb browse coverage')
    args = vars(parser.parse_args())
    command = args.pop('command')
    return command, args


if __name__ == '__main__':
    main()
