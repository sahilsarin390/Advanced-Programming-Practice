from sympy import *
x, y, z, t = symbols('x y z t')

expr = simplify((sin(x)-x)/x**3)
limexpr = limit(expr, x, 0)
print(limexpr)