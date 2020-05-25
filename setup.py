import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / 'README.md').read_text()

setup(
    name='ose-workbench-platform',
    description='Common platform for developing Open Source Ecology (OSE) workbenches.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/gbroques/ose-workbench-platform',
    author='G Roques',
    version='0.1.0a2',
    packages=['osewb'],
    entry_points={
        'console_scripts': [
            'osewb = osewb.osewb:main'
        ]
    },
    install_requires=[
        'cookiecutter==1.7.2'
        'docker==4.2.0'
    ]
)
