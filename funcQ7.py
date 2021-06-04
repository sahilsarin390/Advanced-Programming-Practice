import functools
import operator

player1 = [100, 20, 50, 66, 72, 32]
player2 = [56, 65, 78, 45, 33, 69]

mean1 = (functools.reduce(operator.add, player1)) / len(player1)
mean2 = (functools.reduce(operator.add, player2)) / len(player2)

m1 = [mean1] * len(player1)
m2 = [mean2] * len(player2)

def variance(p, m):
    var = p - m
    return var**2
    
sqvar1 = list(map(variance, player1, m1))
sqvar2 = list(map(variance, player2, m2))

var1 = (functools.reduce(operator.add, sqvar1)) / len(sqvar1)
var2 = (functools.reduce(operator.add, sqvar2)) / len(sqvar2)

sd1 = var1**0.5
sd2 = var2**0.5

if sd1 == sd2:
    print("Both players are consistent.")
elif sd1 > sd2:
    print("Player 2 is more consistent.")
else:
    print("Player 1 is more consistent.")
