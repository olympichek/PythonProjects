from cmath import sqrt

a = -8
b = 57
c = -124
d = 81

p = (3*a*c - b**2) / (3 * a**2)
q = (2 * b**3 - 9*a*b*c + 27 * a**2 * d) / (27 * a**3)

Q = (p / 3) ** 3 + (q / 2) ** 3

alpha = (-(q / 2) + sqrt(Q)) ** (1 / 3)
beta  = (-(q / 2) - sqrt(Q)) ** (1 / 3)

y1 = alpha + beta
y2 = -((alpha + beta) / 2) + 1j * ((alpha - beta) / 2) * sqrt(3)
y3 = -((alpha + beta) / 2) - 1j * ((alpha - beta) / 2) * sqrt(3)

x1 = y1 - b / (3 * a)
x2 = y2 - b / (3 * a)
x3 = y3 - b / (3 * a)

print(x1, x2, x3, sep='\n')
