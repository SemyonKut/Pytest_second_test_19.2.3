import pytest
from calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    #Напишите по одному позитивному тесту для каждого метода калькулятора.

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 18, 6) == 3 #Деление тест

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 12, 5) == 7  # Вычитание тест

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 3, 2) == 5  # Сложение тест