import unittest

# Need to import FreeCAD
import FreeCAD as App  # noqa: F401

from {{ cookiecutter.base_package }}.part import Box


class BoxTest(unittest.TestCase):
    """
    Test for Box Part class.
    """

    def test_make(self):
        # Make a 10 x 10 x 10 box
        box = Box.make()
        self.assertEqual(len(box.Faces), 6)
        self.assertAlmostEqual(box.Volume, 1000)
        self.assertAlmostEqual(box.Area, 600)
        self.assertEqual(box.TypeId, 'Part::TopoShape')


if __name__ == '__main__':
    unittest.main()
