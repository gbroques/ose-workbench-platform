import os
import webbrowser


def handle_browse_command(root_of_git_repository: str,
                          browse_subcommand: str) -> None:
    if browse_subcommand == 'docs':
        path_to_index_html = os.path.join(
            root_of_git_repository, 'docs/_build/index.html')
        if not os.path.isfile(path_to_index_html):
            print('No index.html found in {}'.format(path_to_index_html))
            print('To build the documentation, run:\n')
            print('    osewb docs\n')
        else:
            webbrowser.open(path_to_index_html)
    elif browse_subcommand == 'coverage' or browse_subcommand == 'cov':
        path_to_index_html = os.path.join(
            root_of_git_repository, 'htmlcov/index.html')
        if not os.path.isfile(path_to_index_html):
            print('No index.html found in {}'.format(path_to_index_html))
            print('To build the coverage report, run:\n')
            print('    osewb test --coverage\n')
        else:
            webbrowser.open(path_to_index_html)
