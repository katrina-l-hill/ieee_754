import math
from ieee754_fpn import decimal_to_ieee754_32bit, ieee754_arithmetic_ops, ieee754_special_values, rounding_modes

def test_normal_cases():
    """
    Test normal cases for decimal_to_ieee754_32bit.
    """
    test_cases = [
        (5.75, '01000000101110000000000000000000'),
        (-3.25, '11000000010100000000000000000000'),  
        (0.125, '00111110000000000000000000000000'),
    ]
    
    for decimal_number, expected_output in test_cases:
        assert decimal_to_ieee754_32bit(decimal_number) == expected_output, \
            f"Test failed for {decimal_number}: expected {expected_output}"

def test_edge_cases():
    """
    Test edge cases for decimal_to_ieee754_32bit.
    """
    test_cases = [
        (0.0, '00000000000000000000000000000000'),          # Zero
        (-0.0, '10000000000000000000000000000000'),         # Negative zero
        (float('inf'), '01111111100000000000000000000000'), # Positive infinity
    ]
    
    for decimal_number, expected_output in test_cases:
        assert decimal_to_ieee754_32bit(decimal_number) == expected_output, \
            f"Test failed for {decimal_number}: expected {expected_output}"

def test_ieee754_arithmetic_ops():
    expected_sum_ab = '00111110100110011001100110011001'  # IEEE 754 for 0.1 + 0.2
    expected_div_cd = '00111110101010101010101010101010'  # IEEE 754 for 1.0 / 3.0

    sum_ab_ieee, div_cd_ieee = ieee754_arithmetic_ops()

    assert sum_ab_ieee == expected_sum_ab, \
        f"Test failed for sum_ab_ieee: expected {expected_sum_ab}, got {sum_ab_ieee}"
    
    assert div_cd_ieee == expected_div_cd, \
        f"Test failed for div_cd_ieee: expected {expected_div_cd}, got {div_cd_ieee}"

def test_ieee754_special_values():
    """
    Test special IEEE 754 values: Positive Infinity, Negative Infinity, and NaN.
    """
    pos_inf, neg_inf, nan = ieee754_special_values()

    # Test Positive Infinity
    assert pos_inf == float('inf'), \
        f"Test failed for Positive Infinity: expected {float('inf')}, got {pos_inf}"

    # Test Negative Infinity
    assert neg_inf == float('-inf'), \
        f"Test failed for Negative Infinity: expected {float('-inf')}, got {neg_inf}"

    # Test NaN
    assert (nan != nan), \
        "Test failed for NaN: expected NaN, got a value equal to itself, which should not happen in NaN."

test_ieee754_special_values()

def test_rounding_modes():
    test_cases = [
        # Test ROUND_UP (ceil) – round towards positive infinity
        (2.5, math.ceil(2.5), "ROUND_UP"), 
        
        # Test ROUND_DOWN (floor) – round towards negative infinity
        (2.5, math.floor(2.5), "ROUND_DOWN"), 
        
        # Test ROUND_ZERO (trunc) – round towards zero
        (2.5, math.trunc(2.5), "ROUND_ZERO"),
        
        # Test ROUND_NEAREST (round) – round to nearest integer
        (2.5, round(2.5), "ROUND_NEAREST")
    ]
    
    for number, expected_result, mode in test_cases:
        # Perform the rounding operation based on the mode
        result = None
        if mode == "ROUND_UP":
            result = math.ceil(number)
        elif mode == "ROUND_DOWN":
            result = math.floor(number)
        elif mode == "ROUND_ZERO":
            result = math.trunc(number)
        elif mode == "ROUND_NEAREST":
            result = round(number)
        
        # Assert if the result is correct
        assert result == expected_result, \
            f"Test failed for {mode} mode with {number}: expected {expected_result}, got {result}"

test_rounding_modes()

