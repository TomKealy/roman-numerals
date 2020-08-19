import unittest
from roman_numerals import numeral_converter


# basic valus
# - I-> 1.0
# - V -> 5.
# - X -> 10,
# - L -> 50
# - C -> 100
# - D -> 500
# - M -> 1000


# addition
# - II-> 2.0

class TestRomanNumerals(unittest.TestCase):

    def test_single_number(self):
        test_string = 'I'
        output = numeral_converter(test_string)
        self.assertEqual(output, 1.0)

    def test_basic_value_5(self):
        test_string = 'V'
        output = numeral_converter(test_string)
        self.assertEqual(output, 5.0)

    def test_adding_up_two_numbers(self):
        test_string = 'II'
        output = numeral_converter(test_string)
        self.assertEqual(output, 2.0)

    def test_adding_up_two_numbers_XX(self):
        test_string = 'VV'
        output = numeral_converter(test_string)
        self.assertEqual(output, 6.0)

    def test_test_all_combination_of_numbers(self):
        # acceptance test
        test_string = 'MMCDLXVII'
        output = numeral_converter(test_string)
        self.assertEqual(output, 2467.0)
