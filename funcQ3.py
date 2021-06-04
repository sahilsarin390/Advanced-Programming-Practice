def square(n):
    n = n**2
    return n

def twice(f):
    return square(f)

n = int(input("Enter a number: "))
quad = twice(square(n))
print(quad)