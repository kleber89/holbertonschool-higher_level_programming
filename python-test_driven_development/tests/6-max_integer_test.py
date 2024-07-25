import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegers(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([1, 2, 3, 2]), 3)

    def test_not_parmts(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def testIntNegative(self):
        self.assertEqual(max_integer([-2, -1, 0, 1]), 1)
        self.assertEqual(max_integer([-1, -2, -3]), -1)


if __name__ == '__main__':
    unittest.main()