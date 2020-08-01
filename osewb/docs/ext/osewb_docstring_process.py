import inspect
import os
import re
from os import listdir
from os.path import isfile, join

from sphinx.application import Sphinx
from sphinx.util.logging import getLogger

from osewb.find_base_package import find_root_of_git_repository

logger = getLogger(__name__)

# TODO: Make lint rule to enforce these naming conventions
class_pattern_template = r'ose[A-Za-z0-9]+\.{}\.[A-Z][A-Za-z]+'
part_class_pattern = re.compile(class_pattern_template.format('part'))
model_class_pattern = re.compile(class_pattern_template.format('model'))

icon_package_pattern = re.compile(r'freecad\.ose[A-Za-z0-9]+\.icon')

repo_root = find_root_of_git_repository()
if repo_root is None:
    print('Must be in git repository')
    exit(1)
screenshot_dir = os.path.join(repo_root, 'docs', '_static', 'screenshot')
img_path_template = os.path.join(screenshot_dir, '{}.png')


def process_docstring(app, what, name, obj, options, lines):
    if what == 'module' and icon_package_pattern.match(name):
        icon_directory = os.path.dirname(obj.__file__)
        icons = [f for f in listdir(icon_directory) if isfile(
            join(icon_directory, f)) and not f.endswith('.py')]
        lines.append('Icons')
        lines.append('-----')
        lines.append('')
        sorted_icons = sorted(icons)
        lines.append('.. list-table::')
        lines.append('   :header-rows: 1')
        lines.append('')
        lines.append('   * - Icon')
        lines.append('     - Filename')
        for icon in sorted_icons:
            lines.append('   * - :fcicon:`{} (md) <{}>`'.format(icon, icon))
            lines.append('     - ``{}``'.format(icon))
        lines.append('')
        lines.append('----')
        lines.append('')
    elif what == 'class':
        if part_class_pattern.match(name):
            class_name = obj.__name__
            if os.path.exists(img_path_template.format(class_name)):
                lines.append(
                    '.. image:: /_static/screenshot/{}.png'.format(class_name))
                lines.append('   :alt: {}'.format(class_name))
            else:
                logger.warning(
                    'Screenshot for part "{}" missing. Try running `osewb docs screenshot`.'.format(class_name))
        elif model_class_pattern.match(name) and name.endswith('Model'):
            lines.append('.. fc-custom-property-table::')


def setup(app: Sphinx) -> None:
    """Setup extension.

    :param app: application object controlling high-level functionality,
                such as the setup of extensions, event dispatching, and logging.
                See Also:
                https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx
    """
    app.connect('autodoc-process-docstring', process_docstring)
    if not os.path.exists(screenshot_dir):
        logger.warning(
            'No screenshot directory detected.\nTo generate part screenshots, run:\n\n    osewb docs screenshot\n')


__all__ = ['setup']
