from sympy import *
x, y, z = symbols('x y z')
a=symbols('a')
m=Matrix( [[1, x, z], [y, 1, z] , [z,3,x]])
mat=m**(2)
print (mat)