operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y
}

expr = input('Enter expression: ')
a_str, op, b_str = expr.split()
a, b = float(a_str), float(b_str)
print(operators[op](a, b))
