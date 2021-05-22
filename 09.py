import sympy as sym

x = sym.Symbol('x')
res = sym.integrate(sym.exp(-x**2))
print(res)
