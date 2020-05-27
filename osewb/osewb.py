from __future__ import print_function

import argparse
import os
from typing import List

import docker
from cookiecutter.main import cookiecutter

from .check_for_executable_in_path import check_for_executable_in_path
from .find_base_package import find_base_package, find_root_of_git_repository


def main() -> None:
    command, args = _parse_command()
    if command == 'init':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        cookiecutter(os.path.join(dir_path, 'cookiecutter_ose_workbench'))
    elif command == 'test':
        with_coverage = args['coverage']
        test_command = 'docker exec -it {} pytest'
        base_package = find_base_package()
        if with_coverage and base_package is not None:
            test_command += ' --cov {}/app'.format(base_package)
        test_command += ' ./test'
        execute_command_in_docker_container(test_command, base_package)
        if with_coverage:
            coverage_report_cmd = 'docker exec -it {} coverage html'
            execute_command_in_docker_container(
                coverage_report_cmd, base_package)
            print('Coverage report generated in htmlcov/ directory.')
            print('To view, open htmlcov/index.html in a web browser.')
    elif command == 'docs':
        base_package = find_base_package()
        if base_package is not None:
            execute_command_in_docker_container(
                'docker exec -it {} generate_property_tables.py ' + base_package, base_package)
        execute_command_in_docker_container(
            'docker exec --workdir /var/app/docs -it {} rm -rf ./_build', base_package)
        base_package = find_base_package()
        if base_package is not None:
            clean_cmd = 'docker exec --workdir /var/app/docs -it {} rm -rf ' + base_package
            execute_command_in_docker_container(clean_cmd, base_package)
        execute_command_in_docker_container(
            'docker exec --workdir /var/app/docs -it {} sphinx-build . ./_build', base_package)
    elif command == 'container':
        image_tag = 'ose-workbench-platform'
        if args['container_command'] == 'image':
            print('Building {} image with the following command:\n'.format(image_tag))
            path_to_script = os.path.dirname(os.path.abspath(__file__))
            build_command = '    docker build --tag {} {}'.format(
                image_tag, path_to_script)
            print(build_command + '\n')
            os.system(build_command)
            print('\nBuilt {} image.\n'.format(image_tag))
            print('To create a container from this image, run:\n')
            print('    osewb container create\n')
            print('To delete, or remove the image, run:\n')
            print('    docker rmi {}\n'.format(image_tag))
        elif args['container_command'] == 'create':
            client = docker.from_env()
            images = client.images.list()
            image_tags = [tag.split(':')[0]
                          for image in images for tag in image.tags]
            is_platform_image_created = image_tag in image_tags
            if not is_platform_image_created:
                print('{} image not created.\n'.format(image_tag))
                print('To create the {} image, run:\n'.format(image_tag))
                print('    osewb container image\n'.format(image_tag))
                return
            base_package = find_base_package()
            if base_package is not None:
                if base_package in get_container_names(all=True):
                    print('Container {} already created.'.format(base_package))
                    return
                print('Creating {} container with the following command:\n'.format(
                    base_package))
                repo_root = find_root_of_git_repository()
                create_command = '    docker create --name {} --volume {}:/var/app {}'.format(
                    base_package, repo_root, image_tag)
                print(create_command + '\n')
                os.system(create_command)
                print('\nCreated {} container.\n'.format(base_package))
                print('To start the container, run:\n'.format(base_package))
                print('    docker start {}\n'.format(base_package))
                print('To stop the container, run:\n'.format(base_package))
                print('    docker stop {}\n'.format(base_package))
                print('To delete, or remove the container, run:\n')
                print('    docker rm {}\n'.format(base_package))


def execute_command_in_docker_container(command_template: str, base_package: str) -> None:
    check_for_executable_in_path('docker')
    ose_containers = get_ose_container_names()
    if len(ose_containers) == 0:
        print_no_running_container_message(base_package)
        exit(0)
    if len(ose_containers) > 1:
        print_multiple_containers_found_message(ose_containers)
    container = ose_containers[0]
    command = command_template.format(container)
    print(command)
    os.system(command)


def print_no_running_container_message(base_package) -> None:
    print('No container running.\n')
    print('From within the repository, run:\n')
    print('    docker start {}\n'.format(base_package))
    print('If the container {} doesn\'t exist, then run:\n'.format(base_package))
    print('    osewb container create\n')


def print_multiple_containers_found_message(ose_containers: List[str]) -> None:
    comma_delimited_containers = ', '.join(ose_containers)
    print('Found multiple OSE containers running: {}.'.format(
        comma_delimited_containers))
    print('Executing command within first container: {}.'.format(
        ose_containers[0]))


def get_ose_container_names() -> List[str]:
    container_names = get_container_names()
    ose_containers = [
        name for name in container_names if name.startswith('ose')]
    return ose_containers


def get_container_names(all: bool = False) -> List[str]:
    client = docker.from_env()
    containers = client.containers.list(all=all)
    return [container.name for container in containers]


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
    container_parser = subparsers.add_parser('container',
                                             help='Commands for interacting with containers',
                                             usage='osewb container <command>')
    container_subparser = container_parser.add_subparsers(title='Commands',
                                                          dest='container_command',
                                                          required=True)
    image_parser = container_subparser.add_parser('image',
                                                  help='Build image for container',
                                                  usage='osewb container image')
    create_parser = container_subparser.add_parser('create',
                                                   help='Create container -- must be in workbench repository',
                                                   usage='osewb container create')
    args = vars(parser.parse_args())
    command = args.pop('command')
    return command, args


if __name__ == '__main__':
    main()
