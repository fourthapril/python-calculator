import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_positive(self):
        self.assertEqual(self.calc.add(5, 3), 8)
    
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-2, 4), 2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
    
    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
    
    def test_divide_remain(self):
        self.assertEqual(self.calc.divide(10, 3), 3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)

    def test_modulo_equal(self):
        self.assertEqual(self.calc.modulo(5, 5), 0)

if __name__ == '__main__':
    unittest.main()