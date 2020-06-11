import io
from os import path

from setuptools import setup

current_dir = path.abspath(path.dirname(__file__))
with io.open(path.join(current_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ose-workbench-platform',
    description='Common platform for developing Open Source Ecology (OSE) workbenches.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gbroques/ose-workbench-platform',
    author='G Roques',
    version='0.1.0a18',
    packages=['osewb', 'osewb.docs', 'osewb.docs.ext'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'osewb = osewb.osewb:main'
        ]
    },
    install_requires=[
        # -----------------------
        # | Source Requirements |
        # -----------------------
        'cookiecutter==1.7.2',
        'jinja2-time==0.2.0',
        'docker==4.2.0',

        # ---------------------
        # | Docs Requirements |
        # ---------------------
        'sphinx==3.0.2',
        'sphinx-rtd-theme==0.4.3'
    ]
)
