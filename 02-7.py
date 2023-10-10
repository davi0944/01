c = int(input())
g = c/3
g = float(g)
while(abs(g*g*g-c)>0.000001):
    g = (2*g + c/(g*g))/3
print (g)