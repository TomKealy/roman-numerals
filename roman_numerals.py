string_to_numbers = {
    'I': 1.0,
    'V': 5.0,
    'X': 10.0,
    'L': 50.0,
    'C': 100.0,
    'D': 500.0,
    'M': 1000.0
}


def numeral_converter(s):
    """
    Function to convert roman numerals to floats
    :param s: string
    :return: flat
    """
    if len(s) == 2:
        return string_to_numbers[s[0]] + string_to_numbers[s[1]]
    return string_to_numbers[s]
