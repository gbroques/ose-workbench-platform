# OSE Workbench Platform
A platform for developing CAD workbenches for Open Source Ecology (OSE).

OSE defines a "CAD workbench" as a set of tools in CAD software to design and make a particular machine.

Each CAD workbench OSE develops for one of it's machines has certain common devlopment-time or "dev-time" needs and dependencies.

For example, open source CAD software like FreeCAD, running unit tests, making documentation, and generating code to streamline workbench development.

Rather than duplicate the approaches to each of these needs, `ose-workbench-platform` abstracts those needs into a common platform so they aren't the concern of individual OSE workbench maintainers.

Each workbench maintainer doesn't need to know or care about the particular versions and libraries we use to solve those needs, nor the particular configuration.

Having a common platform for OSE workbench development also makes it easier for developers to readily switch between workbenches by providing a common toolset.

`ose-workbench-platform` provides a command-line interface (CLI), via the `osewb` command, containing commands for common dev-time tasks such as running FreeCAD, running all tests, making documentation, generating a new workbench, and even generating code for common tasks and patterns.

## Open Source CAD Software
FreeCAD is OSE's open-source CAD software of choice.

Currently, OSE chooses to use FreeCAD 16, or "legacy FreeCAD".

It's expected and encouraged that all OSE contributors use the same version of FreeCAD to maximize collaboration.

To run a built-in version of FreeCAD 16 within `ose-workbench-platform`, run:

    osewb run

## Unit Tests
The test framework we choose to use is Pytest.

To run the entire unit-test suite of a workbench, within the root of a OSE workbench repository, run:

    osewb test

## Documentation
For building documentation we use Sphinx.

To build the documentation of a workbench, within the root of a OSE workbench repository, run:

    osewb docs

## Generating New Workbenches
Navigate to where you want to generate a directory for your new workbench. Then run:

    osewb generate <name>

Where `name` is the name of the machine for your new workbench.

For example,

    osewb generate tractor

Will generate a new directory called `ose-tractor-workbench` with the basic structure and files needed for the workbench.

## Generating Code
Within the root of a workbench repository, run the `make` command.

For example,

    osewb make command AddMotor

Will generate a new `AddMotor` command class.
