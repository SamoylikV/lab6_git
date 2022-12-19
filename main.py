import unittest

def calculator(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b
    elif c == '**':
        return a ** b
    elif c == '%':
        return a % b
    else:
        return "Invalid operator"



class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator(1, 2, '+'), 3)

    def test_subtract(self):
        self.assertEqual(calculator(1, 2, '-'), -1)

    def test_multiply(self):
        self.assertEqual(calculator(1, 2, '*'), 2)

    def test_divide(self):
        self.assertEqual(calculator(1, 2, '/'), 0.5)

    def test_modulo(self):
        self.assertEqual(calculator(1, 2, '%'), 1)

    def test_exponent(self):
        self.assertEqual(calculator(1, 2, '**'), 1)

    def test_invalid_operator(self):
        self.assertEqual(calculator(1, 2, 'x'), "Invalid operator")


if __name__ == '__main__':
    unittest.main()
