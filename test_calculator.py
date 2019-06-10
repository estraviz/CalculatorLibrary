"""
Unit tests for the calculator library
"""

import calculator
import pytest


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division_ok(self):
        assert 2.5 == calculator.divide(10, 2)

    def test_division_by_zero(self):
        with pytest.raises(Exception) as excinfo:
            raise Exception('ERROR: Division by Zero')
        assert excinfo.value.message == 'ERROR: Division by Zero'
