a = []
n = int(input('数组长度'))
for i in range(0,n):
    a.append(int(input('数组元素')))

x = 1
b = []
for i in range(0,n):
    for k in range(0,i):
        x = x * a[k]
    for t in range(i+1,n):
        x = x * a[t]
    b.append(x)
    x = 1

for i in range(0,n):
    print(b[i])

