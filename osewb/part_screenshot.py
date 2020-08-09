"""Utility script to automatically create thumbnail screenshots of parts.

Run with freecad -c part_screenshot.py when conda environment is activated.
"""
import importlib
import inspect
import logging
import os
from pathlib import Path
from typing import List

import FreeCAD as App
import FreeCADGui as Gui
import Part

from osewb.find_base_package import find_base_package


def main():
    base_package = find_base_package()
    if not base_package:
        exit(0)

    part_package = importlib.import_module(base_package + '.part')

    def is_part_class(x) -> bool:
        return inspect.isclass(x) and not inspect.isbuiltin(x)

    members = inspect.getmembers(part_package, is_part_class)

    # Setup Gui
    Gui.showMainWindow()
    main_window = Gui.getMainWindow()
    main_window.hide()

    # Document needs to be created after Gui is setup
    document = App.newDocument()

    screenshot_path = Path(os.path.join('docs', '_static', 'screenshot'))
    screenshot_path.mkdir(parents=True, exist_ok=True)

    active_view = Gui.getDocument(document.Name).activeView()
    active_view.setCameraType('Orthographic')
    active_view.setAnimationEnabled(False)

    # It's important not to use Qt's QGLFramebufferObject because it crashes when no GUI is shown
    # but Qt's QGLPixelBuffer still works.
    parameter = App.ParamGet("User parameter:BaseApp")
    group = parameter.GetGroup("Preferences/Document")
    group.SetBool("DisablePBuffers", False)

    for (name, part) in members:
        if not hasattr(part, 'make'):
            logging.warning(
                'No make method defined in part "{}". Skipping screenshots.'.format(name))
            # TODO: For some reason continue statement doesn't work here, and we need to use break.
            #       and raise an exception. Exception while processing file: ...
            #       [type object 'AngleFrameConnector' has no attribute 'make']
            break
        required_arguments = get_required_arguments(part.make)
        if len(required_arguments) > 0:
            args_with_quotes = ['"{}"'.format(arg)
                                for arg in required_arguments]
            potentially_plural_argument = 'arguments' if len(required_arguments) > 1 else 'argument'
            logging.warning('make method in part "{}" has required {} {}. Skipping screenshot.'.format(
                name, potentially_plural_argument, format_list(args_with_quotes)))
            continue
        made_part = part.make()
        Part.show(made_part)

        active_view.viewIsometric()
        active_view.fitAll()

        image_name = str(screenshot_path.joinpath('{}.png'.format(name)))
        print('Saving image {}'.format(image_name))
        active_view.saveImage(image_name, 150, 150, 'Transparent')

        document.removeObject('Shape')

    App.closeDocument(document.Name)
    exit(0)


def get_required_arguments(make_method) -> List[str]:
    arg_spec = inspect.getfullargspec(make_method)
    args = arg_spec.args
    if len(arg_spec.args) > 0 and (arg_spec.args[0] == 'cls' or arg_spec.args[0] == 'self'):
        args = arg_spec.args[1:]
    num_defaults = len(arg_spec.defaults)
    return args[:-num_defaults]


def format_list(l):
    if len(l) == 0:
        raise ValueError('List must not be empty.')
    elif len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return l[0] + ' and ' + l[1]
    else:
        elements_excluding_last = l[:-1]
        return ', '.join(elements_excluding_last) + ', and ' + l[-1]


if __name__ == '__main__':
    main()
