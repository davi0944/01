a = float(input('一个十进制数：'))

b = a/1
b = int(b)
c = bin(b)
print(c, end="")

b = float(b)
d = a - b
if (d != 0):
    while (d != 0):
        d = 2 * d
        e = int(d)
        print(e, end="")
        d = d - e









