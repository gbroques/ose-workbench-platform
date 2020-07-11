"""Utility script to automatically create thumbnail screenshots of parts.

Run with freecad -c part_screenshot.py when conda environment is activated.
"""
import importlib
import inspect
import os
from pathlib import Path

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


if __name__ == '__main__':
    main()
