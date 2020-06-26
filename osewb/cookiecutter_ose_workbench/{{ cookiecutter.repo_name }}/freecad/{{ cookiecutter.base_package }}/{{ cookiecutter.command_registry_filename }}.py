"""Command Registry Module"""
import FreeCADGui as Gui

from .command import AddBoxCommand

#: Command Namespace
command_namespace = '{{ cookiecutter.command_namespace }}'


def register_commands():
    """
    Register all workbench commands,
    and associate them to toolbars, menus, sub-menus, and context menu.
    """
    add_box_key = _register(AddBoxCommand.NAME, AddBoxCommand())

    #: Main Toolbar Commands
    main_toolbar_commands = [
        add_box_key
    ]

    #: Main Menu Commands
    main_menu_commands = [
        add_box_key
    ]

    return main_toolbar_commands, main_menu_commands


def _register(name, command):
    key = '{}_{}'.format(command_namespace, name)
    Gui.addCommand(key, command)
    return key
