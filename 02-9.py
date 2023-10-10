import math
import random
def num(x):
    x = x**2 + 4 * x * math.sin(x)
    return x

g = 0
for i in range(1,101):
    a = random.uniform(2, 3)
    g = g + num(a)

c = g/100
print (c)