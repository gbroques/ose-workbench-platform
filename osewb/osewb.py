from __future__ import print_function

import argparse
import os
from typing import List

import docker
from cookiecutter.main import cookiecutter


def main() -> None:
    sub_command = _parse_sub_command()
    if sub_command == 'init':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        cookiecutter(os.path.join(dir_path, 'cookiecutter_ose_workbench'))
    elif sub_command == 'test':
        execute_command_in_docker_container(
            'docker exec -it {} pytest test/', 'test')
    elif sub_command == 'docs':
        execute_command_in_docker_container(
            'docker exec --workdir /var/app/docs -it {} make html', 'docs')


def execute_command_in_docker_container(command_template: str,
                                        container_type: str) -> None:
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


def _parse_sub_command() -> str:
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
    docs_parser = subparsers.add_parser('docs',
                                        help='Make documentation',
                                        usage='osewb docs')
    args = parser.parse_args()
    return vars(args)['command']


if __name__ == '__main__':
    main()
