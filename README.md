# Understanding IEEE 754 Floating Point Numbers

## Author: Katrina Hill

## Description
This project provides a Python implementation for converting decimal numbers into their 32-bit IEEE 754 floating-point representation. It handles basic arithmetic operations, special floating-point values (such as NaN and infinity), and different rounding modes. Additionally, the project visualizes precision loss in floating-point arithmetic using Python’s `matplotlib`.

The code includes functions to:
- Convert decimal numbers to IEEE 754 32-bit format.
- Perform and floating-point arithmetic operations.
- Demonstrate the handling of special floating-point values.
- Explore different rounding methods.
- Visualize precision loss in floating-point arithmetic.

## Features
- **Decimal to IEEE 754 32-bit Conversion:**
  - Converts a decimal number into its 32-bit binary representation following the IEEE 754 standard.
  - Handles special cases like NaN, positive and negative infinity, and zero.
  
- **Floating-Point Arithmetic Operations:**
  - Performs basic arithmetic operations (addition and division) and converts the results to IEEE 754 32-bit format.

- **Handling Special Values:**
  - Demonstrates how Python manages floating-point special values such as positive infinity, negative infinity, and NaN.

- **Rounding Modes:**
  - Showcases different rounding methods such as rounding towards positive/negative infinity, rounding to zero, and rounding to the nearest integer.

- **Precision Loss Visualization:**
  - Plots and visualizes precision loss in floating-point arithmetic when dealing with very small numbers.

## Files
- `ieee754_fpn.py`: The main program that performs the base conversions.
- `test.py`: A suite of tests for validating the functionality of the base conversion logic.

# Requirements
- Python 3.11

# How to Run
1. **Clone the repository** (or download the files):
- git clone https://github.com/katrina-l-hill/ieee_754.git
- cd into the repository directory
2. **Run the Main program**:
- run python `ieee754_fpn.py` to run the program
3. **Run the tests**:
- run python -m pytest `test.py` to run the tests