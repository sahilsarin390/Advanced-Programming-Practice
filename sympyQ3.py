from sympy import *
x, y, z, t = symbols('x y z t')

expr = expand((x + y)**6)
print(expr)