from typing import Union

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

    def __getstate__(self) -> Union[str, tuple]:
        """Execute when serializing and persisting the object.

        See Also:
            https://docs.python.org/3/library/pickle.html#object.__getstate__

        :return: state
        """
        return self.Type

    def __setstate__(self, state: str) -> None:
        """Execute when deserializing the object.

        See Also:
            https://docs.python.org/3/library/pickle.html#object.__setstate__

        :param state: state, in this case type of object.
        """
        if state:
            self.Type = state