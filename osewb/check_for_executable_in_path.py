import shutil


def check_for_executable_in_path(executable_name) -> None:
    if shutil.which(executable_name) is None:
        print('{} must be installed, and available in your PATH.'.format(
            executable_name))
        exit(0)
