def decimal_to_ieee754_32bit(decimal_number):
    import math

    # Handle special cases
    if math.isnan(decimal_number):
        return '01111111110000000000000000000000'  # NaN
    if math.isinf(decimal_number):
        return '01111111100000000000000000000000' if decimal_number > 0 else '11111111100000000000000000000000'
    if decimal_number == 0.0:
        return '10000000000000000000000000000000' if str(decimal_number).startswith('-') else '00000000000000000000000000000000'

    # Determine the sign bit
    sign_bit = '1' if decimal_number < 0 else '0'
    decimal_number = abs(decimal_number)

    # Normalize the number
    exponent = 0
    if decimal_number >= 2:
        while decimal_number >= 2:
            decimal_number /= 2
            exponent += 1
    elif decimal_number < 1:
        while decimal_number < 1:
            decimal_number *= 2
            exponent -= 1

    # Calculate the exponent with the bias of 127
    exponent_bits = bin(exponent + 127)[2:].zfill(8)

    # Calculate the mantissa
    decimal_number -= 1  # Remove the leading 1
    mantissa_bits = ''
    for _ in range(23):
        decimal_number *= 2
        if decimal_number >= 1:
            mantissa_bits += '1'
            decimal_number -= 1
        else:
            mantissa_bits += '0'

    # Combine the sign bit, exponent, and mantissa
    ieee754_representation = sign_bit + exponent_bits + mantissa_bits

    return ieee754_representation