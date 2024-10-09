def decimal_to_ieee754_32bit(decimal_number):

    # Handle the sign bit
    sign_bit = '1' if decimal_number < 0 else '0'
    decimal_number = abs(decimal_number)

    # Handle zero case
    if decimal_number == 0.0:
        return sign_bit + '00000000' + '00000000000000000000000'

    # Normalize the number to the range [1, 2) by shifting (for exponent calculation)
    exponent = 0
    if decimal_number >= 2:
        while decimal_number >= 2:
            decimal_number /= 2
            exponent += 1
    elif decimal_number < 1:
        while decimal_number < 1:
            decimal_number *= 2
            exponent -= 1

    # IEEE 754 bias for 32-bit floating point (127)
    exponent_bits = f'{(exponent + 127):08b}'

    # Now we have the normalized number in the form 1.xxxx
    # We remove the leading 1 and keep the fraction part as mantissa
    decimal_number -= 1  # Remove the leading 1
    mantissa_bits = ''
    for _ in range(23):
        decimal_number *= 2
        if decimal_number >= 1:
            mantissa_bits += '1'
            decimal_number -= 1
        else:
            mantissa_bits += '0'

    # Combine sign bit, exponent bits, and mantissa bits
    ieee754_representation = sign_bit + exponent_bits + mantissa_bits
    return ieee754_representation

