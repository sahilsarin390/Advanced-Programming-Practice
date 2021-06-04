#(a)
feet = lambda m: m*(3.281)
meters = int(input("Enter the number of meters to be converted: "))
print("{:0.2f} feet".format(feet(meters)))

#(b)
square = lambda x: x**2
total = lambda f, b: lambda a: f(a)+b
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
print(total(square, b)(a))