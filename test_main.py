import unittest
from main import add_numbers


class TestMain(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(-5, -3), -8)

    def test_add_floats(self):
        self.assertAlmostEqual(add_numbers(2.5, 3.1), 5.6)
        self.assertAlmostEqual(add_numbers(-1.5, 1.5), 0.0)


if __name__ == "__main__":
    unittest.main()
