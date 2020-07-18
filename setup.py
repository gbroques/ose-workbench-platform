import io
from os import path

from setuptools import setup

version = {}
with open('osewb/_version.py') as fp:
    exec(fp.read(), version)

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
    version=version['__version__'],
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
        'Jinja2<3.0.0',  # Also a requirement of cookiecutter
        'jinja2-time>=0.2.0',  # Also a requirement of cookiecutter

        # ----------------------------
        # | Docs Requirements        |
        # | Also in environment.yaml |
        # ----------------------------
        'sphinx==3.1.1',
        'sphinx-rtd-theme==0.5.0',

        # ---------------------
        # | Test Requirements |
        # ---------------------
        'coverage==5.1',
        'coveralls==2.0.0',
        'pytest==5.4.3',
        'pytest-cov==2.9.0',

        # ---------------------
        # | Lint Requirements |
        # ---------------------
        'flake8==3.8.3',
        'flake8-colors==0.1.6',
        'flake8-isort==3.0.0',
        'isort==4.3.21',
        'autopep8==1.5.3',
        'mypy==0.781',
        'pydocstyle==5.0.2',
        'rope==0.17.0'
    ],
    classifiers=[
        # Full List: https://pypi.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 3 :: Only'
    ]
)
