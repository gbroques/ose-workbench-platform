from setuptools import setup

setup(
    name='{{ cookiecutter.repo_name }}',
    version='0.1.0',
    packages=[
        'freecad',
        'freecad.{{ cookiecutter.base_package }}',
        '{{ cookiecutter.base_package }}'
    ],
    author='{{ cookiecutter.owner_name }}',
    description='A FreeCAD workbench for designing {{ cookiecutter.machine_display_name }} machines by Open Source Ecology (OSE).',
    install_requires=[],
    include_package_data=True
)
