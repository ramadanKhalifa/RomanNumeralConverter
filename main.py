def int_to_roman(num: int) -> str:
    """
    convert an integer number to a Roman numeral.
    :param num: integer number between 1:3999 inclusive.
    :return: Roman numeral (string).
    """
    if num < 1 or num > 3999:
        raise ValueError("Invalid input:({})! Roman numeral is only valid between 1 and 3999.".format(num))
    int_roman_pairs = (
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    )
    result = ''
    for int_value, roman_char in int_roman_pairs:
        symbols_count = num // int_value
        if symbols_count == 0:
            continue
        result += roman_char * symbols_count
        num -= int_value * symbols_count
    return result


assert int_to_roman(2002) == "MMII"
assert int_to_roman(1999) == "MCMXCIX"
assert int_to_roman(42) == "XLII"
assert int_to_roman(1) == "I"
assert int_to_roman(5) == "V"
assert int_to_roman(10) == "X"
assert int_to_roman(50) == "L"
assert int_to_roman(100) == "C"
assert int_to_roman(500) == "D"
assert int_to_roman(1000) == "M"
assert int_to_roman(3999) == "MMMCMXCIX"
assert int_to_roman(36) == "XXXVI"
# assert int_to_roman(4000) == "M" #  should raise an exception.
# assert int_to_roman(0) == "M" #  should raise an exception.
