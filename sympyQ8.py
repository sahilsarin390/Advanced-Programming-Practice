from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')

expr1 = integrate(x**2, x)
expr2 = integrate(x**2, y)
expr3 = integrate(sin(x), x)
expr4 = integrate(sin(x), y)
expr5 = integrate(cos(x), x)
expr6 = integrate(cos(x), y)

print(expr1)
print(expr2)
print(expr3)
print(expr4)
print(expr5)
print(expr6)