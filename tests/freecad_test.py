import unittest

# Need to import FreeCAD
import FreeCAD as App
import Part


class FreeCADTest(unittest.TestCase):
    """
    Sanity test for FreeCAD integration.
    """

    def test_freecad(self):
        box = Part.makeBox(10, 10, 10)
        self.assertEqual(len(box.Faces), 6)
        self.assertAlmostEqual(box.Volume, 1000)
        self.assertAlmostEqual(box.Area, 600)
        self.assertEqual(box.TypeId, 'Part::TopoShape')


if __name__ == '__main__':
    unittest.main()
