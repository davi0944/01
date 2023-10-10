
n = int(input())

if (n % 3 == 1):
    a = (n+2)/3
    a = int(a)
    for i in range(a-2):
        print(3)
    print(2, 2)
elif (n % 3 == 2):
    a = (n+1)/3
    a = int(a)
    for i in range (a-1):
        print(3)
    print(2)
else:
    a = n/3
    a = int(a)
    for i in range(a):
        print(3)



