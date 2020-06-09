"""
Adds a ``.. model-property-table::`` directive to create a table documenting the properties of model objects.

Must add the ``.. model-property-table::`` directive to the docstring of a model class.

Model objects are also known as "FeaturePython Objects" or "Scripted Objects" in the FreeCAD community.

See `BoxModel for an example <examples/examples.html#module-examples.box_model>`_.
"""
import importlib
import re

from docutils import nodes
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

import FreeCAD as App

logger = logging.getLogger(__name__)


class ModelPropertyTable(SphinxDirective):

    has_content = False

    def run(self):
        source_info = self.get_source_info()
        source = source_info[0]
        pattern = re.compile('.* of (.*)')
        # (e.g. osewb.docs.ext.box_model.BoxModel)
        class_path = pattern.match(source).group(1)
        class_path_parts = class_path.split('.')
        # (e.g. BoxModel)
        class_name = class_path_parts[-1]
        # (e.g. osewb.docs.ext.box_model)
        module_path = '.'.join(class_path_parts[:-1])
        model_module = importlib.import_module(module_path)
        class_ = getattr(model_module, class_name)
        document = App.newDocument()
        obj = document.addObject('Part::FeaturePython', 'FeaturePython')
        feature_python = document.addObject(
            'Part::FeaturePython', 'FeaturePython')
        feature_python_attrs = [x for x in dir(feature_python)]
        try:
            class_(obj)
            custom_obj_attrs = [x for x in dir(
                obj) if x not in feature_python_attrs]
            data = _build_rows(custom_obj_attrs, obj)
        except TypeError:
            logger.warning(
                'Unable to instantiate {}.\n'.format(class_name) +
                'Expecting constructor signature:\n' +
                "    obj = document.addObject('Part::FeaturePython', 'FeaturePython')\n" +
                '    {}(obj)\n'.format(class_name) +
                'Defaulting to model property table with no rows.', location=source_info)
            data = []
        return _build_property_table(data)


def _pascal_case_to_human_readable(str):
    words = [[str[0]]]

    for c in str[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)

    return ' '.join([''.join(word) for word in words])


def _build_property_table(data):
    header = (
        nodes.paragraph(text='Name'),
        nodes.paragraph(text='Type'),
        nodes.paragraph(text='Default Value'),
        nodes.paragraph(text='Description')
    )
    colwidths = (1, 1, 1, 1)
    table = nodes.table()
    tgroup = nodes.tgroup(cols=len(header))
    table += tgroup
    for colwidth in colwidths:
        tgroup += nodes.colspec(colwidth=colwidth)
    thead = nodes.thead()
    tgroup += thead
    thead += create_table_row(header)
    tbody = nodes.tbody()
    tgroup += tbody
    for data_row in data:
        tbody += create_table_row(data_row)
    return [table]


def _build_rows(custom_obj_attrs, obj):
    rows = []
    for attr in custom_obj_attrs:
        description = obj.getDocumentationOfProperty(attr)
        property_type = obj.getTypeIdOfProperty(attr)
        default_value = getattr(obj, attr)
        rows.append((
            nodes.strong(text=_pascal_case_to_human_readable(attr)),
            nodes.literal(text=property_type),
            nodes.paragraph(text=default_value),
            nodes.paragraph(text=description)
        ))
    return rows


def create_table_row(row_cells):
    row = nodes.row()
    for cell in row_cells:
        entry = nodes.entry()
        row += entry
        entry += cell
    return row


def setup(app):
    app.add_directive('model-property-table', ModelPropertyTable)

    return {
        'version': '0.1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
