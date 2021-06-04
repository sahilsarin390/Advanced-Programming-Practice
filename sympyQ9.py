from sympy import *
x, y, z, t = symbols('x y z t')
f, g, h = symbols('f g h', cls=Function)

diffeq = Eq((f(x).diff(x, x)).diff(x, x) + 9*f(x) ,1)
expr = dsolve(diffeq, f(x))

print(expr)