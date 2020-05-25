# OSE Workbench Platform
A platform for developing workbenches for Open Source Ecology (OSE).

OSE defines a "workbench" as a set of tools in CAD software to design and make a particular machine.

Each workbench OSE develops for one of it's machines has certain common development-time or "dev-time" needs and dependencies.

For example, running unit tests, making documentation, and generating code to streamline workbench development.

Rather than duplicate the approaches to each of these needs, `ose-workbench-platform` abstracts those needs into a common platform so they aren't the concern of individual OSE workbench maintainers.

Each workbench maintainer doesn't need to know or care about the particular versions and libraries we use to solve those needs, nor the particular configuration.

Having a common platform for OSE workbench development also makes it easier for developers to readily switch between workbenches by providing a common tool-set.

`ose-workbench-platform` provides a command-line interface (CLI), via the `osewb` command, containing commands for common dev-time tasks such as running all tests, making documentation, initializing new workbenches, and even generating code for common tasks.

## Unit Tests
The test framework we choose to use is Pytest.

To run the entire unit-test suite of a workbench, within the root of a OSE workbench repository, run:

    osewb test

## Documentation
For building documentation we use Sphinx.

To build the documentation of a workbench, within the root of a OSE workbench repository, run:

    osewb docs

## Initializing a New Workbench
Navigate to where you want to initialize a directory for your new workbench. Then run:

    osewb init

You'll be prompted to enter the machine name in **Title Case**.
```
machine_display_name [CEB Brick Press]: Tractor ↵
```

Then, you'll be prompted for several more values.

Each successive prompt derives it's default value from answers to previous prompts.

You can press the <kbd>Enter</kbd> key for most prompts to stick with the defaults.
```
repo_name [ose-tractor-workbench]: ↵
machine_title [OSE Tractor]: ↵
workbench_title [OSE Tractor Workbench]: ↵
base_package [osetractor]: ↵
command_registry_filename [OSE-Tractor]: ↵
command_namespace [OSETractor]: ↵
workbench_class_filename [tractor_workbench]: ↵
workbench_class_name [TractorWorkbench]: ↵
```

The above examples initializes a new workbench, in a `ose-tractor-workbench` directory, with the basic structure and files needed for the workbench.

```
ose-tractor-workbench
    ├── InitGui.py
    ├── osetractor
    │   ├── app
    │   │   ├── __init__.py
    │   │   └── part
    │   │       ├── box
    │   │       │   ├── box.py
    │   │       │   └── __init__.py
    │   │       └── __init__.py
    │   ├── gui
    │   │   ├── command
    │   │   │   ├── add_box
    │   │   │   │   ├── add_box_command.py
    │   │   │   │   └── __init__.py
    │   │   │   └── __init__.py
    │   │   ├── icon
    │   │   │   ├── Box.svg
    │   │   │   └── __init__.py
    │   │   ├── __init__.py
    │   │   ├── OSE-Tractor.py
    │   │   └── tractor_workbench.py
    │   └── __init__.py
    └── README.md
```

![OSE Tractor Workbench](./ose-tractor-workbench.png)

## Generating Code
Within the root of a workbench repository, run the `make` command.

For example,

    osewb make command AddMotor

Will generate a new `AddMotor` command class.

## Developing Locally
Run the following command from the root of the repository:

    pip install -e .

See ["Editable Installs"](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs) on the pip docs for additional information.

This will give you access to the `osewb` command locally for testing any changes to the source code.

## Deploying to PyPi
From the root of repository:

1. `python setup.py sdist`

2. `twine upload dist/*`
    * `pip install twine` (if not already installed)

You'll be prompted for your [PyPi](https://pypi.org/) username and password.
```
Enter your username: 
Enter your password: 
```
