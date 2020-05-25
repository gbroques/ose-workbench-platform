from __future__ import print_function

import argparse
import os
from typing import List

import docker
from cookiecutter.main import cookiecutter


def main() -> None:
    sub_command = _parse_sub_command()
    if sub_command == 'init':
        cookiecutter('./cookiecutter-ose-workbench')
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
    print("No {} container running. Execute:\n".format(container_type))
    print("    docker-compose up --detach {}\n".format(container_type))
    print("from the root of the workbench repository.")


def print_multiple_containers_found_message(ose_containers: List[str],
                                            container_type: str) -> None:
    comma_delimited_test_containers = ', '.join(ose_containers)
    print("Found multiple OSE {} containers running: {}.".format(
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
    sub_commands = {
        'init': 'Initialize new workbench',
        'test': 'Run all tests in workbench',
        'docs': 'Make documentation'
    }
    usage = 'osewb <command> [<args>]\n'
    for command, description in sub_commands.items():
        usage += '    {} - {}\n'.format(command, description)
    parser = argparse.ArgumentParser(
        description='A collection of OSE workbench commands.', usage=usage)
    parser.add_argument('command',
                        metavar='<command>',
                        type=str,
                        nargs=1,
                        help=', '.join((sub_commands.keys())),
                        choices=sub_commands.keys())
    args = parser.parse_args()
    return vars(args)['command'][0]


if __name__ == "__main__":
    main()
