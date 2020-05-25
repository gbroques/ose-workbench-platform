from __future__ import print_function

import argparse
import os
import shutil
from typing import List

import docker
from cookiecutter.main import cookiecutter


def main() -> None:
    command, args = _parse_command()
    if command == 'init':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        cookiecutter(os.path.join(dir_path, 'cookiecutter_ose_workbench'))
    elif command == 'test':
        with_coverage = args['coverage']
        test_command = 'docker exec -it {} pytest'
        if with_coverage:
            base_package = find_base_package()
            if base_package is not None:
                test_command += ' --cov {}/app'.format(base_package)
        test_command += ' ./test'
        execute_command_in_docker_container(test_command, 'test')
        if with_coverage:
            coverage_report_cmd = 'docker exec -it {} coverage html'
            execute_command_in_docker_container(coverage_report_cmd, 'test')
            print('Coverage report generated in htmlcov/ directory.')
            print('To view, open htmlcov/index.html in a web browser.')
    elif command == 'docs':
        execute_command_in_docker_container(
            'docker exec --workdir /var/app/docs -it {} make html', 'docs')


def execute_command_in_docker_container(command_template: str,
                                        container_type: str) -> None:
    check_for_executable_in_path('docker')
    ose_containers = get_ose_container_names()
    ose_containers_with_type = [
        name for name in ose_containers if name.endswith(container_type)]
    if len(ose_containers_with_type) == 0:
        print_no_running_containers_message(container_type)
        return
    if len(ose_containers_with_type) > 1:
        print_multiple_containers_found_message(
            ose_containers_with_type, container_type)
    container = ose_containers_with_type[0]
    command = command_template.format(container)
    print(command)
    os.system(command)


def print_no_running_containers_message(container_type: str) -> None:
    print('No {} container running.\n'.format(container_type))
    print('From the root of the repository, run:\n')
    print('    docker-compose up --detach {}\n'.format(container_type))


def print_multiple_containers_found_message(ose_containers: List[str],
                                            container_type: str) -> None:
    comma_delimited_test_containers = ', '.join(ose_containers)
    print('Found multiple OSE {} containers running: {}.'.format(
        container_type, comma_delimited_test_containers))
    print('Executing command within first container: {}.'.format(
        ose_containers[0]))


def get_ose_container_names() -> List[str]:
    client = docker.from_env()
    containers = client.containers.list()
    container_names = [container.name for container in containers]
    ose_containers = [
        name for name in container_names if name.startswith('ose')]
    return ose_containers


def find_base_package() -> str:
    check_for_executable_in_path('git')
    pipe = os.popen('git rev-parse --show-toplevel')
    output = pipe.read().strip()
    if pipe.close() is not None:
        return
    contents = os.listdir(output)
    directories = [c for c in contents if os.path.isdir(
        os.path.join(output, c)) and c.startswith('ose')]
    if len(directories) == 0:
        print('No base package starting with "ose" found in repository.')
        return
    elif len(directories) > 1:
        print('Multiple potential base packages starting with "ose" found:\n')
        print('    {}\n'.format(', '.join(directories)))
        print('Choosing first "{}" as base package.'.format(directories[0]))
    return directories[0]


def _parse_command() -> str:
    parser = argparse.ArgumentParser(
        description='A collection commands for OSE workbench development.',
        usage='osewb <command> [<args>]\n')
    subparsers = parser.add_subparsers(title='Commands',
                                       dest='command',
                                       required=True)
    init_parser = subparsers.add_parser('init',
                                        help='Initialize new workbench',
                                        usage='osewb init')
    test_parser = subparsers.add_parser('test',
                                        help='Run tests in workbench',
                                        usage='osewb test')
    test_parser.add_argument('-c', '--coverage',
                             action='store_true',
                             help='Run tests with coverage, and generate report')
    docs_parser = subparsers.add_parser('docs',
                                        help='Make documentation',
                                        usage='osewb docs')
    args = vars(parser.parse_args())
    command = args.pop('command')
    return command, args


def check_for_executable_in_path(executable_name):
    if shutil.which(executable_name) is None:
        print('{} must be installed, and available in your PATH.'.format(
            executable_name))
        exit(0)


if __name__ == '__main__':
    main()
