import random
a = []
n = random.randint(0,100)
for i in range(0,n):
    a.append(random.randint(0,100))

for i in range(0,n):
    for k in range(0,n-1):
        if(a[k] < a[k+1]):
            mid = a[k]
            a[k] = a[k+1]
            a[k+1] = mid

for i in range(0,n):
    print(a[i])