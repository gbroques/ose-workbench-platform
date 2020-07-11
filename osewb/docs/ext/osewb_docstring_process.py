import inspect
import re

from sphinx.application import Sphinx

# TODO: Make lint rule to enforce these naming conventions
class_pattern_template = r'ose[A-Za-z0-9]+\.{}\.[A-Z][A-Za-z]+'
part_class_pattern = re.compile(class_pattern_template.format('part'))
model_class_pattern = re.compile(class_pattern_template.format('model'))


def process_docstring(app, what, name, obj, options, lines):
    if what == 'class':
        if part_class_pattern.match(name):
            class_name = obj.__name__
            lines.append(
                '.. image:: /_static/screenshot/{}.png'.format(class_name))
            lines.append('   :alt: {}'.format(class_name))
        elif model_class_pattern.match(name) and name.endswith('Model'):
            lines.append('.. fc-custom-property-table::')


def setup(app: Sphinx):
    """The application object controlling high-level functionality, such as the setup of extensions, event dispatching, and logging.

    See Also:
        https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx

    :param app: 
    :type app: Sphinx
    """
    app.connect('autodoc-process-docstring', process_docstring)


__all__ = ['setup']
