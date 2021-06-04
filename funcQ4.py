#(a)
def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))

#(b)
import random
def outer(n):
    lst = random.sample(range(0,n+1), n)
    def inner():
        ind = random.randrange(0, n)
        return lst[ind]
    return inner

n = int(input("Enter a random number: "))
pick_number = outer(n)
print("Random number generated is: {}".format(pick_number()))