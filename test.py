from ieee754_fpn import decimal_to_ieee754_32bit

def test_normal_cases():
    """
    Function to test decimal_to_ieee754_32bit for normal cases.
    """
    test_cases = [
        # Normal test cases
        (5.75, '01000000101110000000000000000000'),
        (-3.25, '11000000010101000000000000000000'),
        (0.125, '00111110000000000000000000000000'),
    ]
    
    for decimal_number, expected_output in test_cases:
        result = decimal_to_ieee754_32bit(decimal_number)
        assert result == expected_output, f"Test failed for {decimal_number}: got {result}, expected {expected_output}"
    
    print("All normal tests passed!")


def test_edge_cases():
    """
    Function to test decimal_to_ieee754_32bit for edge cases.
    """
    test_cases = [
        # Edge test cases
        (0.0, '00000000000000000000000000000000'),          # Zero
        (-0.0, '10000000000000000000000000000000'),         # Negative zero
        (float('inf'), '01111111100000000000000000000000'), # Positive infinity
    ]
    
    for decimal_number, expected_output in test_cases:
        result = decimal_to_ieee754_32bit(decimal_number)
        assert result == expected_output, f"Test failed for {decimal_number}: got {result}, expected {expected_output}"
    
    print("All edge tests passed!")
