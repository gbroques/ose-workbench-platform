import os
from subprocess import PIPE, Popen
from typing import List


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


def chain_commands(*commands: str,
                   env: dict = {},
                   exit_on_non_zero_code: bool = True) -> List[int]:
    return_codes = []
    for command in commands:
        return_code = execute_command(command, env=env,
                                      exit_on_non_zero_code=exit_on_non_zero_code)
        return_codes.append(return_code)
    return return_codes
