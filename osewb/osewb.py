from __future__ import print_function

import argparse
import os

import docker
from cookiecutter.main import cookiecutter


def main():
    sub_command = _parse_sub_command()
    if sub_command == 'init':
        cookiecutter('./cookiecutter-ose-workbench')
    elif sub_command == 'test':
        client = docker.from_env()
        containers = client.containers.list()
        container_names = [container.name for container in containers]
        ose_test_containers = [
            name for name in container_names if is_ose_test_container(name)]
        if len(ose_test_containers) == 0:
            print("No test container running. Execute:\n")
            print("    docker-compose up --detach test\n")
            print("from the root of the workbench repository.")
            return
        if len(ose_test_containers) > 1:
            comma_delimited_test_containers = ', '.join(ose_test_containers)
            print("Found multiple OSE test containers running: {}.".format(
                comma_delimited_test_containers))
            print('Running tests within first container "{}".'.format(
                ose_test_containers[0]))
        test_container = ose_test_containers[0]
        test_command = 'docker exec -it {} pytest test/'.format(test_container)
        print(test_command)
        os.system(test_command)


def is_ose_test_container(container_name):
    return container_name.startswith('ose') and container_name.endswith('test')


def _parse_sub_command():
    sub_commands = {
        'init': 'Initialize new workbench',
        'test': 'Run all tests in workbench'
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
