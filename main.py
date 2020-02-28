def int_to_roman(num: int) -> str:
    pass


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
