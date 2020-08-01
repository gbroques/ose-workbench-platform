"""Shared base configuration for OSE workbench documentation."""
import os
import sys

# Add lib folder of conda env to sys.path for building docs on Read the Docs
# and importing FreeCAD
on_read_the_docs = os.environ.get('READTHEDOCS') == 'True'
if on_read_the_docs:
    conda_lib_path = os.path.join(
        os.environ['CONDA_ENVS_PATH'], os.environ['CONDA_DEFAULT_ENV'], 'lib')
    sys.path.append(conda_lib_path)

# Configuration for Sphinx Python Documentation Generator
# https://www.sphinx-doc.org/en/master/usage/configuration.html
conf = {
    # Read the Docs Sphinx Theme
    # Designed for great reader experience on both desktop and mobile devices.
    # https://github.com/readthedocs/sphinx_rtd_theme
    'html_theme': 'sphinx_rtd_theme',
    'html_css_files': [
        'https://ose-workbench-platform.readthedocs.io/en/latest/_static/theme_overrides.css'
    ],

    # Path that contains extra templates (or templates that overwrite builtin/theme-specific templates).
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-templates_path
    'templates_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),

    # Path to image file that is the logo of the docs.
    # It is placed at the top of the sidebar; its width should therefore not exceed 200 pixels.
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo
    'html_logo': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ose-sticker-logo.svg'),

    # Whether module names are prepended to all object names
    # (for object types where a “module” of some kind is defined),
    # e.g. for py:function directives. Default is True.
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-add_module_names
    'add_module_names': False,

    # List of strings that are module names of extensions.
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions
    'extensions': [

        # Include documentation from docstrings
        # https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
        'sphinx.ext.autodoc',

        # Helps with having many external links that point to the OSE Wiki.
        # https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
        'sphinx.ext.extlinks',

        # Enables localization of theme strings in translated output
        'sphinx_rtd_theme',

        # Link to other projects' documentation
        'sphinx.ext.intersphinx',

        # Custom OSE Workbench Sphinx Extensions
        # See respective docstring
        'osewb.docs.ext.all_summary_table',
        'osewb.docs.ext.freecad_custom_property_table',
        'osewb.docs.ext.freecad_icon',
        'osewb.docs.ext.osewb_docstring_process'
    ],

    # Base configuration for the above Sphinx extensions
    'ext': {
        'autodoc': {
            # List of modules to be mocked up.
            # Useful when some external dependencies are not met at build time,
            # and break the build process.
            # https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_mock_imports
            'autodoc_mock_imports': [
                'FreeCADGui'
            ],
            # How to represents typehints.
            # description - Show typehints as content of function or method
            # https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_typehints
            'autodoc_typehints': 'description'
        },
        'extlinks': {
            # Dictionary of external sites,
            # mapping unique short alias names to a base URL and a prefix.
            # https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#confval-extlinks
            'extlinks': {
                'osewikipage': (
                    'https://wiki.opensourceecology.org/wiki/%s', ''
                ),
                'freecadwikipage': (
                    'https://wiki.freecadweb.org/%s', ''
                )
            }
        },
        'intersphinx': {
            'intersphinx_mapping': {
                # Add links to Python standard library documentation
                # 'None' means to download the corresponding objects.inv file from the Internet.
                # https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_mapping
                'python': ('https://docs.python.org/3', None)
            }
        },
        'freecad_custom_property_table': {
            'remove_app_property_prefix_from_type': True
        }
    }
}
