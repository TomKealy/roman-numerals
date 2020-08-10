import unittest
from roman_numerals import numeral_converter


class TestRomanNumerals(unittest.TestCase):

    def test_single_number(self):
        test_string = 'I'
        output = numeral_converter(test_string)
        self.assertEqual(output, 1.0)