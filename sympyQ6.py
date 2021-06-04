from sympy import *
x, y, z, t = symbols('x y z t')

expr1 = diff(log(x), x)
expr2 = diff((1/x), x)
expr3 = diff(sin(x), x)
expr4 = diff(cos(x), x)

print(expr1)
print(expr2)
print(expr3)
print(expr4)