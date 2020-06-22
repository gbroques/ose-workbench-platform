import os
from subprocess import PIPE, Popen


def execute_command(command: str,
                    env: dict = {},
                    exit_on_non_zero_code: bool = True) -> int:
    print('Executing the following command:\n')
    print('    {}\n'.format(command))
    environ = os.environ.copy()
    environ.update(env)
    with Popen(command, stdout=PIPE, bufsize=1, universal_newlines=True, shell=True, env=environ) as process:
        for line in process.stdout:
            print(line, end='')
    if process.returncode != 0 and exit_on_non_zero_code:
        exit(1)
    return process.returncode
