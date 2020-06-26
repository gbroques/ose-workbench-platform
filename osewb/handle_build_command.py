from .execute_command import chain_commands


def handle_build_command() -> None:
    return_codes = chain_commands('osewb test --coverage',
                                  'osewb lint',
                                  'osewb docs',
                                  exit_on_non_zero_code=False)
    return_code_pairs = zip(('test', 'lint', 'docs'), return_codes)
    if any(return_codes):
        # TODO: There's some duplication between this and the lint command.
        #       see handle_lint_command.py
        print('Build failed with errors from the following command(s):')
        commands_with_errors = [pair[0]
                                for pair in return_code_pairs if pair[1]]
        print('    {}\n'.format(', '.join(commands_with_errors)))
        exit(1)
    else:
        print('Build passed.')
