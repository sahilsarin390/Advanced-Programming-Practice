from sympy import *
x, y, z, t = symbols('x y z t')

expr = linsolve([x + y - 2, 2*x + y], (x, y))

print(expr)