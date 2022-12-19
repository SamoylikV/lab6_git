import unittest
from main import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator(2, 4, '+'), 6)

    def test_subtract(self):
        self.assertEqual(calculator(4, 2, '-'), 2)

    def test_multiply(self):
        self.assertEqual(calculator(2, 2, '*'), 4)

    def test_divide(self):
        self.assertEqual(calculator(4, 2, '/'), 2)

    def test_power(self):
        self.assertEqual(calculator(2, 3, '**'), 8)

    def test_modulo(self):
        self.assertEqual(calculator(5, 2, '%'), 1)

    def test_invalid_operator(self):
        self.assertEqual(calculator(2, 4, 'a'), "Invalid operator")



if __name__ == '__main__':
    unittest.main()
