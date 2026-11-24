import math
import unittest
from portable_roundoff import validate_derivative_row, sincos_decimal


class PortabilityTests(unittest.TestCase):
    def test_both_recorded_platform_values_satisfy_decimal_oracle(self):
        # Exact pair retained from the failed pre-publication Linux receipt.
        for value in [0.5403023028982545, 0.5403023084493697]:
            validate_derivative_row([1e-8, value, abs(value-math.cos(1.0))])
        sine, cosine = sincos_decimal(1.0)
        self.assertAlmostEqual(float(sine), math.sin(1.0), places=15)
        self.assertAlmostEqual(float(cosine), math.cos(1.0), places=15)

    def test_wrong_derivative_and_fabricated_error_are_rejected(self):
        h=1e-8
        value=(math.sin(1+h)-math.sin(1-h))/(2*h)
        with self.assertRaises(AssertionError):
            validate_derivative_row([h, value+1e-4, abs(value+1e-4-math.cos(1.0))])
        with self.assertRaises(AssertionError):
            validate_derivative_row([h, value, 0.01])
