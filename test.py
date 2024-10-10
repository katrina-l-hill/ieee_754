from ieee754_fpn import decimal_to_ieee754_32bit, ieee754_arithmetic_ops

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