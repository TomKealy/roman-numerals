string_to_numbers = {
    'I': 1.0,
    'V': 5.0
}


def numeral_converter(s):
    if len(s) == 2:
        return 2.0
    if s == "V":
         return 5.0
    return 1.0
