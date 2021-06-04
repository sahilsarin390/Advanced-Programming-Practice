from sympy import *
x, y, z, t = symbols('x y z t')

expr = simplify(sin(x)/cos(x))
print(expr)