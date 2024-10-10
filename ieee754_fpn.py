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
    print(f"Sign bit: {sign_bit}")

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
    print(f"Normalized number: {decimal_number}, Exponent: {exponent}")

    # Calculate the exponent with the bias of 127
    exponent_bits = bin(exponent + 127)[2:].zfill(8)
    print(f"Exponent bits: {exponent_bits}")

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
    print(f"Mantissa bits: {mantissa_bits}")

    # Combine the sign bit, exponent, and mantissa
    ieee754_representation = sign_bit + exponent_bits + mantissa_bits
    print(f"IEEE 754 Representation: {ieee754_representation}")

    return ieee754_representation

decimal_to_ieee754_32bit(decimal_number=13.125)

def ieee754_arithmetic_ops():
    a = 0.1
    b = 0.2
    c = 1.0
    d = 3.0

    print(f"Initial values: a = {a}, b = {b}, c = {c}, d = {d}")

    sum_ab = a + b
    div_cd = c / d

    print(f"Sum of a and b: {a} + {b} = {sum_ab}")
    print(f"Division of c by d: {c} / {d} = {div_cd}")

    sum_ab_ieee = decimal_to_ieee754_32bit(sum_ab)
    div_cd_ieee = decimal_to_ieee754_32bit(div_cd)

    print(f"IEEE 754 representation of sum_ab: {sum_ab_ieee}")
    print(f"IEEE 754 representation of div_cd: {div_cd_ieee}")

    return sum_ab_ieee, div_cd_ieee

ieee754_arithmetic_ops()