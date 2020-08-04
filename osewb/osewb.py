import argparse
import os
from typing import Tuple

from ._version import __version__
from .execute_command import execute_command
from .find_base_package import find_base_package, find_root_of_git_repository
from .handle_browse_command import handle_browse_command
from .handle_build_command import handle_build_command
from .handle_docs_command import handle_docs_command
from .handle_editor_config_command import handle_editor_config_command
from .handle_lint_command import handle_lint_command
from .handle_make_component_command import handle_make_component_command
from .handle_make_workbench_command import handle_make_workbench_command
from .handle_test_command import handle_test_command


def main() -> None:
    command, args = _parse_command()
    if command == 'make' and (args['make_command'] == 'workbench' or args['make_command'] == 'wb'):
        machine_display_name = args['machine_display_name']
        handle_make_workbench_command(machine_display_name)
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
            if args['docs_command'] == 'screenshot' or args['docs_command'] == 'ss':
                screenshot_script = os.path.join(os.path.dirname(
                    os.path.abspath(__file__)), 'part_screenshot.py')
                execute_command('freecad -c {}'.format(screenshot_script))
            else:
                handle_docs_command(base_package, root_of_git_repository)
        elif command == 'make':
            args_copy = args.copy()
            make_subcommand = args_copy.pop('make_command').replace('-', '_')
            try:
                make_subcommand = {
                    'pf': 'part_feature'
                }[make_subcommand]
            except KeyError:
                pass
            name = args_copy.pop('name')
            handle_make_component_command(base_package,
                                          root_of_git_repository,
                                          make_subcommand,
                                          name,
                                          args_copy)
    elif command == 'browse' or command == 'lint' or command == 'editor-config':
        root_of_git_repository = find_root_of_git_repository()
        if root_of_git_repository is None:
            return None
        if command == 'browse':
            browse_subcommand = args['browse_command']
            handle_browse_command(root_of_git_repository, browse_subcommand)
        elif command == 'lint':
            should_fix = args['fix']
            handle_lint_command(root_of_git_repository, should_fix)
        elif command == 'editor-config':
            handle_editor_config_command(
                root_of_git_repository, args['merge_workspace_settings'], args['overwrite_workspace_settings'])
    elif command == 'build':
        handle_build_command()


def _parse_command() -> Tuple[str, dict]:
    parser = argparse.ArgumentParser(
        description='A collection commands for OSE workbench development.',
        usage='osewb <command> [<args>]\n')
    parser.add_argument('--version', action='version', version=__version__)
    subparsers = parser.add_subparsers(title='Commands',
                                       dest='command',
                                       required=True)
    test_parser = subparsers.add_parser('test',
                                        help='Run tests in workbench',
                                        usage='osewb test')
    test_parser.add_argument('-c', '--coverage',
                             action='store_true',
                             help='Run tests with coverage, and generate report')
    lint_parser = subparsers.add_parser('lint',
                                        help='Lint code',
                                        usage='osewb lint')
    lint_parser.add_argument('-f', '--fix',
                             action='store_true',
                             help='Attempt to automatically fix linter issues')
    docs_parser = subparsers.add_parser('docs',
                                        help='Make documentation',
                                        usage='osewb docs [command]')
    docs_subparser = docs_parser.add_subparsers(title='Commands',
                                                dest='docs_command',
                                                required=False)
    docs_subparser.add_parser('screenshot',
                              help='Take screenshots of parts for documentation.',
                              usage='osewb docs screenshot',
                              aliases=['ss'])
    make_parser = subparsers.add_parser('make',
                                        help='Commands for making new code',
                                        usage='osewb make <command>',
                                        aliases=['mk'])
    make_subparser = make_parser.add_subparsers(title='Commands',
                                                dest='make_command',
                                                required=True)
    workbench_subparser = make_subparser.add_parser('workbench',
                                                    help='Make Workbench',
                                                    usage='osewb make workbench <machine_display_name>',
                                                    aliases=['wb'])
    workbench_subparser.add_argument('machine_display_name',
                                     type=str,
                                     help='Name of machine in title-case. Surround in double-quotes if name contains spaces (e.g. "CEB Brick Press")')
    part_subparser = make_subparser.add_parser('part',
                                               help='Make Part class',
                                               usage='osewb make part <name>')
    part_subparser.add_argument(
        'name', help='Name for the part class in pascal or upper camel-case (e.g. MyBox).')
    model_subparser = make_subparser.add_parser('model',
                                                help='Make Model class',
                                                usage='osewb make model <name>')
    model_subparser.add_argument(
        'name', help='Name for the model class in pascal or upper camel-case (e.g. MyBox).')
    model_subparser.add_argument('-p', '--part',
                                 action='store_true',
                                 help='Make part class as well.')
    part_feature_subparser = make_subparser.add_parser('part-feature',
                                                       help='Make Part Feature creation function',
                                                       usage='osewb make part-feature <name>',
                                                       aliases=['pf'])
    part_feature_subparser.add_argument(
        'name', help='Name for the part feature creation function in all-lower snake-case (e.g. my_box).')
    command_subparser = make_subparser.add_parser('command',
                                                  help='Make Command class',
                                                  usage='osewb make command <name>')
    command_subparser.add_argument(
        'name', help='Name for the command class in pascal or upper camel-case (e.g. MyBoxCommand).')
    browse_parser = subparsers.add_parser('browse',
                                          help='Commands for opening documents in a web browser',
                                          usage='osewb browse <command>',
                                          aliases=['br'])
    browse_subparser = browse_parser.add_subparsers(title='Commands',
                                                    dest='browse_command',
                                                    required=True)
    browse_subparser.add_parser('docs',
                                help='Opens docs in web browser',
                                usage='osewb browse docs')
    browse_subparser.add_parser('coverage',
                                help='Opens coverage report in web browser',
                                usage='osewb browse coverage',
                                aliases=['cov'])
    build_parser = subparsers.add_parser('build',
                                         help='Build a workbench',
                                         usage='osewb build',
                                         aliases=['bld'])
    editor_config_parser = subparsers.add_parser('editor-config',
                                                 help='Output config for VS Code editor.',
                                                 usage='osewb editor-config',
                                                 aliases=['ec'])
    editor_config_parser.add_argument('-m', '--merge-workspace-settings',
                                      action='store_true',
                                      help='Merge VS Code workspace settings.')
    editor_config_parser.add_argument('-o', '--overwrite-workspace-settings',
                                      action='store_true',
                                      help='Overwrite VS Code workspace settings.')
    args = vars(parser.parse_args())
    command = args.pop('command')
    # TODO: Map short-alias of sub-commands to full-command name before returning!
    #       For example, ss -> screenshot or wb -> workbench..
    return map_potential_command_alias(command), args


def map_potential_command_alias(command: str):
    try:
        return {
            'mk': 'make',
            'br': 'browse',
            'bld': 'build',
            'ec': 'editor-config'
        }[command]
    except KeyError:
        return command


if __name__ == '__main__':
    main()
