x = int(input())
y = int(input())
z = int(input())

if x < y:
    if y < z:
        print(x, y, z)
    elif x < z:
        print(x, z, y)
    else:
        print(z, x, y)
else:
    if x < z:
        print(y, x, z)
    elif y < z:
        print(y, z, x)
    else:
        print(z, y, x)