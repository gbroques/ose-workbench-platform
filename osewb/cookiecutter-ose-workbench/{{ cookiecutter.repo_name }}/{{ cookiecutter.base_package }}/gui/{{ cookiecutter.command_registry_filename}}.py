import FreeCADGui as Gui

from .command.add_box import AddBoxCommand

#: Command Namespace: Must be unique to all FreeCAD workbenches.
command_namespace = '{{ cookiecutter.command_namespace }}'


def register_commands():
    """
    Register all workbench commands,
    and associate them to toolbars, menus, sub-menus, and context menu.
    """
    add_box_key = register(AddBoxCommand.NAME, AddBoxCommand())

    #: Main Toolbar Commands
    main_toolbar_commands = [
        add_box_key
    ]

    #: Main Menu Commands
    main_menu_commands = [
        add_box_key
    ]

    return main_toolbar_commands, main_menu_commands


def register(name, command):
    """Register a command via Gui.addCommand.
    FreeCAD uses the filename where Gui.addCommand is executed as a category
    to group commands together in it's UI.
    """
    key = from_command_name_to_key(name)
    Gui.addCommand(key, command)
    return key


def from_command_name_to_key(command_name):
    return '{}_{}'.format(command_namespace, command_name)