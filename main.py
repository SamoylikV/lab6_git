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



