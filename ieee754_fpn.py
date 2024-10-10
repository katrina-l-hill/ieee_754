import math
import numpy as np
import matplotlib.pyplot as plt

def decimal_to_ieee754_32bit(decimal_number):
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

    print(f"Sign bit: {sign_bit}")
    print(f"Normalized number: {decimal_number}, Exponent: {exponent}")
    print(f"Exponent bits: {exponent_bits}")
    print(f"Mantissa bits: {mantissa_bits}")
    print(f"IEEE 754 Representation: {ieee754_representation}")

    return ieee754_representation

decimal_to_ieee754_32bit(decimal_number=13.125)

def ieee754_arithmetic_ops():
    a = 0.1
    b = 0.2
    c = 1.0
    d = 3.0

    sum_ab = a + b
    div_cd = c / d

    sum_ab_ieee = decimal_to_ieee754_32bit(sum_ab)
    div_cd_ieee = decimal_to_ieee754_32bit(div_cd)

    print(f"Initial values: a = {a}, b = {b}, c = {c}, d = {d}")
    print(f"Sum of a and b: {a} + {b} = {sum_ab}")
    print(f"Division of c by d: {c} / {d} = {div_cd}")
    print(f"IEEE 754 representation of sum_ab: {sum_ab_ieee}")
    print(f"IEEE 754 representation of div_cd: {div_cd_ieee}")

    return sum_ab_ieee, div_cd_ieee

ieee754_arithmetic_ops()

def ieee754_special_values():
    pos_inf = float('inf')
    neg_inf = float('-inf')
    nan = float('nan')

    print("Positive Infinity:", pos_inf)
    print("Negative Infinity:", neg_inf)
    print("NaN:", nan)

    return pos_inf, neg_inf, nan

ieee754_special_values()

def rounding_modes():
    # Round towards positive infinity
    result = math.ceil(2.5)  # Ceil always rounds up
    print("Round towards positive infinity:", result)

    # Round towards negative infinity
    result = math.floor(2.5)  # Floor always rounds down
    print("Round towards negative infinity:", result)

    # Round towards zero
    result = math.trunc(2.5)  # Truncate cuts off the decimal
    print("Round towards zero:", result)

    # Round to nearest integer
    result = round(2.5)  # Round to the nearest integer
    print("Round to nearest integer:", result)

rounding_modes()

def visualize_precision_loss():
    x = np.linspace(1e-40, 1e-30, 100)
    y = x + 1e-40

    plt.plot(x, y - x, label='Precision Loss')
    plt.xlabel('x')
    plt.ylabel('y - x')
    plt.title("Precision Loss in Floating-Point Arithmetic")
    plt.legend()
    plt.show()

visualize_precision_loss()
