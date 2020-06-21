from subprocess import PIPE, Popen


def execute_command(command: str) -> None:
    print('Executing the following command:\n')
    print('    {}\n'.format(command))
    with Popen(command, stdout=PIPE, bufsize=1, universal_newlines=True, shell=True) as process:
        for line in process.stdout:
            print(line, end='')
    if process.returncode != 0:
        exit(1)
