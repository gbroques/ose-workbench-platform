import argparse


def main():
    sub_command = _parse_sub_command()
    print("Sub command: {}".format(sub_command))


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
