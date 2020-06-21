import Part


class {{ name }}:

    @staticmethod
    def make() -> Part.Shape:
        return Part.makeBox(10, 10, 10)
