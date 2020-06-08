#!/usr/bin/env python3
"""
Script to generate CSV files,
documenting the custom properties of model objects in a tabular format.

Assumptions:
    * Assumes models will be exported from __init__.py
      of <base package>.app.model package
    * Assumes model class names end with a "Model" suffix (e.g. "FrameModel").
    * Assumes models classes only have one required argument in the constructor
      which is the Part::FeaturePython document object.
"""
import csv
import importlib
import os
import sys
from collections import OrderedDict

import FreeCAD as App


def main():
    if (len(sys.argv) != 2):
        print('Usage: generate_property_tables.py <base package>')
    base_package = sys.argv[1]
    model_module_name = '{}.app.model'.format(base_package)

    try:
        model_module = importlib.import_module(model_module_name)
    except ImportError:
        print('No {}.app.model package. Skipping generation of Model property tables.'.format(
            model_module_name))
        return
    models = [a for a in dir(model_module) if a.endswith('Model')]
    for model in models:
        class_ = getattr(model_module, model)

        document = App.newDocument()

        feature_python = document.addObject(
            'Part::FeaturePython', 'FeaturePython')
        feature_python_attrs = [x for x in dir(feature_python)]

        obj = document.addObject('Part::FeaturePython', 'FeaturePython')
        class_(obj)
        custom_obj_attrs = [x for x in dir(
            obj) if x not in feature_python_attrs]

        columns = ['Name', 'Type', 'Default Value', 'Description']
        rows = build_rows(custom_obj_attrs, obj)

        if not os.path.exists('./docs/property_table'):
            os.makedirs('./docs/property_table')
        file = os.path.join('./docs/property_table',
                            '{}PropertyTable.csv'.format(model))

        print('Writing {}'.format(file))

        write_dict_list_to_csv(rows, columns, file)


def build_rows(custom_obj_attrs, obj):
    rows = []
    for attr in custom_obj_attrs:
        description = obj.getDocumentationOfProperty(attr)
        property_type = obj.getTypeIdOfProperty(attr)
        human_readable_property = property_type.replace('App::Property', '')
        default_value = getattr(obj, attr)
        rows.append(OrderedDict([
            ('Name', '**{}**'.format(pascal_case_to_human_readable(attr))),
            ('Type', '``{}``'.format(human_readable_property)),
            ('Default Value', default_value),
            ('Description', description)
        ]))
    return rows


def pascal_case_to_human_readable(str):
    words = [[str[0]]]

    for c in str[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)

    return ' '.join([''.join(word) for word in words])


def write_dict_list_to_csv(dict_list, columns, filename):
    try:
        with open(filename, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=columns)
            writer.writeheader()
            for row in dict_list:
                writer.writerow(row)
    except IOError as e:
        print(str(e))


if __name__ == '__main__':
    main()
