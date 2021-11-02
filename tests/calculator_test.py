"""importing unitest for testcases"""
import unittest
from calculator.main import Calculator
class CalculatorTests(unittest.TestCase):
    """testing unittest of the calculator"""
    def setUp(self):
        """setting the self function of the calculator"""
        self.calculator = Calculator()


    def test_add_method(self):
        """Testing the Add function of the calculator"""
        result = self.calculator.add(4, 2)
        self.assertEqual(6, result)

    def test_add_method_invalid_value(self):
        """Testing the Add invalid function of the calculator"""
        self.assertRaises(ValueError, self.calculator.add, "four", "five")

    def test_sub_method(self):
        """Testing the sub function of the calculator"""
        result = self.calculator.sub(6, 4)
        self.assertEqual(2, result)

    def test_sub_method_invalid_value(self):
        """Testing the sub invalid function of the calculator"""
        self.assertRaises(ValueError, self.calculator.sub, "four", "five")

    def test_multiply_method(self):
        """Testing the mul function of the calculator"""
        result = self.calculator.multiply(5, 3)
        self.assertEqual(15, result)

    def test_multiply_method_invalid_value(self):
        """Testing the mul invalid function of the calculator"""
        self.assertRaises(ValueError, self.calculator.multiply, "four", "five")

    def test_div_method(self):
        """Testing the div function of the calculator"""
        result = self.calculator.div(5, 1)
        self.assertEqual(5, result)

    def test_div_method_invalid_value(self):
        """Testing the div invalid function of the calculator"""
        self.assertRaises(ValueError, self.calculator.div, "five", "four")

    def test_div_method_zero(self):
        """Testing the div zero function of the calculator"""
        self.assertRaises(ZeroDivisionError, self.calculator.div, 5, 0)


if __name__ == '__main__':
    unittest.main()
