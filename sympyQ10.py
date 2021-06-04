from sympy import *
x, y, z, t = symbols('x y z t')

expr = linsolve(Matrix(([3, 7, -12], [4, -2, -5])), [x, y, z])

print(expr)