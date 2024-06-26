#!/usr/bin/python3
import unittest
from your_module import max_integer  # Replace 'your_module' with the actual module name where max_integer is defined

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test that an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test that a single element list returns that element."""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """Test a list of positive numbers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list of mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_duplicates(self):
        """Test a list with duplicate numbers."""
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    def test_floats(self):
        """Test a list with floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5, 3.5]), 3.5)

    def test_mixed_integers_floats(self):
        """Test a list with both integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_large_numbers(self):
        """Test a list with large numbers."""
        self.assertEqual(max_integer([1000000000, 2000000000, 3000000000]), 3000000000)

    def test_strings(self):
        """Test a list with strings should raise a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

    def test_none(self):
        """Test that passing None raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
