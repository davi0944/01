import random
a = 100
b = 100
a = float(a)
b = float(b)
count1 = 0
count2 = 0
count1 = float(count1)
count2 = float(count2)

for i in range(1,100000001):
    x = random.uniform(0, a)
    y = random.uniform(0, b)
    if((x*x) + (y*y) > 10000):
        count1 = count1 + 1
    else:
        count2 = count2 + 1
z = 0
z = float(z)
z = 4 * count2/(count1 + count2)
print('%.10f'%z)