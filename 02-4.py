import math
g = 0
g = float(g)
a = int(input())
for i in range(0,a+1):
    if(i * i >= 2):
        g = i-1
while g * g < 2:
    g += 0.000001
print ("%.5f" % g)