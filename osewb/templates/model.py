import Part
from osecore.app.model import Model
{%- if part and base_package %}
from {{ base_package }}.part import {{ part }}
{%- endif %}


class {{ name }}Model(Model):

    Type = 'OSE{{ name }}'

    def __init__(self, obj):
        super({{ name }}Model, self).__init__(obj)
        # TODO: Add custom properties
        # obj.addProperty('App::PropertyLength', 'PropertyName',
        #         'Base', 'Descriptive tooltip').PropertyName = 10.0

    def execute(self, obj):
        """
        Called on document recompute
        """
        {%- if part %}
        obj.Shape = {{ part }}.make()
        {%- else %}
        obj.Shape = Part.makeBox(10, 10, 10)
        {%- endif %}

    def __getstate__(self):
        return self.Type

    def __setstate__(self, state):
        if state:
            self.Type = state
