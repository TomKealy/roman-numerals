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
    final = 0.0
    for char in s:
        final = final + string_to_numbers[char]

    if "IV" in s or "IX" in s:
        final -= 2 * string_to_numbers['I']

    pos = s[0]
    if 'XL' in s:
        final -= 2 * string_to_numbers[pos]

    if 'CD' in s:
        final -= 2 * string_to_numbers[pos]
    return final
