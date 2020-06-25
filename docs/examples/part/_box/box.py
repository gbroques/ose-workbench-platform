import Part


class Box:
    """Represents a box."""

    @staticmethod
    def make() -> Part.Shape:
        """Make a box.

        :return: The shape of a box.
        :rtype: Part.Shape
        """
        return Part.makeBox(10, 10, 10)
