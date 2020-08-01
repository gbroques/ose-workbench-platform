import inspect

from sphinx.application import Sphinx


def process_docstring(app, what, name, obj, options, lines):
    if what == 'module':
        mutate_module_docstring_lines(obj, name, lines)

def mutate_module_docstring_lines(obj, name, lines):
    public_members = []
    if hasattr(obj, '__all__'):
        public_members = obj.__all__
    all_members = inspect.getmembers(obj)
    members = [
        (
            name + '.' + member[0],
            get_summary_line(inspect.getdoc(member[1]))
        )
        for member in all_members
        if not member[0].startswith('_')
        and member[0] in public_members
        and not inspect.isbuiltin(member[1])
        and (inspect.isclass(member[1]) or inspect.isfunction(member[1]))
    ]
    if len(members):
        lines.append('')
        lines.append('.. list-table::')
        lines.append('   :header-rows: 1')
        lines.append('')
        lines.append('   * - Name')
        lines.append('     - Description')
        lines.append('')
    for member, summary in members:
        lines.append('   * - :mod:`~{}`'.format(member))
        if summary:
            lines.append('     - ' + summary)
        else:
            lines.append('     - None')
        lines.append('')
    if len(members):
        lines.append('')
        lines.append('----')
        lines.append('')


def get_summary_line(docstring):
    if docstring is None:
        return None
    return docstring.splitlines()[0]


def setup(app: Sphinx) -> None:
    """Setup extension.

    :param app: application object controlling high-level functionality,
                such as the setup of extensions, event dispatching, and logging.
                See Also:
                https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx
    """
    app.connect('autodoc-process-docstring', process_docstring)


__all__ = ['setup']
