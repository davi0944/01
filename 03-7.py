a = int(input("整数1"))
b = int(input("整数2"))

min = 0
count = 0

if(a<b):
    min = a + 1
else:
    min = b + 1

for i in range (1, min):
    if(a%i == 0 and b%i == 0):
        count = i

print(count)
