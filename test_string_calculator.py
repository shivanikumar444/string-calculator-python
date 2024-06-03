# test_string_calculator.py

import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_one_number(self):
        self.assertEqual(self.calc.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calc.add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(self.calc.add("1,2,3,4"), 10)

    def test_new_lines_between_numbers(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)

    def test_different_delimiter(self):
        self.assertEqual(self.calc.add("//;\n1;2"), 3)

if __name__ == "__main__":
    unittest.main()
