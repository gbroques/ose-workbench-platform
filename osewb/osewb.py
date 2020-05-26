from __future__ import print_function

import argparse
import os
from typing import List

import docker
from cookiecutter.main import cookiecutter

from .check_for_executable_in_path import check_for_executable_in_path
from .find_base_package import find_base_package


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
        base_package = find_base_package()
        if base_package is not None:
            execute_command_in_docker_container(
                'docker exec -it {} generate_property_tables.py ' + base_package, 'test')
        execute_command_in_docker_container(
            'docker exec --workdir /var/app/docs -it {} rm -rf ./_build', 'docs')
        base_package = find_base_package()
        if base_package is not None:
            clean_cmd = 'docker exec --workdir /var/app/docs -it {} rm -rf ' + base_package
            execute_command_in_docker_container(clean_cmd, 'docs')
        execute_command_in_docker_container(
            'docker exec --workdir /var/app/docs -it {} sphinx-build . ./_build', 'docs')


def execute_command_in_docker_container(command_template: str,
                                        container_type: str) -> None:
    check_for_executable_in_path('docker')
    ose_containers = get_ose_container_names()
    ose_containers_with_type = [
        name for name in ose_containers if name.endswith(container_type)]
    if len(ose_containers_with_type) == 0:
        print_no_running_containers_message(container_type)
        exit(0)
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
    print('    docker-compose up --detach\n')


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


if __name__ == '__main__':
    main()
