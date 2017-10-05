import unittest
import task6part1


class TestToRoman(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(task6part1.to_roman(2345), "MMCCCXLV")

    def test_create_raises(self):
        with self.assertRaises(task6part1.NonValidInput):
            task6part1.to_roman(5555)

    def test_boundary_values(self):
        self.assertEqual(task6part1.to_roman(1), "I")
        self.assertEqual(task6part1.to_roman(5000), "MMMMM")

    def test_not_correct(self):
        self.assertNotEqual(task6part1.to_roman(2222), "MMCCXXIII")
