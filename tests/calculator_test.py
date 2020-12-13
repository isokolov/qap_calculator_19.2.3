import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    """def test_multiply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5"""

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 13, 4) == 9

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 3, 8) == 11

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 10, 4) == 2.5

    def test_modulo_calculate_correctly(self):
        assert self.calc.modulo(self, 10, 4) == 2
