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

# subtraction
# - IV -> 4.0

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
        test_string = 'XX'
        output = numeral_converter(test_string)
        self.assertEqual(output, 20.0)

    def test_adding_up_two_different_numbers(self):
        test_string = 'VI'
        output = numeral_converter(test_string)
        self.assertEqual(output, 6.0)

    def test_adding_up_three_numbers(self):
        test_string = 'III'
        output = numeral_converter(test_string)
        self.assertEqual(output, 3.0)

    def test_subtracting_two_different_numbers(self):
        test_string = 'IV'
        output = numeral_converter(test_string)
        self.assertEqual(output, 4.0)

    def test_subtracting_two_different_numbers_IX(self):
        test_string = 'IX'
        output = numeral_converter(test_string)
        self.assertEqual(output, 9.0)

    def test_nineteen(self):
        test_string = 'XIX'
        output = numeral_converter(test_string)
        self.assertEqual(19.0, output)

    def test_forty(self):
        test_string = 'XL'
        output = numeral_converter(test_string)
        self.assertEqual(40.0, output)

    def test_fourhundred(self):
        test_string = 'CD'
        output = numeral_converter(test_string)
        self.assertEqual(400.0, output)

    # def test_subtracting_three_different_numbers_IX(self):
    #     test_string = 'XIV'
    #     output = numeral_converter(test_string)
    #     self.assertEqual(output, 14.0)

    # def test_test_all_combination_of_numbers(self):
    #     # acceptance test
    #     test_string = 'MMCDLXVII'
    #     output = numeral_converter(test_string)
    #     self.assertEqual(output, 2467.0)
