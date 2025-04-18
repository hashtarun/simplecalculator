import unittest

from main import calculate

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(5, 3, '+'), 8)
        self.assertEqual(calculate(-5, 3, '+'), -2)
        self.assertEqual(calculate(0, 0, '+'), 0)

    def test_subtraction(self):
        self.assertEqual(calculate(5, 3, '-'), 2)
        self.assertEqual(calculate(-5, -3, '-'), -2)
        self.assertEqual(calculate(0, 5, '-'), -5)

    def test_multiplication(self):
        self.assertEqual(calculate(5, 3, '*'), 15)
        self.assertEqual(calculate(-5, 3, '*'), -15)
        self.assertEqual(calculate(0, 5, '*'), 0)

    def test_division(self):
        self.assertEqual(calculate(6, 3, '/'), 2)
        self.assertEqual(calculate(-6, 3, '/'), -2)
        self.assertEqual(calculate(0, 5, '/'), 0)

    def test_division_by_zero(self):
        self.assertEqual(calculate(5, 0, '/'), "Error: Division by zero is not allowed.")

if __name__ == "__main__":
    unittest.main()