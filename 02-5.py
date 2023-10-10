c = int(input())
g = c/2
g = float(g)
while(abs(g*g-c)>0.000001):
    g = (g + c/g)/2
print (g)

